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


class SummaryPersonOffDocument(models.Model):
    _description = 'Summary Person (Off) Document'
    _name = 'clv.summary.person.off.document'

    summary_id = fields.Many2one(
        comodel_name='clv.summary',
        string='Summary',
        index=True,
        ondelete='cascade'
    )
    person_off_id = fields.Many2one(
        comodel_name='clv.person.off',
        string='Person (Off)',
        ondelete='cascade'
    )
    document_off_id = fields.Many2one(
        comodel_name='clv.document.off',
        string='Document (Off)',
        ondelete='cascade'
    )
    document_off_global_tag_ids = fields.Many2many(
        string='Document (off) Global Tags',
        related='document_off_id.global_tag_ids',
        store=False
    )
    document_off_state = fields.Selection(
        string='Document (Off) State',
        related='document_off_id.state',
        store=False
    )


class Summary(models.Model):
    _inherit = "clv.summary"

    summary_person_off_document_ids = fields.One2many(
        comodel_name='clv.summary.person.off.document',
        inverse_name='summary_id',
        string='Person (Off) Documents'
    )
