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


class LabTestOffReport(models.Model):
    _inherit = 'clv.lab_test.off.report'

    person_off_id = fields.Many2one(
        comodel_name='clv.person.off',
        string="Person (Off)",
        ondelete='restrict'
    )

    survey_id = fields.Many2one(
        comodel_name='survey.survey',
        string='Related Survey Type',
        related='lab_test_type_id.survey_id',
        store=True
    )

    approved = fields.Boolean(string='Approved', default=False)
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
    date_approved = fields.Date(
        string='Approved Date',
        readonly=True
    )

    lab_test_report_id = fields.Many2one(
        comodel_name='clv.lab_test.report',
        string="Related Lab Test Report",
        ondelete='restrict'
    )


class PersonOff(models.Model):
    _inherit = 'clv.person.off'

    lab_test_off_report_ids = fields.One2many(
        comodel_name='clv.lab_test.off.report',
        inverse_name='person_off_id',
        string='Lab Test (Off) Reports'
    )
