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

from odoo import api, models

_logger = logging.getLogger(__name__)


class LabTestResultCopyToReport(models.TransientModel):
    _inherit = 'clv.lab_test.result.copy_to_report'

    @api.multi
    def do_result_copy_to_report(self):
        self.ensure_one()

        super(LabTestResultCopyToReport, self).do_result_copy_to_report()

        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))

        if active_id.lab_test_type_id.code == 'EAN18':
            self._do_result_copy_to_report_EAN18()

        if active_id.lab_test_type_id.code == 'EDH18':
            self._do_result_copy_to_report_EDH18()

        if active_id.lab_test_type_id.code == 'ECP18':
            self._do_result_copy_to_report_ECP18()

        if active_id.lab_test_type_id.code == 'EEV18':
            self._do_result_copy_to_report_EEV18()

        if active_id.lab_test_type_id.code == 'EUR18':
            self._do_result_copy_to_report_EUR18()

        return True
