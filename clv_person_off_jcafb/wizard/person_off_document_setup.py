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

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PersonOffDocumentOffSetUp(models.TransientModel):
    _name = 'clv.person.off.document_setup'

    def _default_person_off_ids(self):
        return self._context.get('active_ids')
    person_off_ids = fields.Many2many(
        comodel_name='clv.person.off',
        relation='clv_person_off_document_setup_rel',
        string='Persons (Off)',
        default=_default_person_off_ids
    )

    survey_ids = fields.Many2many(
        comodel_name='survey.survey',
        relation='clv_person_off_document_setup_survey_rel',
        string='Surveys'
    )

    category_id = fields.Many2one(
        comodel_name='clv.document.category',
        string='DocumentOff Category'
    )

    # date_foreseen = fields.Date(string='Foreseen Date', index=True)
    # date_deadline = fields.Date(string='Deadline', index=True)

    # history_marker_id = fields.Many2one(
    #     comodel_name='clv.history_marker',
    #     string='History Marker',
    #     ondelete='restrict'
    # )

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

    @api.multi
    def do_person_off_document_setup(self):
        self.ensure_one()

        DocumentOff = self.env['clv.document.off']
        Document = self.env['clv.document']
        DocumentOffCode = self.env['clv.document.off.code']

        for person_off in self.person_off_ids:

            _logger.info(u'%s %s', '>>>>>', person_off.name)

            for survey in self.survey_ids:

                _logger.info(u'%s %s', '>>>>>>>>>>', survey.title)

                document_off = DocumentOff.search([
                    ('survey_id', '=', survey.id),
                    ('person_off_id', '=', person_off.id),
                    # ('history_marker_id', '=', self.history_marker_id.id),
                ])

                if document_off.id is False:

                    values = {
                        'name': survey.title,
                        # 'code_sequence': 'clv.document.code',
                        # 'date_document': self.date_document,
                        # 'date_foreseen': self.date_foreseen,
                        # 'date_deadline': self.date_deadline,
                        'survey_id': survey.id,
                        # 'category_id': self.category_id.id,
                        'person_off_id': person_off.id,
                        # 'history_marker_id': self.history_marker_id.id,
                        'off_instance_id': person_off.off_instance_id.id,
                    }
                    new_document_off = DocumentOff.create(values)

                    if self.category_id.id is not False:

                        values = {
                            'category_ids': [(4, self.category_id.id)],
                        }
                        new_document_off.write(values)

                    else:

                        category_id = Document.get_document_category_id(survey)

                        if category_id is not False:

                            values = {
                                'category_ids': [(4, category_id)],
                            }
                            new_document_off.write(values)

                        _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', new_document_off.name)

                    document_off_codes = DocumentOffCode.search([
                        ('off_instance_id', '=', new_document_off.off_instance_id.id),
                        ('document_off_id', '=', False),
                    ])
                    for document_off_code in document_off_codes:
                        _logger.info(u'%s %s', '>>>>>>>>>>', document_off_code.code)
                        new_document_off.code = document_off_code.code
                        document_off_code.document_off_id = new_document_off.id
                        break

        return True
