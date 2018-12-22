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


class LabTestRequestDirectMail(models.Model):
    _description = 'Lab Test Request Direct Mail'
    _name = 'clv.lab_test.request.direct_mail'
    _log_access = False
    _order = 'request_code'

    request_code = fields.Char(string='Request Code')
    lab_test_type = fields.Char(string='Lab Test Type')

    person_name = fields.Char(string='Person Name')
    person_code = fields.Char(string='Person Code')
    person_age_reference = fields.Char(string='Reference Age')
    person_category = fields.Char(string='Person Category')
    person_state = fields.Char(string='Person State')

    _sql_constraints = [
        ('request_code_uniq',
         'UNIQUE (request_code)',
         u'Error! The Request Code must be unique!'),
    ]
