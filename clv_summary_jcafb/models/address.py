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


class Address(models.Model):
    _name = "clv.address"
    _inherit = 'clv.address'

    def address_summary_setup(self, dir_path, file_name, global_tag_id=False):
        self.ensure_one()

        Summary = self.env['clv.summary']
        SummaryAddressPerson = self.env['clv.summary.address.person']
        SummaryAddressDocument = self.env['clv.summary.address.document']

        _logger.info(u'%s %s', '>>>>>', self.name)

        summary = Summary.search([
            ('is_address_summary', '=', True),
            ('address_id', '=', self.id),
        ])

        if summary.id is False:

            name = self.name
            code = self.code
            address_id = self.id

            values = {
                'name': name,
                'code': code,
                'address_id': address_id,
                'is_address_summary': True,
            }
            if global_tag_id is not False:
                values['global_tag_ids'] = [(4, global_tag_id)]
            new_summary = Summary.create(values)
            _logger.info(u'%s %s', '>>>>>>>>>>', new_summary.name)

            summary_address_persons = SummaryAddressPerson.search([
                ('summary_id', '=', new_summary.id),
                ('address_id', '=', new_summary.address_id.id),
            ])
            summary_address_persons.unlink()

            for person in new_summary.address_id.person_ids:

                values = {
                    'summary_id': new_summary.id,
                    'address_id': new_summary.address_id.id,
                    'person_id': person.id,
                    'person_address_role_id': person.person_address_role_id.id,
                }
                SummaryAddressPerson.create(values)

            summary_address_documents = SummaryAddressDocument.search([
                ('summary_id', '=', new_summary.id),
                ('address_id', '=', new_summary.address_id.id),
            ])
            summary_address_documents.unlink()

            for document in new_summary.address_id.document_ids:

                if document.history_marker_id.id == new_summary.address_id.history_marker_id.id:

                    values = {
                        'summary_id': new_summary.id,
                        'address_id': new_summary.address_id.id,
                        'document_id': document.id,
                    }
                    SummaryAddressDocument.create(values)

            new_summary.summary_export_xls(dir_path, file_name)

        else:

            name = self.name
            code = self.code
            address_id = self.id

            summary.name = name
            summary.date_summary = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if global_tag_id is not False:
                summary.global_tag_ids = [(4, global_tag_id)]

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

            summary.summary_export_xls(dir_path, file_name)

        return True
