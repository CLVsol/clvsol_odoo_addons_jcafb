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

import logging
import xlwt
# import os.path
# from PIL import Image

from odoo import models

_logger = logging.getLogger(__name__)


class GroupSummary(models.Model):
    _name = "clv.group_summary"
    _inherit = 'clv.group_summary'

    # def group_summary_templates_dir_path(self):
    #     return '/opt/openerp/clvsol_clvhealth_jcafb/report_files/group_summary/templates'

    def group_summary_dir_path(self):
        return '/opt/openerp/clvsol_clvhealth_jcafb/report_files/group_summary/xls'

    def group_summary_file_name(self):
        return 'GroupSummary_<group_summary_code>.xls'

    # def group_summary_setup(self, dir_path, file_name, use_template, templates_dir_path):
    def group_summary_setup(self, dir_path, file_name):

        group_summary_code = self.code

        AddressCategory = self.env['clv.address.category']
        Address = self.env['clv.address']
        Person = self.env['clv.person']

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', dir_path),
        ])

        file_name = file_name.replace('<group_summary_code>', group_summary_code)

        file_path = dir_path + '/' + file_name
        _logger.info(u'%s %s', '>>>>>>>>>>', file_path)

        wbook = xlwt.Workbook()
        sheet = wbook.add_sheet(file_name)

        # sheet.header_str = ''
        # sheet.footer_str = ''

        for i in range(0, 49):
            sheet.col(i).width = 256 * 2
        sheet.show_grid = False

        # logo_file_path = templates_dir_path + '/' + 'jcafb.bmp'
        # if not os.path.isfile(logo_file_path):
        #     img = Image.open(templates_dir_path + '/' + 'jcafb.png')
        #     r, g, b, a = img.split()
        #     img = Image.merge('RGB', (r, g, b))
        #     img.save(logo_file_path)

        row_nr = 0

        row_nr += 1

        style_bold_str = 'font: bold on'
        style_bold = xlwt.easyxf(style_bold_str)

        style_str = 'font: bold on; font: italic on, height 256'
        style = xlwt.easyxf(style_str)
        sheet.write(row_nr, 0, self.name, style=style)
        sheet.row(row_nr).height = 256
        row_nr += 2

        col_address_category = 0
        col_district = 2
        col_address = 4
        col_person = 6

        address_categories = AddressCategory.search([])
        for address_category in address_categories:

            sheet.write(row_nr, col_address_category, address_category.name, style=style_bold)
            row_nr += 2

            addresses = Address.search([
                ('employee_id', '=', self.employee_id.id),
                ('category_names', '=', address_category.name),
            ])

            districts = []
            for address in addresses:
                if address.district not in districts:
                    districts.append(address.district)

            for district in districts:

                sheet.write(row_nr, col_district, district, style=style_bold)
                row_nr += 2

                addresses_2 = Address.search([
                    ('employee_id', '=', self.employee_id.id),
                    ('district', '=', district),
                    ('state', '=', 'selected'),
                ])

                for address_2 in addresses_2:

                    sheet.write(row_nr, col_address, '[' + address_2.code + ']')
                    sheet.write(row_nr, col_address + 7, address_2.name, style=style_bold)
                    sheet.write(row_nr, col_address + 36, address_2.state, style=style_bold)
                    row_nr += 2

                    persons = Person.search([
                        ('address_id', '=', address_2.id),
                        ('state', '=', 'selected'),
                    ])

                    for person in persons:

                        sheet.write(row_nr, col_person, '[' + person.code + ']')
                        sheet.write(row_nr, col_person + 7, person.name, style=style_bold)
                        sheet.write(row_nr, col_person + 30,
                                    '(' + person.category_names + ' - ' + person.age_reference + ')')
                        sheet.write(row_nr, col_person + 36, person.state)
                        row_nr += 2

                    persons = Person.search([
                        ('address_id', '=', address_2.id),
                        ('state', '=', 'waiting'),
                    ])

                    for person in persons:

                        sheet.write(row_nr, col_person, '[' + person.code + ']')
                        sheet.write(row_nr, col_person + 7, person.name, style=style_bold)
                        sheet.write(row_nr, col_person + 30,
                                    '(' + person.category_names + ' - ' + person.age_reference + ')')
                        sheet.write(row_nr, col_person + 36, person.state)
                        row_nr += 2

                addresses_2 = Address.search([
                    ('employee_id', '=', self.employee_id.id),
                    ('district', '=', district),
                    ('state', '=', 'waiting'),
                ])

                for address_2 in addresses_2:

                    sheet.write(row_nr, col_address, '[' + address_2.code + ']')
                    sheet.write(row_nr, col_address + 7, address_2.name, style=style_bold)
                    sheet.write(row_nr, col_address + 36, address_2.state, style=style_bold)
                    row_nr += 2

                    persons = Person.search([
                        ('address_id', '=', address_2.id),
                        ('state', '=', 'selected'),
                    ])

                    for person in persons:

                        sheet.write(row_nr, col_person, '[' + person.code + ']')
                        sheet.write(row_nr, col_person + 7, person.name, style=style_bold)
                        sheet.write(row_nr, col_person + 30,
                                    '(' + person.category_names + ' - ' + person.age_reference + ')')
                        sheet.write(row_nr, col_person + 36, person.state)
                        row_nr += 2

                    persons = Person.search([
                        ('address_id', '=', address_2.id),
                        ('state', '=', 'waiting'),
                    ])

                    for person in persons:

                        sheet.write(row_nr, col_person, '[' + person.code + ']')
                        sheet.write(row_nr, col_person + 7, person.name, style=style_bold)
                        sheet.write(row_nr, col_person + 30,
                                    '(' + person.category_names + ' - ' + person.age_reference + ')')
                        sheet.write(row_nr, col_person + 36, person.state)
                        row_nr += 2

        # style_str = 'borders: bottom dotted'
        # style = xlwt.easyxf(style_str)
        # for col in range(0, 10):
        #     sheet.write(row_nr, col, None, style=style)

        wbook.save(file_path)

        self.directory_id = file_system_directory.id
        self.file_name = file_name
        self.stored_file_name = file_name

        return True
