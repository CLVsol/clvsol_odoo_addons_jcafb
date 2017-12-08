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


class AddressSummarySetUp(models.TransientModel):
    _name = 'clv.address.summary_setup'

    def _default_address_ids(self):
        return self._context.get('active_ids')
    address_ids = fields.Many2many(
        comodel_name='clv.address',
        relation='clv_address_summary_setup_rel',
        string='Addresses',
        default=_default_address_ids
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
    def do_address_summary_setup(self):
        self.ensure_one()

        Summary = self.env['clv.summary']
        SummaryAddressPerson = self.env['clv.summary.address.person']
        SummaryAddressDocument = self.env['clv.summary.address.document']

        for address in self.address_ids:

            _logger.info(u'%s %s', '>>>>>', address.name)

            summary = Summary.search([
                ('is_address_summary', '=', True),
                ('address_id', '=', address.id),
            ])

            if summary.id is False:

                name = address.name
                address_id = address.id

                values = {
                    'name': name,
                    'address_id': address_id,
                    'is_address_summary': True,
                }
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

            else:

                name = address.name
                address_id = address.id

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

        return True

    @api.multi
    def do_populate_all_addresses(self):
        self.ensure_one()

        Address = self.env['clv.address']
        addresses = Address.search([])

        self.address_ids = addresses

        return self._reopen_form()
