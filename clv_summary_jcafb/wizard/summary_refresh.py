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


class SummaryRefresh(models.TransientModel):
    _name = 'clv.summary.refresh'

    def _default_summary_ids(self):
        return self._context.get('active_ids')
    summary_ids = fields.Many2many(
        comodel_name='clv.summary',
        relation='clv_summary_refresh_rel',
        string='Summaries',
        default=_default_summary_ids
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
    def do_summary_refresh(self):
        self.ensure_one()

        SummaryAddressPerson = self.env['clv.summary.address.person']
        SummaryAddressDocument = self.env['clv.summary.address.document']
        SummaryPersonDocument = self.env['clv.summary.person.document']
        SummaryPersonLabTestRequest = self.env['clv.summary.person.lab_test.request']
        SummaryPersonEvent = self.env['clv.summary.person.event']

        for summary in self.summary_ids:

            _logger.info(u'%s %s', '>>>>>', summary.name)

            if summary.is_address_summary:

                _logger.info(u'%s %s', '>>>>>>>>>>', 'is_address_summary')

                name = summary.address_id.name

                summary.name = name

                _logger.info(u'%s %s', '>>>>>>>>>>', summary.name)

                summary_address_persons = SummaryAddressPerson.search([
                    ('summary_id', '=', summary.id),
                    ('address_id', '=', summary.address_id.id),
                ])
                summary_address_persons.unlink()

                for person in summary.address_id.person_ids:

                    values = {
                        'summary_id': summary.id,
                        'address_id': summary.address_id.id,
                        'person_id': person.id,
                        'person_address_role_id': person.person_address_role_id.id,
                    }
                    SummaryAddressPerson.create(values)

                summary_address_documents = SummaryAddressDocument.search([
                    ('summary_id', '=', summary.id),
                    ('address_id', '=', summary.address_id.id),
                ])
                summary_address_documents.unlink()

                for document in summary.address_id.document_ids:

                    if document.history_marker_id.id == summary.address_id.history_marker_id.id:

                        values = {
                            'summary_id': summary.id,
                            'address_id': summary.address_id.id,
                            'document_id': document.id,
                        }
                        SummaryAddressDocument.create(values)

            elif summary.is_person_summary:

                _logger.info(u'%s %s', '>>>>>>>>>>', 'is_person_summary')

                name = summary.person_id.name
                address_id = summary.person_id.address_id.id

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

                summary_person_events = SummaryPersonEvent.search([
                    ('summary_id', '=', summary.id),
                    ('person_id', '=', summary.person_id.id),
                ])
                summary_person_events.unlink()

                for event in summary.person_id.event_ids:

                    if event.history_marker_id.id == summary.person_id.history_marker_id.id:

                        values = {
                            'summary_id': summary.id,
                            'person_id': summary.person_id.id,
                            'event_id': event.id,
                        }
                        SummaryPersonEvent.create(values)

            summary.summary_export_xls(self.dir_path, self.file_name)

        return True

    @api.multi
    def do_populate_all_summaries(self):
        self.ensure_one()

        Summary = self.env['clv.summary']
        summaries = Summary.search([])

        self.summary_ids = summaries

        return self._reopen_form()
