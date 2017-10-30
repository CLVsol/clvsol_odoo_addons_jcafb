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

# from odoo import api, fields, models
from odoo import api, models

_logger = logging.getLogger(__name__)


class PersonSelGroupSetUp(models.TransientModel):
    _name = 'clv.person_sel.group.setup'

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
    def do_person_sel_group_setup(self):
        self.ensure_one()

        person_available_states = ['available', 'waiting', 'selected', 'unselected']
        person_selected_states = ['selected']

        PersonSelGroup = self.env['clv.person_sel.group']
        Person = self.env['clv.person']
        PersonCategory = self.env['clv.person.category']

        PersonSelDistrict = self.env['clv.person_sel.district']
        districts = PersonSelDistrict.search([])

        PersonSelAgeGroup = self.env['clv.person_sel.age_group']
        age_groups = PersonSelAgeGroup.search([])

        for district in districts:

            for age_group in age_groups:

                name = district.name + ' - ' + age_group.name

                _logger.info(u'%s %s', '>>>>>', name)

                person_sel_group = PersonSelGroup.search([
                    ('name', '=', name),
                ])

                if person_sel_group.id is False:

                    values = {
                        'name': name,
                        # 'code': code,
                        'district_id': district.id,
                        'age_group_id': age_group.id,
                    }
                    person_sel_group = PersonSelGroup.create(values)

                persons = Person.search([
                    ('state', 'in', person_available_states),
                    ('age_reference', '>=', age_group.min_age),
                    ('age_reference', '<=', age_group.max_age),
                ])
                count = 0
                for person in persons:
                    category_id = PersonCategory.search([
                        ('name', '=', age_group.person_category_ids.name),
                    ]).id
                    if (person.category_ids.id == category_id) and \
                       (person.address_id.district == district.name):
                        count += 1
                person_sel_group.available_persons = count

                persons = Person.search([
                    ('state', 'in', person_selected_states),
                    ('age_reference', '>=', age_group.min_age),
                    ('age_reference', '<=', age_group.max_age),
                ])
                count = 0
                for person in persons:
                    category_id = PersonCategory.search([
                        ('name', '=', age_group.person_category_ids.name),
                    ]).id
                    if (person.category_ids.id == category_id) and \
                       (person.address_id.district == district.name):
                        count += 1
                person_sel_group.selected_persons = count

        return True
