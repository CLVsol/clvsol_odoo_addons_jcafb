# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

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

        if active_id.lab_test_type_id.code == 'EAN19':
            self._do_result_copy_to_report_EAN19()

        if active_id.lab_test_type_id.code == 'EDH19':
            self._do_result_copy_to_report_EDH19()

        if active_id.lab_test_type_id.code == 'ECP19':
            self._do_result_copy_to_report_ECP19()

        if active_id.lab_test_type_id.code == 'EEV19':
            self._do_result_copy_to_report_EEV19()

        if active_id.lab_test_type_id.code == 'EUR19':
            self._do_result_copy_to_report_EUR19()

        return True
