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
from datetime import datetime

from odoo import models

_logger = logging.getLogger(__name__)


class PersonOff(models.Model):
    _name = "clv.person.off"
    _inherit = 'clv.person.off'

    def person_off_summary_setup(self, dir_path, file_name, global_tag_id=False):

        Summary = self.env['clv.summary']
        SummaryPersonOffDocument = self.env['clv.summary.person.off.document']
        SummaryPersonOffLabTestRequest = self.env['clv.summary.person.off.lab_test.request']
        SummaryPersonOffEvent = self.env['clv.summary.person.off.event']

        _logger.info(u'%s %s', '>>>>>', self.name)

        summary = Summary.search([
            ('person_off_id', '=', self.id),
        ])

        if summary.id is False:

            name = self.name
            code = self.code + '_off'
            person_off_id = self.id
            # address_id = self.address_id.id

            values = {
                'name': name,
                'code': code,
                'person_off_id': person_off_id,
                'is_person_off_summary': True,
                # 'address_id': address_id,
            }
            if global_tag_id is not False:
                values['global_tag_ids'] = [(4, global_tag_id)]
            new_summary = Summary.create(values)
            _logger.info(u'%s %s', '>>>>>>>>>>', new_summary.name)

            summary_person_off_documents = SummaryPersonOffDocument.search([
                ('summary_id', '=', new_summary.id),
                ('person_off_id', '=', new_summary.person_off_id.id),
            ])
            summary_person_off_documents.unlink()

            for document_off in new_summary.person_off_id.document_off_ids:

                # if document_off.history_marker_id.id == new_summary.person_off_id.history_marker_id.id:

                values = {
                    'summary_id': new_summary.id,
                    'person_off_id': new_summary.person_off_id.id,
                    'document_off_id': document_off.id,
                }
                SummaryPersonOffDocument.create(values)
                _logger.info(u'%s %s', '>>>>>>>>>>', values)

            summary_person_off_lab_test_requests = SummaryPersonOffLabTestRequest.search([
                ('summary_id', '=', new_summary.id),
                ('person_off_id', '=', new_summary.person_off_id.id),
            ])
            summary_person_off_lab_test_requests.unlink()

            for lab_test_off_request in new_summary.person_off_id.lab_test_off_request_ids:

                # if lab_test_off_request.history_marker_id.id == new_summary.person_off_id.history_marker_id.id:

                values = {
                    'summary_id': new_summary.id,
                    'person_off_id': new_summary.person_off_id.id,
                    'lab_test_off_request_id': lab_test_off_request.id,
                }
                SummaryPersonOffLabTestRequest.create(values)

            summary_person_events = SummaryPersonOffEvent.search([
                ('summary_id', '=', new_summary.id),
                ('person_off_id', '=', new_summary.person_off_id.id),
            ])
            summary_person_events.unlink()

            for event in new_summary.person_off_id.event_ids:

                # if event.history_marker_id.id == new_summary.person_off_id.history_marker_id.id:

                values = {
                    'summary_id': new_summary.id,
                    'person_off_id': new_summary.person_off_id.id,
                    'event_id': event.id,
                }
                SummaryPersonOffEvent.create(values)

            new_summary.summary_export_xls(dir_path, file_name)

        else:

            name = self.name
            code = self.code + '_off'
            person_off_id = self.id
            address_id = self.address_id.id

            summary.name = name
            summary.address_id = address_id
            summary.date_summary = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if global_tag_id is not False:
                summary.global_tag_ids = [(4, global_tag_id)]

            _logger.info(u'%s %s', '>>>>>>>>>>xx', summary.name)

            summary_person_off_documents = SummaryPersonOffDocument.search([
                ('summary_id', '=', summary.id),
                ('person_off_id', '=', summary.person_off_id.id),
            ])
            summary_person_off_documents.unlink()

            for document_off in summary.person_off_id.document_off_ids:

                # if document_off.history_marker_id.id == summary.person_off_id.history_marker_id.id:

                values = {
                    'summary_id': summary.id,
                    'person_off_id': summary.person_off_id.id,
                    'document_off_id': document_off.id,
                }
                SummaryPersonOffDocument.create(values)
                _logger.info(u'%s %s', '>>>>>>>>>>xx', values)

            summary_person_off_lab_test_requests = SummaryPersonOffLabTestRequest.search([
                ('summary_id', '=', summary.id),
                ('person_off_id', '=', summary.person_off_id.id),
            ])
            summary_person_off_lab_test_requests.unlink()

            for lab_test_off_request in summary.person_off_id.lab_test_off_request_ids:

                # if lab_test_off_request.history_marker_id.id == summary.person_off_id.history_marker_id.id:

                values = {
                    'summary_id': summary.id,
                    'person_off_id': summary.person_off_id.id,
                    'lab_test_off_request_id': lab_test_off_request.id,
                }
                SummaryPersonOffLabTestRequest.create(values)

            summary_person_events = SummaryPersonOffEvent.search([
                ('summary_id', '=', summary.id),
                ('person_off_id', '=', summary.person_off_id.id),
            ])
            summary_person_events.unlink()

            for event in summary.person_off_id.event_ids:

                # if event.history_marker_id.id == summary.person_off_id.history_marker_id.id:

                values = {
                    'summary_id': summary.id,
                    'person_off_id': summary.person_off_id.id,
                    'event_id': event.id,
                }
                SummaryPersonOffEvent.create(values)

            summary.summary_export_xls(dir_path, file_name)

        return True
