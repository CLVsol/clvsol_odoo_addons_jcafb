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


class PersonSelect2018(models.TransientModel):
    _name = 'clv.person.select_2018'

    def _default_person_ids(self):
        return self._context.get('active_ids')
    person_ids = fields.Many2many(
        comodel_name='clv.person',
        relation='clv_person_select_2018_rel',
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

    def _person_document_setup(self, person, survey, history_marker_id, global_tag_id):

        _logger.info(u'%s %s', '>>>>>>>>>>', survey.title)

        Document = self.env['clv.document']
        document = Document.search([
            ('survey_id', '=', survey.id),
            ('person_id', '=', person.id),
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
                'person_id': person.id,
                'history_marker_id': history_marker_id,
                'global_tag_ids': [(4, global_tag_id)],
            }

            new_document = Document.create(values)

            category_id = new_document.get_document_category_id(survey)

            if category_id is not False:

                values = {
                    'category_ids': [(4, category_id)],
                }
                new_document.write(values)

            _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', new_document.name)

    def _person_lab_test_request_setup(self, person, lab_test_type, history_marker_id, global_tag_id):

        _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_type.name)

        LabTestRequest = self.env['clv.lab_test.request']
        lab_test_requests = LabTestRequest.search([
            ('lab_test_type_ids', '=', lab_test_type.id),
            ('person_id', '=', person.id),
            ('history_marker_id', '=', history_marker_id,),
        ])

        if lab_test_requests.id is False:

            m2m_list = []
            m2m_list.append((4, lab_test_type.id))

            _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', m2m_list)

            values = {
                'code_sequence': 'clv.lab_test.request.code',
                'lab_test_type_ids': m2m_list,
                'person_id': person.id,
                'history_marker_id': history_marker_id,
                'global_tag_ids': [(4, global_tag_id)],
            }
            lab_test_request = LabTestRequest.create(values)

            _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', lab_test_request.code)

    @api.multi
    def do_person_select_2018(self):
        self.ensure_one()

        Survey = self.env['survey.survey']
        LabTestType = self.env['clv.lab_test.type']

        PersonCategory = self.env['clv.person.category']
        person_category_id_crianca = PersonCategory.search([
            ('name', '=', 'Criança'),
        ])
        person_category_id_idoso = PersonCategory.search([
            ('name', '=', 'Idoso'),
        ])

        HistoryMarker = self.env['clv.history_marker']
        history_marker_id_jcafb_2018 = HistoryMarker.search([
            ('name', '=', 'JCAFB-2018'),
        ]).id

        for person in self.person_ids:

            _logger.info(u'%s %s', '>>>>>', person.name)

            if person_category_id_crianca in person.category_ids:

                person.state = 'selected'
                person.global_tag_ids = [(4, self.global_tag_id.id)]

                survey = Survey.search([
                    ('title', '=', '[TCR18]'),
                ])
                self._person_document_setup(person, survey, history_marker_id_jcafb_2018, self.global_tag_id.id)

                survey = Survey.search([
                    ('title', '=', '[QSC18]'),
                ])
                self._person_document_setup(person, survey, history_marker_id_jcafb_2018, self.global_tag_id.id)

                lab_test_type = LabTestType.search([
                    ('code', '=', 'ECP18'),
                ])
                self._person_lab_test_request_setup(person, lab_test_type, history_marker_id_jcafb_2018,
                                                    self.global_tag_id.id)

                lab_test_type = LabTestType.search([
                    ('code', '=', 'EEV18'),
                ])
                self._person_lab_test_request_setup(person, lab_test_type, history_marker_id_jcafb_2018,
                                                    self.global_tag_id.id)

            if person_category_id_idoso in person.category_ids:

                person.state = 'selected'
                person.global_tag_ids = [(4, self.global_tag_id.id)]

                survey = Survey.search([
                    ('title', '=', '[TID18]'),
                ])
                self._person_document_setup(person, survey, history_marker_id_jcafb_2018, self.global_tag_id.id)

                survey = Survey.search([
                    ('title', '=', '[QSI18]'),
                ])
                self._person_document_setup(person, survey, history_marker_id_jcafb_2018, self.global_tag_id.id)

                survey = Survey.search([
                    ('title', '=', '[QMD18]'),
                ])
                self._person_document_setup(person, survey, history_marker_id_jcafb_2018, self.global_tag_id.id)

                lab_test_type = LabTestType.search([
                    ('code', '=', 'ECP18'),
                ])
                self._person_lab_test_request_setup(person, lab_test_type, history_marker_id_jcafb_2018,
                                                    self.global_tag_id.id)

                lab_test_type = LabTestType.search([
                    ('code', '=', 'EUR18'),
                ])
                self._person_lab_test_request_setup(person, lab_test_type, history_marker_id_jcafb_2018,
                                                    self.global_tag_id.id)

            person.person_summary_setup(self.dir_path, self.file_name, self.global_tag_id.id)

        return True

    @api.multi
    def do_populate_all_persons(self):
        self.ensure_one()

        Person = self.env['clv.person']
        persons = Person.search([])

        self.person_ids = persons

        return self._reopen_form()
