# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
# import xlwt

from odoo import models

_logger = logging.getLogger(__name__)


class LabTestReport(models.Model):
    _name = "clv.lab_test.report"
    _inherit = 'clv.lab_test.report'

    def lab_test_report_export_xls_EAN19(self, sheet, row_nr):

        lab_test_type = self.lab_test_type_id.code
        lab_test_request_code = self.lab_test_request_id.code

        row_nr += 1
        row = sheet.row(row_nr)
        # row.write(0, 'Person:')
        # row.write(3, self.person_id.name)
        row.write(3, self.ref_id.name)
        row_nr += 1
        row = sheet.row(row_nr)
        row.write(0, 'Lab Test Type:')
        row.write(3, lab_test_type)
        row_nr += 1
        row = sheet.row(row_nr)
        row.write(0, 'Request Code:')
        row.write(3, lab_test_request_code)
        row_nr += 1

        return True
