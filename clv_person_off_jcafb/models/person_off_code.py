# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PersonOffCode(models.Model):
    _description = 'Person (Off) Code'
    _name = 'clv.person_off.code'
    _inherit = 'clv.abstract.code'
    _rec_name = 'code'
    _order = 'code'

    code = fields.Char(string='Person (Off) Code', required=False, default='/')
    code_sequence = fields.Char(default='clv.person.code')

    off_instance_id = fields.Many2one(comodel_name='clv.off.instance', string='Off Instance', ondelete='restrict')
    person_off_id = fields.Many2one(comodel_name='clv.person_off', string='Related Person (Off)', ondelete='restrict')

    notes = fields.Text(string='Notes')

    active = fields.Boolean(string='Active', default=1)

    _sql_constraints = [
        ('code_uniq',
         'UNIQUE (code)',
         u'Error! The Code must be unique!'),
    ]
