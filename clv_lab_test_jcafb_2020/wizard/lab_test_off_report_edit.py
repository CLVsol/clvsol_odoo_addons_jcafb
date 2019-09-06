# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class LabTestOffReportEdit(models.TransientModel):
    _inherit = 'clv.lab_test.off.report.edit'

    @api.multi
    def do_report_updt(self):
        self.ensure_one()

        super(LabTestOffReportEdit, self).do_report_updt()

        active_id = self.env['clv.lab_test.off.report'].browse(self._context.get('active_id'))

        if active_id.lab_test_type_id.code == 'EAN20':
            self._do_report_updt_EAN20()

        if active_id.lab_test_type_id.code == 'EDH20':
            self._do_report_updt_EDH20()

        return True
