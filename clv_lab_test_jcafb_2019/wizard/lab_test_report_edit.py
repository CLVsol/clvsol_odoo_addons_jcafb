# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class LabTestReportEdit(models.TransientModel):
    _inherit = 'clv.lab_test.report.edit'

    @api.multi
    def do_report_updt(self):
        self.ensure_one()

        super(LabTestReportEdit, self).do_report_updt()

        active_id = self.env['clv.lab_test.report'].browse(self._context.get('active_id'))

        if active_id.lab_test_type_id.code == 'EAN19':
            self._do_report_updt_EAN19()

        if active_id.lab_test_type_id.code == 'EDH19':
            self._do_report_updt_EDH19()

        if active_id.lab_test_type_id.code == 'ECP19':
            self._do_report_updt_ECP19()

        if active_id.lab_test_type_id.code == 'EEV19':
            self._do_report_updt_EEV19()

        if active_id.lab_test_type_id.code == 'EUR19':
            self._do_report_updt_EUR19()

        return True
