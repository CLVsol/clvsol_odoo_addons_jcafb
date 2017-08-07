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


class Documenmt(models.Model):
    _inherit = 'clv.document'

    reg_state = fields.Selection(
        [('draft', 'Draft'),
         ('revised', 'Revised'),
         ('done', 'Done'),
         ('cancelled', 'Cancelled')
         ], string='Register State', default='draft', readonly=True, required=True
    )

    @api.model
    def is_allowed_transition_reg_state(self, old_reg_state, new_reg_state):
        # allowed = [
        #     ('cancelled', 'draft'),
        #     ('draft', 'revised'),
        #     ('done', 'revised'),
        #     ('revised', 'done'),
        #     ('draft', 'cancelled'),
        #     ('revised', 'cancelled')
        # ]
        # return (old_reg_state, new_reg_state) in allowed
        return True

    @api.multi
    def change_reg_state(self, new_reg_state):
        for document in self:
            if document.is_allowed_transition_reg_state(document.reg_state, new_reg_state):
                document.reg_state = new_reg_state
            else:
                raise UserError(
                    'Status transition (' + document.reg_state + ', ' + new_reg_state + ') is not allowed!'
                )

    @api.multi
    def action_draft(self):
        for document in self:
            document.change_reg_state('draft')

    @api.multi
    def action_revised(self):
        for document in self:
            document.change_reg_state('revised')

    @api.multi
    def action_done(self):
        for document in self:
            document.change_reg_state('done')

    @api.multi
    def action_cancel(self):
        for document in self:
            document.change_reg_state('cancelled')
