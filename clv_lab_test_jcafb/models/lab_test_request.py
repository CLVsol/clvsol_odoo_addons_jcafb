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


class LabTestRequest(models.Model):
    _inherit = 'clv.lab_test.request'

    person_id = fields.Many2one(
        comodel_name='clv.person',
        string="Person",
        ondelete='restrict'
    )
    person_employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Responsible Empĺoyee (Person)',
        related='person_id.address_id.employee_id',
        store=True
    )


class Person(models.Model):
    _inherit = 'clv.person'

    lab_test_request_ids = fields.One2many(
        comodel_name='clv.lab_test.request',
        inverse_name='person_id',
        string='Lab Test Requests'
    )
