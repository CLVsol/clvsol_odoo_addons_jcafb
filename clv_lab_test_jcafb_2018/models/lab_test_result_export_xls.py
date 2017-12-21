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


class LabTestResult(models.Model):
    _name = "clv.lab_test.result"
    _inherit = 'clv.lab_test.result'

    def lab_test_result_export_xls(self, dir_path, file_name):

        lab_test_type = self.lab_test_type_id.code
        lab_test_request_code = self.lab_test_request_id.code

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', dir_path),
        ])

        file_name = file_name.replace('<type>', lab_test_type).replace('<request_code>', lab_test_request_code)
        file_path = dir_path + '/' + file_name

        _logger.info(u'%s %s %s', '>>>>>>>>>>', lab_test_request_code, lab_test_type)

        book = xlwt.Workbook()

        sheet = book.add_sheet(file_name)
        row_nr = 0

        save_book = False

        if lab_test_type == 'EAN18':
            return True

        if lab_test_type == 'ECP18':
            self.lab_test_result_export_xls_ECP18(sheet, row_nr)
            save_book = True

        if lab_test_type == 'EDH18':
            return True

        if lab_test_type == 'EEV18':
            self.lab_test_result_export_xls_EEV18(sheet, row_nr)
            save_book = True

        if lab_test_type == 'EUR18':
            self.lab_test_result_export_xls_EUR18(sheet, row_nr)
            save_book = True

        if save_book:

            book.save(file_path)

            self.directory_id = file_system_directory.id
            self.file_name = file_name
            self.stored_file_name = file_name

        return True
