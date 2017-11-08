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

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestReportEdit(models.TransientModel):
    _inherit = 'clv.lab_test.report.edit'

    #
    # EEV18
    #

    def _default_is_EEV18(self):
        active_id = self.env['clv.lab_test.report'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EEV18':
            is_EEV18 = True
        else:
            is_EEV18 = False
        return is_EEV18
    is_EEV18 = fields.Boolean('Is EEV18', readonly=True, default=_default_is_EEV18)

    def _default_EEV18_resultado(self):
        return self._get_default('EEV18', 'EEV18-01-03')
    EEV18_resultado = fields.Selection([
        ('Positivo', 'Positivo'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não Realizado', 'Não Realizado'),
    ], 'Resultado', readonly=False, default=_default_EEV18_resultado)

    def _write_EEV18_resultado(self):
        self._set_result('EEV18', 'EEV18-01-03', self.EEV18_resultado)

    def _default_EEV18_metodo_utilizado(self):
        return self._get_default('EEV18', 'EEV18-01-05')
    EEV18_metodo_utilizado = fields.Selection([
        ('Swab anal', 'Swab anal'),
        ('Outro', 'Outro'),
    ], 'Método utilizado', readonly=False, default=_default_EEV18_metodo_utilizado)

    def _write_EEV18_metodo_utilizado(self):
        self._set_result('EEV18', 'EEV18-01-05', self.EEV18_metodo_utilizado)

    def _default_EEV18_obs(self):
        return self._get_default('EEV18', 'EEV18-01-06')
    EEV18_obs = fields.Char(
        'Observações', readonly=False, default=_default_EEV18_obs
    )

    def _write_EEV18_obs(self):
        self._set_result('EEV18', 'EEV18-01-06', self.EEV18_obs)

    def _do_report_updt_EEV18(self):

        self._write_EEV18_resultado()
        self._write_EEV18_metodo_utilizado()
        self._write_EEV18_obs()

        return True
