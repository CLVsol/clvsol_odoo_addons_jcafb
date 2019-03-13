# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LabTestResultCodeOff(models.Model):
    _description = 'Lab Test Result Code (Off)'
    _name = 'clv.lab_test.result.code_off'
    _inherit = 'clv.abstract.code'
    _rec_name = 'code'
    _order = 'code'

    code = fields.Char(string='Lab Test Result Code (Off)', required=False, default='/')
    code_sequence = fields.Char(default='clv.lab_test.result.code')

    off_instance_id = fields.Many2one(comodel_name='clv.off.instance', string='Off Instance', ondelete='restrict')
    lab_test_result_id = fields.Many2one(
        comodel_name='clv.lab_test.result',
        string='Related Lab Test Result',
        ondelete='restrict'
    )

    notes = fields.Text(string='Notes')

    active = fields.Boolean(string='Active', default=1)

    _sql_constraints = [
        ('code_uniq',
         'UNIQUE (code)',
         u'Error! The Code must be unique!'),
    ]
