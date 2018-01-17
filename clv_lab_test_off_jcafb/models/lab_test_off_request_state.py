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


class LabTestOffRequest(models.Model):
    _inherit = 'clv.lab_test.off.request'

    state = fields.Selection(
        [('draft', 'Draft'),
         ('tested', 'Tested'),
         ('done', 'Done'),
         ('cancelled', 'Cancelled'),
         ], 'Status', default='draft', readonly=True
    )

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        # allowed = [
        #     ('draft', 'tested'),
        # ]
        # return (old_state, new_state) in allowed
        return True

    @api.multi
    def change_state(self, new_state):
        for lab_test_off_request in self:
            if lab_test_off_request.is_allowed_transition(lab_test_off_request.state, new_state):
                lab_test_off_request.state = new_state
            else:
                raise UserError('Status transition (' + lab_test_off_request.state + ', ' + new_state +
                                ') is not allowed!')

    @api.multi
    def action_draft(self):
        for lab_test_off_request in self:
            lab_test_off_request.change_state('draft')

    @api.multi
    def action_test(self):
        for lab_test_off_request in self:
            lab_test_off_request.change_state('tested')

    @api.multi
    def action_done(self):
        for lab_test_off_request in self:
            lab_test_off_request.change_state('done')

    @api.multi
    def action_cancel(self):
        for lab_test_off_request in self:
            lab_test_off_request.change_state('cancelled')
