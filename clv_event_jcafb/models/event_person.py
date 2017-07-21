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

from odoo import fields, models


class EventPerson(models.Model):
    _name = 'clv.event.person'

    event_id = fields.Many2one(
        comodel_name='clv.event',
        string='Event'
    )
    person_id = fields.Many2one(
        comodel_name='clv.person',
        string='Person'
    )

    role_id = fields.Many2one(
        comodel_name='clv.event.participant.role',
        string='Role',
        required=False
    )

    notes = fields.Text(string='Notes')

    active = fields.Boolean(string='Active', default=1)


class Event(models.Model):
    _inherit = 'clv.event'

    person_ids = fields.One2many(
        comodel_name='clv.event.person',
        inverse_name='event_id',
        string='Persons'
    )


class Person(models.Model):
    _inherit = 'clv.person'

    event_person_ids = fields.One2many(
        comodel_name='clv.event.person',
        inverse_name='person_id',
        string='Event Persons'
    )
