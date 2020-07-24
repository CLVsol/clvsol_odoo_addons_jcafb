# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class DocumentTypeParameter(models.Model):
    _description = 'Document Type  '
    _name = "clv.document.type.parameter"
    _order = "name"

    name = fields.Char(string='Parameter')
    code = fields.Char(string='Parameter Code')

    parameter_type = fields.Char(sring='Parameter Type')

    document_type_id = fields.Many2one(comodel_name='clv.document.type', string='Document Type')

    active = fields.Boolean(string='Active', default=1)

    _sql_constraints = [
        ('name_uniq',
         'UNIQUE(document_type_id, name)',
         u'Error! The Parameter Name must be unique for a Document Type!'
         ),
    ]


class DocumentType(models.Model):
    _inherit = 'clv.document.type'

    parameter_ids = fields.One2many(
        comodel_name='clv.document.type.parameter',
        inverse_name='document_type_id',
        string='Parameters'
    )
