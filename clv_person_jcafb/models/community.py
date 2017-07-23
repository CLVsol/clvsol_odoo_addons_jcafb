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

from odoo import api, models, fields


class Community(models.Model):
    _inherit = 'clv.community'

    person_ids = fields.Many2many(
        comodel_name='clv.person',
        relation='clv_person_community_rel',
        column1='community_id',
        column2='person_id',
        string='Persons'
    )


class Person(models.Model):
    _inherit = 'clv.person'

    community_ids = fields.Many2many(
        comodel_name='clv.community',
        relation='clv_person_community_rel',
        column1='person_id',
        column2='community_id',
        string='Communities'
    )
    community_names = fields.Char(
        string='Community Names',
        compute='_compute_community_names',
        store=True
    )
    community_names_suport = fields.Char(
        string='Community Names Suport',
        compute='_compute_community_names_suport',
        store=False
    )

    @api.depends('community_ids')
    def _compute_community_names(self):
        for r in self:
            r.community_names = r.community_names_suport

    @api.multi
    def _compute_community_names_suport(self):
        for r in self:
            community_names = False
            for community in r.community_ids:
                if community_names is False:
                    community_names = community.name
                else:
                    community_names = community_names + ', ' + community.name
            r.community_names_suport = community_names
            if r.community_names != community_names:
                record = self.env['clv.person'].search([('id', '=', r.id)])
                record.write({'community_ids': r.community_ids})
