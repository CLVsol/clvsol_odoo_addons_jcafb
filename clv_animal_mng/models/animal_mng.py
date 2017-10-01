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

from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import UserError

import re


class AnimalMng(models.Model):
    _description = 'Animal Management'
    _name = 'clv.animal.mng'
    _order = 'name'

    @api.multi
    @api.depends('name', 'code', 'age')
    def name_get(self):
        result = []
        for record in self:
            result.append(
                (record.id,
                 # u'%s [%s] (%s)' % (record.name, record.code, record.age)
                 u'%s (%s)' % (record.name, record.age)
                 ))
        return result

    name = fields.Char(string='Name', required=True)

    notes = fields.Text(string='Notes')

    spayed = fields.Selection(
        [('Y', 'Yes'),
         ('N', 'No')
         ], 'Spayed'
    )
    gender = fields.Selection(
        [('M', 'Male'),
         ('F', 'Female')
         ], string='Gender'
    )
    species_id = fields.Many2one(
        comodel_name='clv.animal.species',
        string='Species',
        ondelete='restrict'
    )
    breed_id = fields.Many2one(
        comodel_name='clv.animal.breed',
        string='Breed',
        ondelete='restrict',
        domain="[('species_id','in',species_id)]"
    )

    birthday = fields.Date(string="Date of Birth")
    age = fields.Char(
        string='Age',
        compute='_compute_age',
        store=True
    )
    estimated_age = fields.Char(string='Estimated Age', required=False)

    tutor_name = fields.Char(string='Tutor Name', required=False)
    tutor_id = fields.Many2one(comodel_name='clv.animal', string='Tutor', ondelete='restrict')

    active = fields.Boolean(string='Active', default=1)

    @api.multi
    @api.constrains('birthday')
    def _check_birthday(self):
        for animal in self:
            if animal.birthday > fields.Date.today():
                raise UserError(u'Date of Birth must be in the past!')

    @api.one
    @api.depends('birthday')
    def _compute_age(self):
        now = datetime.now()
        if self.birthday:
            dob = datetime.strptime(self.birthday, '%Y-%m-%d')
            delta = relativedelta(now, dob)
            # self.age = str(delta.years) + "y " + str(delta.months) + "m " + str(delta.days) + "d"
            self.age = str(delta.years)
        else:
            self.age = "No Date of Birth!"

    animal_id = fields.Many2one(comodel_name='clv.animal', string='Related Animal', ondelete='restrict')
    animal_spayed = fields.Selection(string='Animal Spayed', related='animal_id.spayed')
    animal_gender = fields.Selection(string='Animal Gender', related='animal_id.gender')
    animal_species_id = fields.Many2one(
        comodel_name='clv.animal.species',
        string='Animal Species',
        related='animal_id.species_id'
    )
    animal_breed_id = fields.Many2one(
        comodel_name='clv.animal.breed',
        string='Animal Breed',
        related='animal_id.breed_id'
    )
    animal_birthday = fields.Date(string='Animal Date of Birth', related='animal_id.birthday')
    animal_tutor_id = fields.Many2one(
        comodel_name='clv.person',
        string='Animal Tutor',
        related='animal_id.tutor_id'
    )
    animal_phone = fields.Char(string='Animal Phone', related='animal_id.phone')
    animal_mobile = fields.Char(string='Animal Mobile', related='animal_id.mobile')
    animal_category_ids = fields.Char(
        string='Animal Categories',
        related='animal_id.category_ids.name',
        store=True
    )
    animal_history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='Animal History Marker',
        related='animal_id.history_marker_id'
    )
    animal_address_id = fields.Many2one(
        comodel_name='clv.address',
        string='Animal Address',
        related='animal_id.address_id'
    )

    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    zip = fields.Char(string='ZIP code', change_default=True)
    state_id = fields.Many2one(comodel_name="res.country.state", string='State', ondelete='restrict')
    country_id = fields.Many2one(comodel_name='res.country', string='Country', ondelete='restrict')

    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')

    addr_category_ids = fields.Many2many(
        comodel_name='clv.address.category',
        relation='clv_animal_mng_addr_category_rel',
        column1='addr_id',
        column2='category_id',
        string='Address Categories'
    )
    addr_category_names = fields.Char(
        string='Address Category Names',
        compute='_compute_addr_category_names',
        store=True
    )
    addr_category_names_suport = fields.Char(
        string='Address Category Names Suport',
        compute='_compute_addr_category_names_suport',
        store=False
    )

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            return {'domain': {'state_id': [('country_id', '=', self.country_id.id)]}}
        else:
            return {'domain': {'state_id': []}}

    l10n_br_city_id = fields.Many2one(
        comodel_name='l10n_br_base.city',
        string='City',
        domain="[('state_id','=',state_id)]"
    )
    district = fields.Char(string='District')
    number = fields.Char(string='Number')

    @api.onchange('l10n_br_city_id')
    def onchange_l10n_br_city_id(self):
        if self.l10n_br_city_id:
            self.city = self.l10n_br_city_id.name
            self.l10n_br_city_id = self.l10n_br_city_id

    @api.onchange('zip')
    def onchange_mask_zip(self):
        if self.zip:
            val = re.sub('[^0-9]', '', self.zip)
            if len(val) == 8:
                zip = "%s-%s" % (val[0:5], val[5:8])
                self.zip = zip

    @api.multi
    def zip_search(self):
        self.ensure_one()
        obj_zip = self.env['l10n_br.zip']

        zip_ids = obj_zip.zip_search_multi(
            country_id=self.country_id.id,
            state_id=self.state_id.id,
            l10n_br_city_id=self.l10n_br_city_id.id,
            district=self.district,
            street=self.street,
            zip_code=self.zip,
        )

        if len(zip_ids) == 1:
            result = obj_zip.set_result(zip_ids[0])
            self.write(result)
            return True
        else:
            if len(zip_ids) > 1:
                obj_zip_result = self.env['l10n_br.zip.result']
                zip_ids = obj_zip_result.map_to_zip_result(
                    zip_ids, self._name, self.id)

                return obj_zip.create_wizard(
                    self._name,
                    self.id,
                    country_id=self.country_id.id,
                    state_id=self.state_id.id,
                    l10n_br_city_id=self.l10n_br_city_id.id,
                    district=self.district,
                    street=self.street,
                    zip_code=self.zip,
                    zip_ids=[zip.id for zip in zip_ids]
                )
            else:
                raise Warning(('Warning. No records found!'))

    @api.depends('addr_category_ids')
    def _compute_addr_category_names(self):
        for r in self:
            r.addr_category_names = r.addr_category_names_suport

    @api.multi
    def _compute_addr_category_names_suport(self):
        for r in self:
            addr_category_names = False
            for category in r.addr_category_ids:
                if addr_category_names is False:
                    addr_category_names = category.complete_name
                else:
                    addr_category_names = addr_category_names + ', ' + category.addr_complete_name
            r.addr_category_names_suport = addr_category_names
            if r.addr_category_names != addr_category_names:
                record = self.env['clv.animal.mng'].search([('id', '=', r.id)])
                record.write({'addr_category_ids': r.addr_category_ids})

    address_id = fields.Many2one(comodel_name='clv.address', string='Related Address', ondelete='restrict')
    address_code = fields.Char(string='Address Code', related='address_id.code', store=False)

    address_phone = fields.Char(string='Address Phone', related='address_id.phone')
    address_mobile_phone = fields.Char(string='Address Mobile', related='address_id.mobile')

    address_category_ids = fields.Char(
        string='Address Categories',
        related='address_id.category_ids.name',
        store=True
    )
    address_history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='Address History Marker',
        related='address_id.history_marker_id'
    )

    action_animal = fields.Selection(
        [('undefined', 'Undefined'),
         ('confirm', 'Confirm'),
         ('update', 'Update'),
         ('create', 'Create'),
         ('remove', 'Remove'),
         ('none', 'None'),
         ], string='Action (Animal)', default='undefined'
    )

    action_address = fields.Selection(
        [('undefined', 'Undefined'),
         ('confirm', 'Confirm'),
         ('update', 'Update'),
         ('create', 'Create'),
         ('remove', 'Remove'),
         ('none', 'None'),
         ], string='Action (Address)', default='undefined'
    )

    action_animal_address = fields.Selection(
        [('undefined', 'Undefined'),
         ('confirm', 'Confirm'),
         ('move', 'Move'),
         ('remove', 'Remove'),
         ('none', 'None'),
         ], string='Action (Animal Address)', default='undefined'
    )
