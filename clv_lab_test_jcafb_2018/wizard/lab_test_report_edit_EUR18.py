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
    # EUR18
    #

    def _default_is_EUR18(self):
        active_id = self.env['clv.lab_test.report'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EUR18':
            is_EUR18 = True
        else:
            is_EUR18 = False
        return is_EUR18
    is_EUR18 = fields.Boolean('Is EUR18', readonly=True, default=_default_is_EUR18)

    def _default_EUR18_data_entrada_material(self):
        return self._get_default('EUR18', 'EUR18-01-01')
    EUR18_data_entrada_material = fields.Date(
        'Data de Entrada do Material', readonly=False, default=_default_EUR18_data_entrada_material
    )

    def _write_EUR18_data_entrada_material(self):
        self._set_result('EUR18', 'EUR18-01-01', self.EUR18_data_entrada_material)

    def _default_EUR18_liberacao_reportado(self):
        return self._get_default('EUR18', 'EUR18-01-02')
    EUR18_liberacao_reportado = fields.Date(
        'Liberação do Reportado', readonly=False, default=_default_EUR18_liberacao_reportado
    )

    def _write_EUR18_liberacao_reportado(self):
        self._set_result('EUR18', 'EUR18-01-02', self.EUR18_liberacao_reportado)

    def _default_EUR18_examinador(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EUR18', 'EUR18-01-03')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EUR18_examinador = fields.Many2one(
        'hr.employee',
        string='Examinador',
        readonly=False,
        default=_default_EUR18_examinador
    )

    def _write_EUR18_examinador(self):
        self._set_result(
            'EUR18', 'EUR18-01-03',
            self.EUR18_examinador.name + ' [' + self.EUR18_examinador.code + ']'
        )

    def _default_EUR18_volume(self):
        return self._get_default('EUR18', 'EUR18-02-01')
    EUR18_volume = fields.Char(
        'Volume', readonly=False, default=_default_EUR18_volume
    )

    def _write_EUR18_volume(self):
        self._set_result('EUR18', 'EUR18-02-01', self.EUR18_volume)

    def _do_report_updt_EUR18(self):

        self._write_EUR18_data_entrada_material()
        self._write_EUR18_liberacao_reportado()
        self._write_EUR18_examinador()
        self._write_EUR18_volume()

        return True
