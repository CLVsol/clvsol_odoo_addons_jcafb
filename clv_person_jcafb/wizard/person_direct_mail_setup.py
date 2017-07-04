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


class PersonDirectMailSetUp(models.TransientModel):
    _name = 'clv.person.direct_mail.setup'

    person_ids = fields.Many2many(
        comodel_name='clv.person',
        relation='clv_person_person_direct_mail_setup_rel',
        string='Persons',
        domain=['|', ('active', '=', False), ('active', '=', True)],
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
    def do_person_direct_mail_setup(self):
        self.ensure_one()

        for person in self.person_ids:

            _logger.info(u'%s %s', '>>>>>', person.name)

        PersonDirectMail = self.env['clv.person.direct_mail']

        for person in self.person_ids:

            name = person.name
            code = person.code
            birthday = person.birthday
            age = person.age
            estimated_age = person.estimated_age
            date_reference = person.date_reference
            age_reference = person.age_reference
            gender = person.gender
            categories = ''
            for category in person.category_ids:
                if categories == '':
                    categories = category.name
                else:
                    categories += ';' + category.name
            reg_state = person.reg_state
            state = person.state
            responsible_name = person.responsible_id.name
            responsible_code = person.responsible_id.code

            address_name = person.address_id.name
            address_code = person.address_id.code
            address_categories = ''
            for category in person.address_id.category_ids:
                if address_categories == '':
                    address_categories = category.name
                else:
                    address_categories += ';' + category.name
            street = person.address_id.street
            number = person.address_id.number
            street2 = person.address_id.street2
            district = person.address_id.district
            l10n_br_city = person.address_id.l10n_br_city_id.name
            country_state = person.address_id.state_id.name
            country = person.address_id.country_id.name
            zip_code = person.address_id.zip
            email = person.address_id.email
            phone = person.address_id.phone
            mobile = person.address_id.mobile

            values = {
                'name': name,
                'code': code,
                'birthday': birthday,
                'age': age,
                'estimated_age': estimated_age,
                'date_reference': date_reference,
                'age_reference': age_reference,
                'gender': gender,
                'categories': categories,
                'reg_state': reg_state,
                'state': state,
                'responsible_name': responsible_name,
                'responsible_code': responsible_code,
                'address_name': address_name,
                'address_code': address_code,
                'address_categories': address_categories,
                'street': street,
                'number': number,
                'street2': street2,
                'district': district,
                'l10n_br_city': l10n_br_city,
                'country_state': country_state,
                'country': country,
                'zip_code': zip_code,
                'email': email,
                'phone': phone,
                'mobile': mobile,
            }
            PersonDirectMail.create(values)

        return True

    @api.multi
    def do_delete_all(self):
        self.ensure_one()

        PersonDirectMail = self.env['clv.person.direct_mail']

        all_person_direct_mail = PersonDirectMail.search([])
        all_person_direct_mail.unlink()

        return self._reopen_form()

    @api.multi
    def do_populate_all_persons(self):
        self.ensure_one()

        Person = self.env['clv.person']
        persons = Person.search([])

        self.person_ids = persons

        return self._reopen_form()

    @api.multi
    def do_populate_new_persons(self):
        self.ensure_one()

        PersonDirectMail = self.env['clv.person.direct_mail']

        Person = self.env['clv.person']
        persons = Person.search([])

        new_persons = []
        for person in persons:
            person_direct_mail = PersonDirectMail.search([
                ('code', '=', person.code),
            ])
            if person_direct_mail.id is False:
                new_persons.append(person.id)

        self.person_ids = new_persons

        return self._reopen_form()
