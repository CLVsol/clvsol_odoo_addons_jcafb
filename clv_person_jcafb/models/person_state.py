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


class Person(models.Model):
    _inherit = 'clv.person'

    state = fields.Selection(
        [('new', 'New'),
         ('available', 'Available'),
         ('waiting', 'Waiting'),
         ('selected', 'Selected'),
         ('unselected', 'Unselected'),
         ('unavailable', 'Unavailable'),
         ('unknown', 'Unknown')
         ], string='State', default='new', readonly=True, required=True
    )

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        # allowed = [
        #     ('unavailable', 'new'),
        #     ('new', 'available'),
        #     ('waiting', 'available'),
        #     ('selected', 'available'),
        #     ('unselected', 'available'),
        #     ('available', 'waiting'),
        #     ('available', 'selected'),
        #     ('waiting', 'selected'),
        #     ('unselected', 'selected'),
        #     ('available', 'unselected'),
        #     ('waiting', 'unselected'),
        #     ('selected', 'unselected'),
        #     ('new', 'unavailable'),
        #     ('available', 'unavailable')
        # ]
        # return (old_state, new_state) in allowed
        return True

    @api.multi
    def change_state(self, new_state):
        for person in self:
            if person.is_allowed_transition(person.state, new_state):
                person.state = new_state
            else:
                raise UserError('Status transition (' + person.state + ', ' + new_state + ') is not allowed!')

    @api.multi
    def action_new(self):
        for person in self:
            person.change_state('new')

    @api.multi
    def action_available(self):
        for person in self:
            person.change_state('available')

    @api.multi
    def action_waiting(self):
        for person in self:
            person.change_state('waiting')

    @api.multi
    def action_select(self):
        for person in self:
            person.change_state('selected')

    @api.multi
    def action_unselect(self):
        for person in self:
            person.change_state('unselected')

    @api.multi
    def action_unavailable(self):
        for person in self:
            person.change_state('unavailable')

    @api.multi
    def action_unknown(self):
        for person in self:
            person.change_state('unknown')


class PersonHistory(models.Model):
    _inherit = 'clv.person.history'

    state = fields.Selection(
        [('new', 'New'),
         ('available', 'Available'),
         ('waiting', 'Waiting'),
         ('selected', 'Selected'),
         ('unselected', 'Unselected'),
         ('unavailable', 'Unavailable'),
         ('unknown', 'Unknown')
         ], string='State', default='new', readonly=True, required=True
    )
