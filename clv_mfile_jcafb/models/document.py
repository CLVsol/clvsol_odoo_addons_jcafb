# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class MediaFile(models.Model):
    _inherit = 'clv.mfile'

    document_id = fields.Many2one(
        comodel_name='clv.document',
        string='Related Document'
    )
    document_code = fields.Char(
        string='Document Code',
        related='document_id.code',
        store=False,
        readonly=True
    )
    document_state = fields.Selection(
        string='Document State',
        related='document_id.state',
        store=True,
        readonly=True
    )