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


class PersonSel(models.Model):
    _description = 'Person Selection'
    _name = 'clv.person_sel'
    _order = 'name'

    name = fields.Char(string='Name', required=True)

    code = fields.Char(string='Code', required=False)

    available_persons = fields.Integer(string='Available Persons', required=False)
    selected_persons = fields.Integer(string='Selected Persons', required=False)

    notes = fields.Text(string='Notes')

    active = fields.Boolean(string='Active', default=1)

    _sql_constraints = [
        ('name_uniq',
         'UNIQUE(name)',
         u'Error! The Name must be unique!'
         ),
        ('code_uniq',
         'UNIQUE(code)',
         u'Error! The Code must be unique!'
         ),
    ]


# class PersonSel_2(models.Model):
#     _inherit = 'clv.person_sel'

#     person_category_ids = fields.Many2many(
#         comodel_name='clv.person.category',
#         relation='clv_person_sel_person_category_rel',
#         column1='person_sel_id',
#         column2='person_category_id',
#         string='Person Categories'
#     )
#     person_category_names = fields.Char(
#         string='Person Category Names',
#         compute='_compute_person_category_names',
#         store=True
#     )
#     person_category_names_suport = fields.Char(
#         string='Person Category Names Suport',
#         compute='_compute_person_category_names_suport',
#         store=False
#     )

#     @api.depends('person_category_ids')
#     def _compute_person_category_names(self):
#         for r in self:
#             r.person_category_names = r.person_category_names_suport

#     @api.multi
#     def _compute_person_category_names_suport(self):
#         for r in self:
#             person_category_names = False
#             for person_category in r.person_category_ids:
#                 if person_category_names is False:
#                     person_category_names = person_category.complete_name
#                 else:
#                     person_category_names = person_category_names + ', ' + person_category.complete_name
#             r.person_category_names_suport = person_category_names
#             if r.person_category_names != person_category_names:
#                 record = self.env['clv.person_sel'].search([('id', '=', r.id)])
#                 record.write({'person_category_ids': r.person_category_ids})


# class PersonSel_3(models.Model):
#     _inherit = "clv.person_sel"

#     addr_category_ids = fields.Many2many(
#         comodel_name='clv.address.category',
#         relation='clv_person_sel_addr_category_rel',
#         column1='person_sel_id',
#         column2='addr_category_id',
#         string='Address Categories'
#     )
#     addr_category_names = fields.Char(
#         string='Address Category Names',
#         compute='_compute_addr_category_names',
#         store=True
#     )
#     addr_category_names_suport = fields.Char(
#         string='Address Category Names Suport',
#         compute='_compute_addr_category_names_suport',
#         store=False
#     )

#     @api.depends('addr_category_ids')
#     def _compute_addr_category_names(self):
#         for r in self:
#             r.addr_category_names = r.addr_category_names_suport

#     @api.multi
#     def _compute_addr_category_names_suport(self):
#         for r in self:
#             addr_category_names = False
#             for addr_category in r.addr_category_ids:
#                 if addr_category_names is False:
#                     addr_category_names = addr_category.complete_name
#                 else:
#                     addr_category_names = addr_category_names + ', ' + addr_category.complete_name
#             r.addr_category_names_suport = addr_category_names
#             if r.addr_category_names != addr_category_names:
#                 record = self.env['clv.person_sel'].search([('id', '=', r.id)])
#                 record.write({'addr_category_ids': r.addr_category_ids})

#     @api.multi
#     def _compute_category_names_suport(self):
#         for r in self:
#             category_names = False
#             for category in r.category_ids:
#                 if category_names is False:
#                     category_names = category.complete_name
#                 else:
#                     category_names = category_names + ', ' + category.complete_name
#             r.category_names_suport = category_names
#             if r.category_names != category_names:
#                 record = self.env['clv.address'].search([('id', '=', r.id)])
#                 record.write({'category_ids': r.category_ids})
