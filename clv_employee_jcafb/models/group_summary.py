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

from openerp import api, fields, models


class GroupSummary(models.Model):
    _description = 'Group Summary'
    _name = 'clv.group_summary'
    _inherit = 'clv.object.report', 'clv.code.model'

    code = fields.Char(string='Summary Code', required=False, default='/')
    code_sequence = fields.Char(default='clv.report.code')

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee',
        required=True,
        ondelete='restrict'
    )

    _sql_constraints = [
        ('code_uniq',
         'UNIQUE (code)',
         u'Error! The Code must be unique!'),
    ]


class Employee(models.Model):
    _name = "hr.employee"
    _inherit = 'hr.employee'

    group_summary_ids = fields.One2many(
        comodel_name='clv.group_summary',
        inverse_name='employee_id',
        string='Group Summaries',
        readonly=True
    )


class GroupSummary_2(models.Model):
    _inherit = 'clv.group_summary'

    name = fields.Char(
        string="Name", required=True, default=False,
        help='Use "/" to get an automatic new Group Summary Name.'
    )
    suggested_name = fields.Char(
        string="Suggested Name", required=False, store=True,
        compute="_get_suggested_name",
        help='Suggested Name for the Group Summary.'
    )
    automatic_set_name = fields.Boolean(
        string='Automatic Name',
        help="If checked, the Group Summary Name will be set automatically.",
        default=True
    )

    @api.depends('employee_id', 'history_marker_id')
    def _get_suggested_name(self):
        for record in self:
            record.suggested_name = 'Group Summary'
            if record.employee_id:
                record.suggested_name = record.suggested_name + ' - ' + record.employee_id.name
                if record.history_marker_id:
                    record.suggested_name = record.suggested_name + ' - ' + record.history_marker_id.name
            else:
                if not record.suggested_name:
                    if record.code:
                        record.suggested_name = record.code
            if record.automatic_set_name:
                record.name = record.suggested_name

    @api.multi
    def write(self, values):
        ret = super(GroupSummary_2, self).write(values)
        for record in self:
            if record.automatic_set_name:
                if record.name != record.suggested_name:
                    values['name'] = record.suggested_name
                    super(GroupSummary_2, record).write(values)
            else:
                if ('name' in values and values['name'] == '/') or \
                   (record.name == '/'):
                    values['name'] = record.suggested_name
                    super(GroupSummary_2, record).write(values)
        return ret
