# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import xlwt
from xlutils.copy import copy
from xlrd import open_workbook
from datetime import datetime

from shutil import copyfile

import os.path
from PIL import Image

from odoo import models

_logger = logging.getLogger(__name__)


class LabTestReport(models.Model):
    _name = "clv.lab_test.report"
    _inherit = 'clv.lab_test.report'

    def lab_test_report_export_xls(self, dir_path, file_name, use_template, template_dir_path):

        lab_test_type = self.lab_test_type_id.code
        lab_test_request_code = self.lab_test_request_id.code

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', dir_path),
        ])

        if use_template:
            template_file_name = self.lab_test_type_id.template_file_name_report
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

        ExportXLS = self.env['clv.export_xls']

        sheet.insert_bitmap(logo_file_path, 0, 3)

        ExportXLS.setOutCell(sheet, 6, 7, self.ref_id.name)
        ExportXLS.setOutCell(sheet, 35, 7, self.ref_id.code)
        date = datetime.strftime(self.date_approved, '%d-%m-%Y')
        ExportXLS.setOutCell(sheet, 9, 9, date)
        ExportXLS.setOutCell(sheet, 38, 9, lab_test_request_code)

        result = self.criterion_ids.search([
            ('lab_test_result_id', '=', self.lab_test_result_id.id),
            ('code', '=', 'EAN21_03_02'),
        ]).result
        if result is not False:
            ExportXLS.setOutCell(sheet, 16, 23, result)

        result_peso = self.criterion_ids.search([
            ('lab_test_result_id', '=', self.lab_test_result_id.id),
            ('code', '=', 'EAN21_02_01'),
        ]).result
        if result_peso is not False:
            ExportXLS.setOutCell(sheet, 5, 29, result_peso)

        result_altura = self.criterion_ids.search([
            ('lab_test_result_id', '=', self.lab_test_result_id.id),
            ('code', '=', 'EAN21_02_03'),
        ]).result
        if result_altura is not False:
            ExportXLS.setOutCell(sheet, 18, 29, result_altura)

        ExportXLS.setOutCell(sheet, 33, 57, self.employee_id.name)
        ExportXLS.setOutCell(sheet, 36, 58, self.employee_id.professional_id)

        save_book = True

        if save_book:

            wbook.save(file_path)

            self.directory_id = file_system_directory.id
            self.file_name = file_name
            self.stored_file_name = file_name

        return True
