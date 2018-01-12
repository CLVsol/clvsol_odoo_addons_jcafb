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

from odoo import models

_logger = logging.getLogger(__name__)


class Summary(models.Model):
    _name = "clv.summary"
    _inherit = 'clv.summary'

    def summary_export_xls_dir_path(self):
        return '/opt/openerp/clvsol_clvhealth_jcafb/summary_files/xls'

    def summary_export_xls_file_name(self):
        return '<category>_<code>.xls'

    def summary_export_xls(self, dir_path, file_name):

        if self.is_person_summary:
            category = 'Person'
            code = self.code
        if self.is_person_off_summary:
            category = 'Person_Off'
            code = self.code
        if self.is_address_summary:
            category = 'Address'
            code = self.code

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', dir_path),
        ])

        file_name = file_name.replace('<category>', category).replace('<code>', code)

        file_path = dir_path + '/' + file_name
        _logger.info(u'%s %s', '>>>>>>>>>>', file_path)

        book = xlwt.Workbook()

        if self.is_address_summary:

            sheet = book.add_sheet('AddressSummary_' + self.code)
            row_nr = 0

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Summary for:')
            row.write(3, self.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Summary date:')
            row.write(3, self.date_summary)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Responsible Employee:')
            row.write(3, self.address_employee_id.name)
            # row.write(5, self.address_employee_id.code)
            row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Address:')
            row.write(3, self.address_id.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(3, self.address_id.district)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Address Categories:')
            row.write(3, self.address_category_ids.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Address Code:')
            row.write(3, self.address_id.code)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Address State:')
            row.write(3, self.address_id.state)
            row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Document ')
            row.write(2, 'Code')
            row.write(4, 'Categories')
            row_nr += 1
            sheet.row(row_nr).height_mismatch = True
            sheet.row(row_nr).height = 20 * 4
            row_nr += 1

            for address_document in self.summary_address_document_ids:

                row = sheet.row(row_nr)
                row.write(0, address_document.document_id.name)
                row.write(2, address_document.document_id.code)
                row.write(4, address_document.document_category_ids.name)
                row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Person ')
            row.write(5, 'Code')
            row.write(7, 'Birthday')
            # row.write(8, 'Reference Age')
            # row.write(10, 'Categories')
            # row.write(12, 'Status')
            row.write(9, 'Categories')
            row.write(11, 'Status')
            row_nr += 1
            sheet.row(row_nr).height_mismatch = True
            sheet.row(row_nr).height = 20 * 4
            row_nr += 1

            for address_person in self.summary_address_person_ids:

                row = sheet.row(row_nr)
                row.write(0, address_person.person_id.name)
                row.write(5, address_person.person_id.code)
                if address_person.person_id.birthday is not False:
                    row.write(7, address_person.person_id.birthday)
                # if address_person.person_id.age_reference is not False:
                #     row.write(8, address_person.person_id.age_reference)
                # if address_person.person_category_ids.name is not False:
                #     row.write(10, address_person.person_category_ids.name)
                # row.write(12, address_person.person_state)
                if address_person.person_category_ids.name is not False:
                    row.write(9, address_person.person_category_ids.name)
                row.write(11, address_person.person_state)
                row_nr += 1

        if self.is_person_summary:

            sheet = book.add_sheet('PersonSummary_' + self.code)
            row_nr = 0

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Summary for:')
            row.write(3, self.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Summary date:')
            row.write(3, self.date_summary)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Responsible Employee:')
            row.write(3, self.person_employee_id.name)
            # row.write(5, self.person_employee_id.code)
            row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Address:')
            row.write(3, self.address_id.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(3, self.address_id.district)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Address Categories:')
            row.write(3, self.address_category_ids.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Address Code:')
            row.write(3, self.address_id.code)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Address State:')
            row.write(3, self.address_id.state)
            row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Person:')
            row.write(3, self.person_id.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Code:')
            row.write(3, self.person_id.code)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Person Categories:')
            row.write(3, self.person_category_ids.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Birthday:')
            if self.person_id.birthday is not False:
                row.write(3, self.person_id.birthday)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Reference Age:')
            if self.person_id.age_reference is not False:
                row.write(3, self.person_id.age_reference)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Person State:')
            row.write(3, self.person_id.state)
            row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Document ')
            row.write(2, 'Code')
            row.write(4, 'Categories')
            row_nr += 1
            sheet.row(row_nr).height_mismatch = True
            sheet.row(row_nr).height = 20 * 4
            row_nr += 1

            for person_document in self.summary_person_document_ids:

                row = sheet.row(row_nr)
                row.write(0, person_document.document_id.name)
                row.write(2, person_document.document_id.code)
                row.write(4, person_document.document_category_ids.name)
                row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Lab Test Type ')
            row.write(8, 'Lab Test Request')
            row_nr += 1
            sheet.row(row_nr).height_mismatch = True
            sheet.row(row_nr).height = 20 * 4
            row_nr += 1

            for person_lab_test_request in self.summary_person_lab_test_request_ids:

                row = sheet.row(row_nr)
                row.write(0, person_lab_test_request.lab_test_type_ids.name)
                row.write(8, person_lab_test_request.lab_test_request_id.code)
                row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Event ')
            # row.write(6, 'Code')
            row_nr += 1
            sheet.row(row_nr).height_mismatch = True
            sheet.row(row_nr).height = 20 * 4
            row_nr += 1

            for person_event in self.summary_person_event_ids:

                row = sheet.row(row_nr)
                row.write(0, person_event.event_id.name)
                # row.write(6, person_event.event_id.code)
                row_nr += 1

        if self.is_person_off_summary:

            sheet = book.add_sheet('PersonOffSummary_' + self.code)
            row_nr = 0

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Summary for:')
            row.write(3, self.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Summary date:')
            row.write(3, self.date_summary)
            # row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Responsible Employee:')
            # row.write(3, self.person_employee_id.name)
            # row.write(5, self.person_employee_id.code)
            row_nr += 1

            # row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Address:')
            # row.write(3, self.address_id.name)
            # row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(3, self.address_id.district)
            # row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Address Categories:')
            # row.write(3, self.address_category_ids.name)
            # row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Address Code:')
            # row.write(3, self.address_id.code)
            # row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Address State:')
            # row.write(3, self.address_id.state)
            # row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Person (Off):')
            row.write(3, self.person_off_id.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Code:')
            row.write(3, self.person_off_id.code)
            row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Person Categories:')
            # row.write(3, self.person_category_ids.name)
            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Birthday:')
            if self.person_off_id.birthday is not False:
                row.write(3, self.person_off_id.birthday)
            row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Reference Age:')
            # if self.person_off_id.age_reference is not False:
            #     row.write(3, self.person_off_id.age_reference)
            row = sheet.row(row_nr)
            row.write(0, 'Age:')
            if self.person_off_id.age is not False:
                row.write(3, self.person_off_id.age)
            row_nr += 1
            # row = sheet.row(row_nr)
            # row.write(0, 'Person State:')
            # row.write(3, self.person_off_id.state)
            # row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Document (Off)')
            row.write(2, 'Code')
            # row.write(4, 'Categories')
            row_nr += 1
            sheet.row(row_nr).height_mismatch = True
            sheet.row(row_nr).height = 20 * 4
            row_nr += 1

            for person_off_document in self.summary_person_off_document_ids:

                row = sheet.row(row_nr)
                row.write(0, person_off_document.document_off_id.name)
                row.write(2, person_off_document.document_off_id.code)
                # row.write(4, person_off_document.document_category_ids.name)
                row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Lab Test Type ')
            row.write(8, 'Lab Test (Off) Request')
            row_nr += 1
            sheet.row(row_nr).height_mismatch = True
            sheet.row(row_nr).height = 20 * 4
            row_nr += 1

            for person_off_lab_test_request in self.summary_person_off_lab_test_request_ids:

                row = sheet.row(row_nr)
                row.write(0, person_off_lab_test_request.lab_test_type_ids.name)
                row.write(8, person_off_lab_test_request.lab_test_off_request_id.code)
                row_nr += 1

            row_nr += 1
            row = sheet.row(row_nr)
            row.write(0, 'Event ')
            # row.write(6, 'Code')
            row_nr += 1
            sheet.row(row_nr).height_mismatch = True
            sheet.row(row_nr).height = 20 * 4
            row_nr += 1

            for person_off_event in self.summary_person_off_event_ids:

                row = sheet.row(row_nr)
                row.write(0, person_off_event.event_id.name)
                # row.write(6, person_event.event_id.code)
                row_nr += 1

            self.person_off_id.directory_id = file_system_directory.id
            self.person_off_id.file_name = file_name
            self.person_off_id.stored_file_name = file_name

        for i in range(12):
            sheet.col(i).width = 256 * 7
        sheet.show_grid = False

        book.save(file_path)

        self.directory_id = file_system_directory.id
        self.file_name = file_name
        self.stored_file_name = file_name

        return True
