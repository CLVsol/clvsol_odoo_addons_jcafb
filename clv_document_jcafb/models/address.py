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


class Address(models.Model):
    _inherit = 'clv.address'

    document_ids = fields.One2many(
        comodel_name='clv.document',
        inverse_name='address_id',
        string='Documents'
    )
    count_documents = fields.Integer(
        string='Number of Documents',
        compute='_compute_count_documents'
    )

    @api.depends('document_ids')
    def _compute_count_documents(self):
        for r in self:
            r.count_documents = len(r.document_ids)


class Document(models.Model):
    _inherit = 'clv.document'

    address_id = fields.Many2one(
        comodel_name='clv.address',
        string='Address',
        ondelete='restrict'
    )
    address_code = fields.Char(
        string='Address Code',
        related='address_id.code',
        readonly=True
    )
    address_employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Responsible Empĺoyee (Address)',
        related='address_id.employee_id',
        store=True
    )
