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


class DataExportDocumentItem(models.Model):
    _description = 'Data Export Document Item'
    _name = "clv.data_export.document_item"
    _order = "sequence"

    name = fields.Char(string='Alias', index=False, required=False)

    data_export_id = fields.Many2one(
        comodel_name='clv.data_export',
        string='Data Export',
        ondelete='restrict'
    )

    document_item_id = fields.Many2one(
        comodel_name='clv.document.item',
        string='Document Item',
        ondelete='restrict',
        domain="[('document_type_id','!=',False')]"
    )
    document_item_code = fields.Char(string='Item Code', related='document_item_id.code', store=False)
    document_item_document_type_id = fields.Many2one(
        string='Item Type', related='document_item_id.document_type_id', store=False)
    document_item_name = fields.Char(string='Item', related='document_item_id.name', store=False)

    sequence = fields.Integer(
        string='Sequence',
        default=10
    )

    data_export_display = fields.Boolean(string='Display in Export', default=True)


class DataExport(models.Model):
    _inherit = 'clv.data_export'

    data_export_document_item_ids = fields.One2many(
        comodel_name='clv.data_export.document_item',
        inverse_name='data_export_id',
        string='Data Export Document Items'
    )

    count_data_export_document_items = fields.Integer(
        string='Data Export Document Items',
        compute='_compute_count_data_export_document_item',
        store=True
    )

    @api.depends('data_export_document_item_ids')
    def _compute_count_data_export_document_item(self):
        for r in self:
            r.count_data_export_document_items = len(r.data_export_document_item_ids)
