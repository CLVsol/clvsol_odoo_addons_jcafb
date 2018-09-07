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

# from odoo import api, fields, models
from odoo import fields, models


class Person(models.Model):
    _inherit = 'clv.person'

    person_document_ids = fields.One2many(
        string='Documents',
        related='partner_id.document_ids',
        readonly=False
    )
    person_count_documents = fields.Integer(
        string='Number of Documents',
        related='partner_id.count_documents',
        readonly=False
    )
    # document_ids = fields.One2many(
    #     comodel_name='clv.document',
    #     inverse_name='person_id',
    #     string='Documents'
    # )
    # count_documents = fields.Integer(
    #     string='Number of Documents',
    #     compute='_compute_count_documents'
    # )

    # @api.depends('document_ids')
    # def _compute_count_documents(self):
    #     for r in self:
    #         r.count_documents = len(r.document_ids)


class Document(models.Model):
    _inherit = 'clv.document'

    # person_id = fields.Many2one(
    #     comodel_name='clv.person',
    #     string='Person',
    #     ondelete='restrict'
    # )
    # person_code = fields.Char(
    #     string='Person Code',
    #     related='person_id.code',
    #     readonly=True
    # )
    # person_employee_id = fields.Many2one(
    #     comodel_name='hr.employee',
    #     string='Responsible Empĺoyee (Person)',
    #     related='person_id.address_id.employee_id',
    #     store=True
    # )
