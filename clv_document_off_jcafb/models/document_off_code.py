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

from odoo import fields, models


class DocumentOffCode(models.Model):
    _description = 'Document (Off) Code'
    _name = 'clv.document.off.code'
    _inherit = 'clv.code.model'
    _rec_name = 'code'
    _order = 'code'

    code = fields.Char(string='Document (Off) Code', required=False, default='/')
    code_sequence = fields.Char(default='clv.document.code')

    off_instance_id = fields.Many2one(
        comodel_name='clv.off.instance',
        string='Off Instance',
        ondelete='restrict'
    )
    document_off_id = fields.Many2one(
        comodel_name='clv.document.off',
        string='Related Document (Off)',
        ondelete='restrict'
    )

    notes = fields.Text(string='Notes')

    active = fields.Boolean(string='Active', default=1)

    _sql_constraints = [
        ('code_uniq',
         'UNIQUE (code)',
         u'Error! The Code must be unique!'),
    ]
