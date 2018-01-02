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


class LabTestParasite(models.Model):
    _description = 'Lab Test Parasite'
    _name = 'clv.lab_test.parasite'
    _order = 'name'

    name = fields.Char(string='Parasite', required=True)

    part1 = fields.Char(string='Part 1', required=False)
    part2 = fields.Char(string='Part 2', required=False)

    code = fields.Char(string='Parasite Code', required=False)

    notes = fields.Text(string='Notes')

    active = fields.Boolean(string='Active', default=1)

    _sql_constraints = [
        ('name_uniq',
         'UNIQUE(name)',
         u'Error! The Parasite must be unique!'
         ),
        ('code_uniq',
         'UNIQUE(code)',
         u'Error! The Parasite Code must be unique!'
         ),
    ]
