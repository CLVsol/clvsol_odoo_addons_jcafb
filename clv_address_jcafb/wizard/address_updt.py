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


class AddressUpdate(models.TransientModel):
    _inherit = 'clv.address.updt'

    reg_state = fields.Selection(
        [('draft', 'Draft'),
         ('revised', 'Revised'),
         ('done', 'Done'),
         ('canceled', 'Canceled')
         ], string='Register State', default=False, readonly=False, required=False
    )
    reg_state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='Register State', default=False, readonly=False, required=False
    )

    state = fields.Selection(
        [('new', 'New'),
         ('available', 'Available'),
         ('waiting', 'Waiting'),
         ('selected', 'Selected'),
         ('unselected', 'Unselected'),
         ('unavailable', 'Unavailable')
         ], string='State', default=False, readonly=False, required=False
    )
    state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='State', default=False, readonly=False, required=False
    )

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Responsible Empĺoyee'
    )
    employee_id_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Responsible Empĺoyee', default=False, readonly=False, required=False
    )

    @api.multi
    def do_address_updt(self):
        self.ensure_one()

        super(AddressUpdate, self)

        for address in self.address_ids:

            _logger.info(u'%s %s', '>>>>>', address.name)

            if self.reg_state_selection == 'set':
                address.reg_state = self.reg_state
            if self.reg_state_selection == 'remove':
                address.reg_state = False

            if self.state_selection == 'set':
                address.state = self.state
            if self.state_selection == 'remove':
                address.state = False

            if self.employee_id_selection == 'set':
                address.employee_id = self.employee_id
            if self.employee_id_selection == 'remove':
                address.employee_id = False

        return True
