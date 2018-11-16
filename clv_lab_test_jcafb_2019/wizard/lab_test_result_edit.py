# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class LabTestResultEdit(models.TransientModel):
    _inherit = 'clv.lab_test.result.edit'

    @api.multi
    def do_result_updt(self):
        self.ensure_one()

        super(LabTestResultEdit, self).do_result_updt()

        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))

        if active_id.lab_test_type_id.code == 'EAN17':
            self._do_result_updt_EAN17()

        if active_id.lab_test_type_id.code == 'EDH17':
            self._do_result_updt_EDH17()

        if active_id.lab_test_type_id.code == 'ECP17':
            self._do_result_updt_ECP17()

        if active_id.lab_test_type_id.code == 'EEV17':
            self._do_result_updt_EEV17()

        if active_id.lab_test_type_id.code == 'EUR17':
            self._do_result_updt_EUR17()

        if active_id.lab_test_type_id.code == 'EAN18':
            self._do_result_updt_EAN18()

        if active_id.lab_test_type_id.code == 'EDH18':
            self._do_result_updt_EDH18()

        if active_id.lab_test_type_id.code == 'ECP18':
            self._do_result_updt_ECP18()

        if active_id.lab_test_type_id.code == 'EEV18':
            self._do_result_updt_EEV18()

        if active_id.lab_test_type_id.code == 'EUR18':
            self._do_result_updt_EUR18()

        if active_id.lab_test_type_id.code == 'EAN19':
            self._do_result_updt_EAN19()

        if active_id.lab_test_type_id.code == 'EDH19':
            self._do_result_updt_EDH19()

        if active_id.lab_test_type_id.code == 'ECP19':
            self._do_result_updt_ECP19()

        if active_id.lab_test_type_id.code == 'EEV19':
            self._do_result_updt_EEV19()

        if active_id.lab_test_type_id.code == 'EUR19':
            self._do_result_updt_EUR19()

        return True
