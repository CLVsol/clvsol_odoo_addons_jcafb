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


class LabTestReport(models.Model):
    _inherit = 'clv.lab_test.report'

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

    survey_id = fields.Many2one(
        comodel_name='survey.survey',
        string='Related Survey Type',
        related='lab_test_type_id.survey_id',
        store=True
    )

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Approved by',
        readonly=True
    )
    professional_id = fields.Char(
        comodel_name='hr.employee',
        string='Professional ID',
        related='employee_id.professional_id',
        store=False,
        readonly=True
    )
    date_approved = fields.Datetime(
        string='Received Date',
        readonly=True
    )


class Person(models.Model):
    _inherit = 'clv.person'

    lab_test_report_ids = fields.One2many(
        comodel_name='clv.lab_test.report',
        inverse_name='person_id',
        string='Lab Test Reports'
    )
