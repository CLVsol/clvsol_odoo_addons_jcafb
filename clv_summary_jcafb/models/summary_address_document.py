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


class SummaryAddressDocument(models.Model):
    _description = 'Summary Address Document'
    _name = 'clv.summary.address.document'

    summary_id = fields.Many2one(
        comodel_name='clv.summary',
        string='Summary',
        index=True,
        ondelete='cascade'
    )
    address_id = fields.Many2one(
        comodel_name='clv.address',
        string='Address',
        ondelete='cascade'
    )
    document_id = fields.Many2one(
        comodel_name='clv.document',
        string='Document',
        ondelete='cascade'
    )
    document_global_tag_ids = fields.Many2many(
        string='Document Global Tags',
        related='document_id.global_tag_ids',
        store=False
    )
    document_category_ids = fields.Many2many(
        string='Document Categories',
        related='document_id.category_ids',
        store=False
    )
    document_state = fields.Selection(
        string='Document State',
        related='document_id.state',
        store=False
    )


class Summary(models.Model):
    _inherit = "clv.summary"

    summary_address_document_ids = fields.One2many(
        comodel_name='clv.summary.address.document',
        inverse_name='summary_id',
        string='Address Documents'
    )
