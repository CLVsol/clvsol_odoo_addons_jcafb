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
# import xlwt

from odoo import models

_logger = logging.getLogger(__name__)


class LabTestResult(models.Model):
    _name = "clv.lab_test.result"
    _inherit = 'clv.lab_test.result'

    def lab_test_result_export_xls_ECP18(self, sheet, row_nr):

        lab_test_type = self.lab_test_type_id.code
        lab_test_request_code = self.lab_test_request_id.code

        row_nr += 1
        row = sheet.row(row_nr)
        row.write(0, 'Person:')
        row.write(3, self.person_id.name)
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
