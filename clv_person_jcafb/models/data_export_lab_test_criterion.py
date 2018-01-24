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

from odoo import api, fields, models


class DataExportLabTestCriterion(models.Model):
    _description = 'Data Export Lab Test Criterion'
    _name = "clv.data_export.lab_test_criterion"
    _order = "sequence"

    name = fields.Char(string='Alias', index=False, required=False)

    data_export_id = fields.Many2one(
        comodel_name='clv.data_export',
        string='Data Export',
        ondelete='restrict'
    )

    lab_test_criterion_id = fields.Many2one(
        comodel_name='clv.lab_test.criterion',
        string='Lab Test Criterion',
        ondelete='restrict',
        domain="[('lab_test_type_id','!=',False')]"
    )
    lab_test_criterion_code = fields.Char(string='Item Code', related='lab_test_criterion_id.code', store=False)
    lab_test_criterion_lab_test_type_id = fields.Many2one(
        string='Item Type', related='lab_test_criterion_id.lab_test_type_id', store=False)
    lab_test_criterion_name = fields.Char(string='Item', related='lab_test_criterion_id.name', store=False)

    sequence = fields.Integer(
        string='Sequence',
        default=10
    )

    data_export_display = fields.Boolean(string='Display in Export', default=True)


class DataExport(models.Model):
    _inherit = 'clv.data_export'

    data_export_lab_test_criterion_ids = fields.One2many(
        comodel_name='clv.data_export.lab_test_criterion',
        inverse_name='data_export_id',
        string='Data Export Lab Test Criterions'
    )

    count_data_export_lab_test_criterions = fields.Integer(
        string='Data Export Lab Test Criterions',
        compute='_compute_count_data_export_lab_test_criterion',
        store=True
    )

    @api.depends('data_export_lab_test_criterion_ids')
    def _compute_count_data_export_lab_test_criterion(self):
        for r in self:
            r.count_data_export_lab_test_criterions = len(r.data_export_lab_test_criterion_ids)
