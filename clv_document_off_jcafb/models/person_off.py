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


class PersonOff(models.Model):
    _inherit = 'clv.person.off'

    document_off_ids = fields.One2many(
        comodel_name='clv.document.off',
        inverse_name='person_off_id',
        string='Documents (Off)'
    )
    count_documents_off = fields.Integer(
        string='Number of Documents (Off)',
        compute='_compute_count_documents_off'
    )

    @api.depends('document_off_ids')
    def _compute_count_documents_off(self):
        for r in self:
            r.count_documents_off = len(r.document_off_ids)


class DocumentOff(models.Model):
    _inherit = 'clv.document.off'

    person_off_id = fields.Many2one(
        comodel_name='clv.person.off',
        string='Person (Off)',
        ondelete='restrict'
    )
    person_off_code = fields.Char(
        string='Person (Off) Code',
        related='person_off_id.code',
        readonly=True
    )
    # person_off_employee_id = fields.Many2one(
    #     comodel_name='hr.employee',
    #     string='Responsible Empĺoyee (Person)',
    #     related='person_off_id.address_id.employee_id',
    #     store=True
    # )
