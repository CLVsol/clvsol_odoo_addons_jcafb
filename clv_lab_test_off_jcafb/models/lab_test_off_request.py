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


class LabTestOffRequest(models.Model):
    _inherit = 'clv.lab_test.off.request'

    person_off_id = fields.Many2one(
        comodel_name='clv.person.off',
        string="Person (Off)",
        ondelete='restrict'
    )

    document_off_id = fields.Many2one(
        comodel_name='clv.document.off',
        string='Related Document (Off)'
    )

    employee_id = fields.Many2one(comodel_name='hr.employee', string='Received by')
    date_received = fields.Datetime(string='Received Date')

    lab_test_request_id = fields.Many2one(
        comodel_name='clv.lab_test.request',
        string="Related Lab Test Requests",
        ondelete='restrict'
    )


class PersonOff(models.Model):
    _inherit = 'clv.person.off'

    lab_test_off_request_ids = fields.One2many(
        comodel_name='clv.lab_test.off.request',
        inverse_name='person_off_id',
        string='Lab Test (Off) Requests'
    )
