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


class PersonDirectMail(models.Model):
    _description = 'Person Direct Mail'
    _name = 'clv.person.direct_mail'
    _log_access = False
    _order = 'name'

    name = fields.Char(string='Name')
    code = fields.Char(string='Person Code')
    birthday = fields.Date(string="Date of Birth")
    age = fields.Char(strilng='Age')
    estimated_age = fields.Char(string='Estimated Age')
    date_reference = fields.Date(string="Reference Date")
    age_reference = fields.Char(string='Reference Age')
    gender = fields.Selection(
        [('M', 'Male'),
         ('F', 'Female')
         ], 'Gender'
    )
    categories = fields.Char(string='Categories')
    reg_state = fields.Selection(
        [('draft', 'Draft'),
         ('revised', 'Revised'),
         ('done', 'Done'),
         ('canceled', 'Canceled')
         ], string='Register State', default='draft', readonly=True, required=False
    )
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
    responsible_name = fields.Char(string='Responsible Name')
    responsible_code = fields.Char(string='Responsible Code')

    address_name = fields.Char(string='Address Name')
    address_code = fields.Char(string='Address Code')
    address_categories = fields.Char(string='Address Categories')
    street = fields.Char(string='Street')
    number = fields.Char(string=u'Number', size=10)
    street2 = fields.Char(string='Street2')
    district = fields.Char(string='District')
    l10n_br_city = fields.Char(string='City')
    country_state = fields.Char(string='State')
    country = fields.Char(string='Country')
    zip_code = fields.Char(string='ZIP code')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
