# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class DocumentCodeOff(models.Model):
    _description = 'Document Code (Off)'
    _name = 'clv.document.code_off'
    _inherit = 'clv.abstract.code'
    _rec_name = 'code'
    _order = 'code'

    code = fields.Char(string='Document Code (Off)', required=False, default='/')
    code_sequence = fields.Char(default='clv.document.code')

    off_instance_id = fields.Many2one(comodel_name='clv.off.instance', string='Off Instance', ondelete='restrict')
    document_id = fields.Many2one(comodel_name='clv.document', string='Related Document', ondelete='restrict')

    notes = fields.Text(string='Notes')

    active = fields.Boolean(string='Active', default=1)

    _sql_constraints = [
        ('code_uniq',
         'UNIQUE (code)',
         u'Error! The Code must be unique!'),
    ]
