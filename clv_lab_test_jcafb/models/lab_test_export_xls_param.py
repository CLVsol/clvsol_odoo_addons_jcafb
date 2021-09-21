# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LabTestTypeExportXlsParam(models.Model):
    _description = 'Lab Test Export XLS Parameter'
    _name = "clv.lab_test.export_xls.param"

    lab_test_type_id = fields.Many2one(comodel_name='clv.lab_test.type', string='Test Type')

    display = fields.Selection(
        [('none', 'None'),
         ('result', 'Result'),
         ('report', 'Report')
         ], string='Display', default='none', readonly=False, required=True
    )

    parameter_type = fields.Selection(
        [('constant_char', 'Constant Char'),
         ('constant_int', 'Constant Integer'),
         ('constant_float', 'Constant Float'),
         ('image_file_name', 'Image File Name'),
         ('expression', 'Expression'),
         ('result_code', 'Result Code'),
         ('variable_name', 'Variable Name')
         ], string='Parameter Type', default='variable_name', readonly=False, required=True
    )

    parameter = fields.Char(string='Parameter')

    cell = fields.Char(string='Cell')

    col_nr = fields.Integer(string='Column Number')
    row_nr = fields.Integer(string='Row Number')

    active = fields.Boolean(string='Active', default=1)


class LabTestType(models.Model):
    _inherit = 'clv.lab_test.type'

    lab_test_export_xls_param_ids = fields.One2many(
        comodel_name='clv.lab_test.export_xls.param',
        inverse_name='lab_test_type_id',
        string='Lab Test Export XLS Parameters'
    )
