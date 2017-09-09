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


class LabTestResultEdit(models.TransientModel):
    _inherit = 'clv.lab_test.result.edit'

    #
    # EUR17
    #

    def _default_is_EUR17(self):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EUR17':
            is_EUR17 = True
        else:
            is_EUR17 = False
        return is_EUR17
    is_EUR17 = fields.Boolean('Is EUR17', readonly=True, default=_default_is_EUR17)

    def _default_EUR17_data_entrada_material(self):
        return self._get_default('EUR17', 'EUR17-01-01')
    EUR17_data_entrada_material = fields.Date(
        'Data de Entrada do Material', readonly=False, default=_default_EUR17_data_entrada_material
    )

    def _write_EUR17_data_entrada_material(self):
        self._set_result('EUR17', 'EUR17-01-01', self.EUR17_data_entrada_material)

    def _default_EUR17_liberacao_resultado(self):
        return self._get_default('EUR17', 'EUR17-01-02')
    EUR17_liberacao_resultado = fields.Date(
        'Liberação do Resultado', readonly=False, default=_default_EUR17_liberacao_resultado
    )

    def _write_EUR17_liberacao_resultado(self):
        self._set_result('EUR17', 'EUR17-01-02', self.EUR17_liberacao_resultado)

    def _default_EUR17_examinador(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EUR17', 'EUR17-01-03')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EUR17_examinador = fields.Many2one(
        'hr.employee',
        string='Examinador',
        readonly=False,
        default=_default_EUR17_examinador
    )

    def _write_EUR17_examinador(self):
        self._set_result(
            'EUR17', 'EUR17-01-03',
            self.EUR17_examinador.name + ' [' + self.EUR17_examinador.code + ']'
        )

    def _default_EUR17_volume(self):
        return self._get_default('EUR17', 'EUR17-02-01')
    EUR17_volume = fields.Char(
        'Volume', readonly=False, default=_default_EUR17_volume
    )

    def _write_EUR17_volume(self):
        self._set_result('EUR17', 'EUR17-02-01', self.EUR17_volume)

    def _do_result_updt_EUR17(self):

        self._write_EUR17_data_entrada_material()
        self._write_EUR17_liberacao_resultado()
        self._write_EUR17_examinador()
        self._write_EUR17_volume()

        return True
