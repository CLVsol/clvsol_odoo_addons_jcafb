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


class PersonSummarySetUp(models.TransientModel):
    _name = 'clv.person.summary_setup'

    def _default_person_ids(self):
        return self._context.get('active_ids')
    person_ids = fields.Many2many(
        comodel_name='clv.person',
        relation='clv_person_summary_setup_rel',
        string='Persones',
        default=_default_person_ids
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

    @api.multi
    def do_person_summary_setup(self):
        self.ensure_one()

        Summary = self.env['clv.summary']
        SummaryPersonDocument = self.env['clv.summary.person.document']
        SummaryPersonLabTestRequest = self.env['clv.summary.person.lab_test.request']

        for person in self.person_ids:

            _logger.info(u'%s %s', '>>>>>', person.name)

            summary = Summary.search([
                ('person_id', '=', person.id),
            ])

            if summary.id is False:

                name = person.name
                person_id = person.id
                address_id = person.address_id.id

                values = {
                    'name': name,
                    'person_id': person_id,
                    'is_person_summary': True,
                    'address_id': address_id,
                }
                new_summary = Summary.create(values)
                _logger.info(u'%s %s', '>>>>>>>>>>', new_summary.name)

                summary_person_documents = SummaryPersonDocument.search([
                    ('summary_id', '=', new_summary.id),
                    ('person_id', '=', new_summary.person_id.id),
                ])
                summary_person_documents.unlink()

                for document in new_summary.person_id.document_ids:

                    if document.history_marker_id.id == new_summary.person_id.history_marker_id.id:

                        values = {
                            'summary_id': new_summary.id,
                            'person_id': new_summary.person_id.id,
                            'document_id': document.id,
                        }
                        SummaryPersonDocument.create(values)

                summary_person_lab_test_requests = SummaryPersonLabTestRequest.search([
                    ('summary_id', '=', new_summary.id),
                    ('person_id', '=', new_summary.person_id.id),
                ])
                summary_person_lab_test_requests.unlink()

                for lab_test_request in new_summary.person_id.lab_test_request_ids:

                    if lab_test_request.history_marker_id.id == new_summary.person_id.history_marker_id.id:

                        values = {
                            'summary_id': new_summary.id,
                            'person_id': new_summary.person_id.id,
                            'lab_test_request_id': lab_test_request.id,
                        }
                        SummaryPersonLabTestRequest.create(values)

            else:

                name = person.name
                address_id = person.address_id.id

                summary.name = name
                summary.address_id = address_id

                _logger.info(u'%s %s', '>>>>>>>>>>', summary.name)

                summary_person_documents = SummaryPersonDocument.search([
                    ('summary_id', '=', summary.id),
                    ('person_id', '=', summary.person_id.id),
                ])
                summary_person_documents.unlink()

                for document in summary.person_id.document_ids:

                    if document.history_marker_id.id == summary.person_id.history_marker_id.id:

                        values = {
                            'summary_id': summary.id,
                            'person_id': summary.person_id.id,
                            'document_id': document.id,
                        }
                        SummaryPersonDocument.create(values)

                summary_person_lab_test_requests = SummaryPersonLabTestRequest.search([
                    ('summary_id', '=', summary.id),
                    ('person_id', '=', summary.person_id.id),
                ])
                summary_person_lab_test_requests.unlink()

                for lab_test_request in summary.person_id.lab_test_request_ids:

                    if lab_test_request.history_marker_id.id == summary.person_id.history_marker_id.id:

                        values = {
                            'summary_id': summary.id,
                            'person_id': summary.person_id.id,
                            'lab_test_request_id': lab_test_request.id,
                        }
                        SummaryPersonLabTestRequest.create(values)

        return True

    @api.multi
    def do_populate_all_persons(self):
        self.ensure_one()

        Person = self.env['clv.person']
        persons = Person.search([])

        self.person_ids = persons

        return self._reopen_form()
