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


class Person(models.Model):
    _name = "clv.person"
    _inherit = 'clv.person'

    def person_summary_setup(self, dir_path, file_name):

        Summary = self.env['clv.summary']
        SummaryPersonDocument = self.env['clv.summary.person.document']
        SummaryPersonLabTestRequest = self.env['clv.summary.person.lab_test.request']
        SummaryPersonEvent = self.env['clv.summary.person.event']

        _logger.info(u'%s %s', '>>>>>', self.name)

        summary = Summary.search([
            ('person_id', '=', self.id),
        ])

        if summary.id is False:

            name = self.name
            code = self.code
            person_id = self.id
            address_id = self.address_id.id

            values = {
                'name': name,
                'code': code,
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

            summary_person_events = SummaryPersonEvent.search([
                ('summary_id', '=', new_summary.id),
                ('person_id', '=', new_summary.person_id.id),
            ])
            summary_person_events.unlink()

            for event in new_summary.person_id.event_ids:

                if event.history_marker_id.id == new_summary.person_id.history_marker_id.id:

                    values = {
                        'summary_id': new_summary.id,
                        'person_id': new_summary.person_id.id,
                        'event_id': event.id,
                    }
                    SummaryPersonEvent.create(values)

            new_summary.summary_export_xls(self.dir_path, self.file_name)

        else:

            name = self.name
            code = self.code
            person_id = self.id
            address_id = self.address_id.id

            summary.name = name
            summary.address_id = address_id
            summary.date_summary = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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

            summary.summary_export_xls(dir_path, file_name)

        return True
