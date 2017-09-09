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

        return True
