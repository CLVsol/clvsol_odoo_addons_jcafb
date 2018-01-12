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

from openerp import fields, models


class SummaryPersonOffLabTestRequest(models.Model):
    _description = 'Summary Person (Off) Lab Test Request'
    _name = 'clv.summary.person.off.lab_test.request'

    summary_id = fields.Many2one(
        comodel_name='clv.summary',
        string='Summary',
        index=True,
        ondelete='cascade'
    )
    person_off_id = fields.Many2one(
        comodel_name='clv.person.off',
        string='Person (Off)',
        ondelete='cascade'
    )
    lab_test_off_request_id = fields.Many2one(
        comodel_name='clv.lab_test.off.request',
        string='Lab Test (Off) Request',
        ondelete='cascade'
    )
    lab_test_type_ids = fields.Many2many(
        comodel_name='clv.lab_test.type',
        string='Lab Test Types',
        related='lab_test_off_request_id.lab_test_type_ids',
        store=False
    )
    # lab_test_off_request_state = fields.Selection(
    #     string='Lab Test (Off) Request State',
    #     related='lab_test_off_request_id.state',
    #     store=False
    # )


class Summary(models.Model):
    _inherit = "clv.summary"

    summary_person_off_lab_test_request_ids = fields.One2many(
        comodel_name='clv.summary.person.off.lab_test.request',
        inverse_name='summary_id',
        string='Person (Off) Lab Test Requests'
    )
