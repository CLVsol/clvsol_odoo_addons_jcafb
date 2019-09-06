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

        if active_id.lab_test_type_id.code == 'EAN20':
            self._do_report_updt_EAN20()

        if active_id.lab_test_type_id.code == 'EDH20':
            self._do_report_updt_EDH20()

        if active_id.lab_test_type_id.code == 'ECP20':
            self._do_report_updt_ECP20()

        if active_id.lab_test_type_id.code == 'EEV20':
            self._do_report_updt_EEV20()

        if active_id.lab_test_type_id.code == 'EUR20':
            self._do_report_updt_EUR20()

        return True
