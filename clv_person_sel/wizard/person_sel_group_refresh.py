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


class PersonSelGroupRefresh(models.TransientModel):
    _name = 'clv.person_sel.group.refresh'

    def _default_group_ids(self):
        return self._context.get('active_ids')
    group_ids = fields.Many2many(
        comodel_name='clv.person_sel.group',
        relation='clv_person_sel_group_refresh_rel',
        string='Person Selection Groups',
        domain=['|', ('active', '=', False), ('active', '=', True)],
        default=_default_group_ids
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
    def do_person_sel_group_refresh(self):
        self.ensure_one()

        # person_available_states = ['available', 'waiting', 'selected', 'unselected']
        person_available_states = ['available', 'waiting', 'selected']
        person_selected_states = ['selected']

        Person = self.env['clv.person']
        PersonCategory = self.env['clv.person.category']

        for group in self.group_ids:

            _logger.info(u'%s %s', '>>>>>', group.name)

            persons = Person.search([
                ('state', 'in', person_available_states),
                ('age_reference', '>=', group.age_group_id.min_age),
                ('age_reference', '<=', group.age_group_id.max_age),
            ])
            count = 0
            for person in persons:
                category_id = PersonCategory.search([
                    ('name', '=', group.age_group_id.person_category_ids.name),
                ]).id
                if (person.category_ids.id == category_id) and \
                   (person.address_id.district == group.district_id.name):
                    count += 1
            group.available_persons = count

            persons = Person.search([
                ('state', 'in', person_selected_states),
                ('age_reference', '>=', group.age_group_id.min_age),
                ('age_reference', '<=', group.age_group_id.max_age),
            ])
            count = 0
            for person in persons:
                category_id = PersonCategory.search([
                    ('name', '=', group.age_group_id.person_category_ids.name),
                ]).id
                if (person.category_ids.id == category_id) and \
                   (person.address_id.district == group.district_id.name):
                    count += 1
            group.selected_persons = count

        return True

    @api.multi
    def do_populate_all(self):
        self.ensure_one()

        PersonSelGroup = self.env['clv.person_sel.group']
        person_sel_groups = PersonSelGroup.search([])

        self.group_ids = person_sel_groups

        return self._reopen_form()
