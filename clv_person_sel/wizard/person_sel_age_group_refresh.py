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


class PersonSelAgeGroupRefresh(models.TransientModel):
    _name = 'clv.person_sel.age_group.refresh'

    def _default_age_group_ids(self):
        return self._context.get('active_ids')
    age_group_ids = fields.Many2many(
        comodel_name='clv.person_sel.age_group',
        relation='clv_person_sel_age_group_refresh_rel',
        string='Person Selection Age-Groups',
        domain=['|', ('active', '=', False), ('active', '=', True)],
        default=_default_age_group_ids
    )

    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
        return action

    @api.multi
    def do_person_sel_age_group_refresh(self):
        self.ensure_one()

        # person_available_states = ['available', 'waiting', 'selected', 'unselected']
        person_available_states = ['available', 'waiting', 'selected']
        person_selected_states = ['selected']

        PersonCategory = self.env['clv.person.category']

        Person = self.env['clv.person']

        for age_group in self.age_group_ids:

            _logger.info(u'%s %s', '>>>>>', age_group.name)

            available_persons = Person.search([
                ('state', 'in', person_available_states),
                ('age_reference', '>=', age_group.min_age),
                ('age_reference', '<=', age_group.max_age),
            ])
            count = 0
            for available_person in available_persons:
                category_id = PersonCategory.search([
                    ('name', '=', age_group.person_category_ids.name),
                ]).id
                if available_person.category_ids.id == category_id:
                    count += 1
            age_group.available_persons = count

            selected_persons = Person.search([
                ('state', 'in', person_selected_states),
                ('age_reference', '>=', age_group.min_age),
                ('age_reference', '<=', age_group.max_age),
            ])
            count = 0
            for available_person in selected_persons:
                category_id = PersonCategory.search([
                    ('name', '=', age_group.person_category_ids.name),
                ]).id
                if available_person.category_ids.id == category_id:
                    count += 1
            age_group.selected_persons = count

        return True

    @api.multi
    def do_populate_all(self):
        self.ensure_one()

        PersonSelAgeGroup = self.env['clv.person_sel.age_group']
        person_sel_age_groups = PersonSelAgeGroup.search([])

        self.age_group_ids = person_sel_age_groups

        return self._reopen_form()
