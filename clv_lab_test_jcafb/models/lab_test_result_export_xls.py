# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import xlwt
from xlutils.copy import copy
from xlrd import open_workbook

from datetime import timedelta

# from os import listdir
# from os.path import isfile, join, exists, normpath, realpath
import os.path
from PIL import Image

from odoo import models

_logger = logging.getLogger(__name__)


class LabTestResult(models.Model):
    _name = "clv.lab_test.result"
    _inherit = 'clv.lab_test.result'

    def lab_test_result_export_xls(self, dir_path, file_name, use_template, template_dir_path):

        lab_test_type = self.lab_test_type_id.code
        lab_test_request_code = self.lab_test_request_id.code
        lab_test_result_code = self.code

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', dir_path),
        ])

        if use_template:
            template_file_name = self.lab_test_type_id.template_file_name_result
            template_file_path = template_dir_path + '/' + template_file_name
            book = open_workbook(template_file_path, formatting_info=True)
            wbook = copy(book)
            sheet = wbook.get_sheet(0)
            file_name = file_name.replace('<type>', lab_test_type).replace('<request_code>', lab_test_request_code)
            file_path = dir_path + '/' + file_name
            idx = book.sheet_names().index(template_file_name)
            wbook.get_sheet(idx).name = file_name
        else:
            file_name = file_name.replace('<type>', lab_test_type).replace('<request_code>', lab_test_request_code)
            file_path = dir_path + '/' + file_name
            wbook = xlwt.Workbook()
            sheet = wbook.add_sheet(file_name)

        logo_file_path = template_dir_path + '/' + 'jcafb.bmp'
        if not os.path.isfile(logo_file_path):
            img = Image.open(template_dir_path + '/' + 'jcafb.png')
            r, g, b, a = img.split()
            img = Image.merge('RGB', (r, g, b))
            img.save(logo_file_path)

        _logger.info(u'%s %s %s %s', '>>>>>>>>>>', lab_test_request_code, lab_test_type, use_template)

        save_book = False

        delta_hours = -3

        ExportXLS = self.env['clv.export_xls']

        ExportXLS.setOutCell(sheet, 11, 3, lab_test_request_code)
        ExportXLS.setOutCell(sheet, 35, 3, lab_test_result_code)

        ExportXLS.setOutCell(sheet, 11, 5, self.ref_id.name)
        ExportXLS.setOutCell(sheet, 11, 7, self.ref_id.code)

        ExportXLS.setOutCell(sheet, 11, 9, self.lab_test_request_id.employee_id.name)
        ExportXLS.setOutCell(sheet, 11, 10, self.lab_test_request_id.employee_id.code)
        ExportXLS.setOutCell(
            sheet, 11, 11,
            (self.lab_test_request_id.date_received + timedelta(hours=delta_hours)).strftime('%d-%m-%Y  %H:%M:%S')
        )

        save_book = True

        if save_book:

            wbook.save(file_path)

            self.directory_id = file_system_directory.id
            self.file_name = file_name
            self.stored_file_name = file_name

        return True
