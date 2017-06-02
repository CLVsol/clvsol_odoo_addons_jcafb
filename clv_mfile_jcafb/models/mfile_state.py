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


class Address(models.Model):
    _inherit = 'clv.mfile'

    state = fields.Selection(
        [('new', 'New'),
         ('returned', 'Returned'),
         ('checked', 'Checked'),
         ('validated', 'Validated'),
         ('imported', 'Imported'),
         ('archived', 'Archived'),
         ('discarded', 'Discarded'),
         ], string='State', default='new', readonly=True, required=True
    )

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        return True

    @api.multi
    def change_state(self, new_state):
        for mfile in self:
            if mfile.is_allowed_transition(mfile.state, new_state):
                mfile.state = new_state
            else:
                raise UserError('Status transition (' + mfile.state + ', ' + new_state + ') is not allowed!')

    @api.multi
    def action_new(self):
        for mfile in self:
            mfile.change_state('new')

    @api.multi
    def action_returned(self):
        for mfile in self:
            mfile.change_state('returned')

    @api.multi
    def action_checked(self):
        for mfile in self:
            mfile.change_state('checked')

    @api.multi
    def action_validated(self):
        for mfile in self:
            mfile.change_state('validated')

    @api.multi
    def action_imported(self):
        for mfile in self:
            mfile.change_state('imported')

    @api.multi
    def action_archived(self):
        for mfile in self:
            mfile.change_state('archived')

    @api.multi
    def action_discarded(self):
        for mfile in self:
            mfile.change_state('discarded')
