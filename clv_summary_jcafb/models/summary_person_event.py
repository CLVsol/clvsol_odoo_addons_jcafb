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

from openerp import fields, models


class SummaryPersonEvent(models.Model):
    _description = 'Summary Person Event'
    _name = 'clv.summary.person.event'

    summary_id = fields.Many2one(
        comodel_name='clv.summary',
        string='Summary',
        index=True,
        ondelete='cascade'
    )
    person_id = fields.Many2one(
        comodel_name='clv.person',
        string='Person',
        ondelete='cascade'
    )
    event_id = fields.Many2one(
        comodel_name='clv.event',
        string='Event',
        ondelete='cascade'
    )
    event_global_tag_ids = fields.Many2many(
        string='Event Global Tags',
        related='event_id.global_tag_ids',
        store=False
    )
    event_category_ids = fields.Many2many(
        string='Event Categories',
        related='event_id.category_ids',
        store=False
    )
    event_state = fields.Selection(
        string='Event State',
        related='event_id.state',
        store=False
    )


class Summary(models.Model):
    _inherit = "clv.summary"

    summary_person_event_ids = fields.One2many(
        comodel_name='clv.summary.person.event',
        inverse_name='summary_id',
        string='Person Events'
    )
