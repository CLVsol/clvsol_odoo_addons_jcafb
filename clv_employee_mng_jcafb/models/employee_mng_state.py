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

from openerp import api, fields, models
from openerp.exceptions import UserError


class EmployeeManagement(models.Model):
    _inherit = 'clv.employee.mng'

    state = fields.Selection(
        [('draft', 'Draft'),
         ('revised', 'Revised'),
         ('verified', 'Verified'),
         ('ready', 'Ready'),
         ('done', 'Done'),
         ('undone', 'Undone'),
         ('cancelled', 'Cancelled')
         ], string='State', default='draft', readonly=True, required=True
    )

    @api.model
    def is_allowed_transition(self, old_state, draft_state):
        # allowed = [
        #     ('cancelled', 'draft'),
        #     ('draft', 'revised'),
        #     ('ready', 'revised'),
        #     ('done', 'revised'),
        #     ('undone', 'revised'),
        #     ('revised', 'ready'),
        #     ('revised', 'done'),
        #     ('ready', 'done'),
        #     ('undone', 'done'),
        #     ('revised', 'undone'),
        #     ('ready', 'undone'),
        #     ('done', 'undone'),
        #     ('draft', 'cancelled'),
        #     ('revised', 'cancelled')
        # ]
        # return (old_state, draft_state) in allowed
        return True

    @api.multi
    def change_state(self, draft_state):
        for employee in self:
            if employee.is_allowed_transition(employee.state, draft_state):
                employee.state = draft_state
            else:
                raise UserError('Status transition (' + employee.state + ', ' + draft_state + ') is not allowed!')

    @api.multi
    def action_draft(self):
        for employee in self:
            employee.change_state('draft')

    @api.multi
    def action_revised(self):
        for employee in self:
            employee.change_state('revised')

    @api.multi
    def action_verified(self):
        for employee in self:
            employee.change_state('verified')

    @api.multi
    def action_ready(self):
        for employee in self:
            employee.change_state('ready')

    @api.multi
    def action_done(self):
        for employee in self:
            employee.change_state('done')

    @api.multi
    def action_cancelled(self):
        for employee in self:
            employee.change_state('cancelled')
