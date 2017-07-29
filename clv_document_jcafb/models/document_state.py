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


class Document(models.Model):
    _inherit = 'clv.document'

    state = fields.Selection(
        [('new', 'New'),
         ('available', 'Available'),
         ('waiting', 'Waiting'),
         ('returned', 'Returned'),
         ('archived', 'Archived'),
         ('discarded', 'Discarded')
         ], string='State', default='new', readonly=True, required=True
    )

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        # allowed = [
        #     ('discarded', 'new'),
        #     ('new', 'available'),
        # ]
        # return (old_state, new_state) in allowed
        return True

    @api.multi
    def change_state(self, new_state):
        for document in self:
            if document.is_allowed_transition(document.state, new_state):
                document.state = new_state
            else:
                raise UserError('Status transition (' + document.state + ', ' + new_state + ') is not allowed!')

    @api.multi
    def action_new(self):
        for document in self:
            document.change_state('new')

    @api.multi
    def action_available(self):
        for document in self:
            document.change_state('available')

    @api.multi
    def action_waiting(self):
        for document in self:
            document.change_state('waiting')

    @api.multi
    def action_returned(self):
        for document in self:
            document.change_state('returned')

    @api.multi
    def action_archive(self):
        for document in self:
            document.change_state('archived')

    @api.multi
    def action_discarded(self):
        for document in self:
            document.change_state('discarded')
