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


class EmployeeMngUpdate(models.TransientModel):
    _inherit = 'clv.employee.mng.updt'

    state = fields.Selection(
        [('draft', 'Draft'),
         ('revised', 'Revised'),
         ('verified', 'Verified'),
         ('ready', 'Ready'),
         ('done', 'Done'),
         ('undone', 'Undone'),
         ('cancelled', 'Cancelled')
         ], string='State', default='draft', readonly=False, required=False
    )
    state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='State', default=False, readonly=False, required=False
    )

    @api.multi
    def do_employee_mng_updt(self):
        self.ensure_one()

        super(EmployeeMngUpdate, self).do_employee_mng_updt()

        for employee in self.employee_mng_ids:

            _logger.info(u'%s %s', '>>>>>', employee.name)

            if self.state_selection == 'set':
                employee.state = self.state
            if self.state_selection == 'remove':
                employee.state = False

        return True
