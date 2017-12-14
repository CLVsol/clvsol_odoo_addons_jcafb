# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import logging
# from datetime import datetime

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PersonAddressSelect2018(models.TransientModel):
    _name = 'clv.person.address_select_2018'

    def _default_person_ids(self):
        return self._context.get('active_ids')
    person_ids = fields.Many2many(
        comodel_name='clv.person',
        relation='clv_person_address_select_2018_rel',
        string='Persons',
        default=_default_person_ids
    )

    def _default_dir_path(self):
        Summary = self.env['clv.summary']
        return Summary.summary_export_xls_dir_path()
    dir_path = fields.Char(
        string='Directory Path',
        required=True,
        help="Directory Path",
        default=_default_dir_path
    )

    def _default_file_name(self):
        Summary = self.env['clv.summary']
        return Summary.summary_export_xls_file_name()
    file_name = fields.Char(
        string='File Name',
        required=True,
        help="File Name",
        default=_default_file_name
    )

    def _default_global_tag_id(self):
        GlobalTag = self.env['clv.global_tag']
        global_tag = GlobalTag.search([
            ('name', '=', 'Selecionado Recentemente'),
        ])
        global_tag_id = False
        if global_tag.id is not False:
            global_tag_id = global_tag.id
        else:
            values = {
                'name': 'Selecionado Recentemente',
                'description':
                    'O registro refere-se a uma Pessoa que tenha sido "selecionada" ' +
                    '(State = "Selected") recentemente.',
            }
            global_tag_id = GlobalTag.create(values).id
        return global_tag_id
    global_tag_id = fields.Many2one(
        comodel_name='clv.global_tag',
        string='Global Tag',
        ondelete='restrict',
        required=True,
        default=_default_global_tag_id
    )

    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
        return action

    def _address_document_setup(self, address, survey, history_marker_id, global_tag_id):

        _logger.info(u'%s %s', '>>>>>>>>>>', survey.title)
        _logger.info(u'%s %s', '>>>>>>>>>>>>>>>x', history_marker_id)

        Document = self.env['clv.document']
        document = Document.search([
            ('survey_id', '=', survey.id),
            ('address_id', '=', address.id),
            ('history_marker_id', '=', history_marker_id,),
        ])

        if document.id is False:

            values = {
                'name': survey.title,
                'code_sequence': 'clv.document.code',
                # 'date_document': self.date_document,
                # 'date_foreseen': self.date_foreseen,
                # 'date_deadline': self.date_deadline,
                'survey_id': survey.id,
                # 'category_id': self.category_id.id,
                'address_id': address.id,
                'history_marker_id': history_marker_id,
                'global_tag_ids': [(4, global_tag_id)],
            }
            _logger.info(u'%s %s', '>>>>>>>>>>>>>>>y', values)

            new_document = Document.create(values)

            category_id = new_document.get_document_category_id(survey)

            if category_id is not False:

                values = {
                    'category_ids': [(4, category_id)],
                }
                new_document.write(values)

            _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', new_document.name)

    @api.multi
    def do_person_address_select_2018(self):
        self.ensure_one()

        Survey = self.env['survey.survey']

        HistoryMarker = self.env['clv.history_marker']
        history_marker_id_jcafb_2018 = HistoryMarker.search([
            ('name', '=', 'JCAFB-2018'),
        ]).id

        for person in self.person_ids:

            address = person.address_id
            _logger.info(u'%s %s', '>>>>>', person.name)
            _logger.info(u'%s %s', '>>>>>', address.name)

            if address.state != 'selected':

                address.state = 'selected'
                address.global_tag_ids = [(4, self.global_tag_id.id)]

                survey = Survey.search([
                    ('title', '=', '[QSF18]'),
                ])
                self._address_document_setup(address, survey, history_marker_id_jcafb_2018, self.global_tag_id.id)

            # else:

            #     address.global_tag_ids = [(4, self.global_tag_id.id)]

            address.address_summary_setup(self.dir_path, self.file_name, self.global_tag_id.id)

        return True

    @api.multi
    def do_populate_all_persons(self):
        self.ensure_one()

        Person = self.env['clv.person']
        persons = Person.search([])

        self.person_ids = persons

        return self._reopen_form()
