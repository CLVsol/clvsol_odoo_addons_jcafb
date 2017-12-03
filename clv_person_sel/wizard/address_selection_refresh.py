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


class AddressSelectionbRefresh(models.TransientModel):
    _name = 'clv.address.selection_refresh'

    def _default_address_ids(self):
        return self._context.get('active_ids')
    address_ids = fields.Many2many(
        comodel_name='clv.address',
        relation='clv_address_selection_refresh_rel',
        string='Addresses',
        default=_default_address_ids
    )

    non_selected_state = fields.Selection(
        [('new', 'New'),
         ('available', 'Available'),
         ('waiting', 'Waiting'),
         ('selected', 'Selected'),
         ('unselected', 'Unselected'),
         ('unavailable', 'Unavailable'),
         ('unknown', 'Unknown')
         ], string='Non Selected State', default='unselected', readonly=False, required=True
    )

    available_states = fields.Char(
        string='Available States',
        required=True,
        default='available; waiting; selected; unselected'
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
    def do_address_selection_refresh(self):
        self.ensure_one()

        available_states = self.available_states.replace(' ', '').replace(' ', '').split(';')

        for address in self.address_ids:

            _logger.info(u'%s %s', '>>>>>', address.name)

            if address.state in available_states:

                _logger.info(u'%s %s', '>>>>>>>>>>', address.state)

                selected_count = 0
                for person in address.person_ids:
                    if person.state == 'selected':
                        selected_count += 1

                _logger.info(u'%s %s', '>>>>>>>>>>', selected_count)

                if selected_count > 0:
                    address.state = 'selected'
                else:
                    if address.state == 'selected':
                        address.state = self.non_selected_state

                _logger.info(u'%s %s', '>>>>>>>>>>', address.state)

        return True

    @api.multi
    def do_populate_all_addresses(self):
        self.ensure_one()

        Address = self.env['clv.address']
        addresses = Address.search([])

        self.address_ids = addresses

        return self._reopen_form()
