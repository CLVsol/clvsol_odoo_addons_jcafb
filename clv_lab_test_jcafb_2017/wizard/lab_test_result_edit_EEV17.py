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
    # EEV17
    #

    def _default_is_EEV17(self):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EEV17':
            is_EEV17 = True
        else:
            is_EEV17 = False
        return is_EEV17
    is_EEV17 = fields.Boolean('Is EEV17', readonly=True, default=_default_is_EEV17)

    def _default_EEV17_data_entrada_material(self):
        return self._get_default('EEV17', 'EEV17-01-01')
    EEV17_data_entrada_material = fields.Date(
        'Data de Entrada do Material', readonly=False, default=_default_EEV17_data_entrada_material
    )

    def _write_EEV17_data_entrada_material(self):
        self._set_result('EEV17', 'EEV17-01-01', self.EEV17_data_entrada_material)

    def _default_EEV17_liberacao_resultado(self):
        return self._get_default('EEV17', 'EEV17-01-02')
    EEV17_liberacao_resultado = fields.Date(
        'Liberação do Resultado', readonly=False, default=_default_EEV17_liberacao_resultado
    )

    def _write_EEV17_liberacao_resultado(self):
        self._set_result('EEV17', 'EEV17-01-02', self.EEV17_liberacao_resultado)

    def _default_EEV17_resultado(self):
        return self._get_default('EEV17', 'EEV17-01-03')
    EEV17_resultado = fields.Selection([
        ('Positivo', 'Positivo'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não Realizado', 'Não Realizado'),
    ], 'Resultado', readonly=False, default=_default_EEV17_resultado)

    def _write_EEV17_resultado(self):
        self._set_result('EEV17', 'EEV17-01-03', self.EEV17_resultado)

    def _default_EEV17_examinador(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EEV17', 'EEV17-01-04')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EEV17_examinador = fields.Many2one(
        'hr.employee',
        string='Examinador',
        readonly=False,
        default=_default_EEV17_examinador
    )

    def _write_EEV17_examinador(self):
        self._set_result(
            'EEV17', 'EEV17-01-04',
            self.EEV17_examinador.name + ' [' + self.EEV17_examinador.code + ']'
        )

    def _default_EEV17_metodo_utilizado(self):
        return self._get_default('EEV17', 'EEV17-01-05')
    EEV17_metodo_utilizado = fields.Selection([
        ('Swab anal', 'Swab anal'),
        ('Outro', 'Outro'),
    ], 'Método utilizado', readonly=False, default=_default_EEV17_metodo_utilizado)

    def _write_EEV17_metodo_utilizado(self):
        self._set_result('EEV17', 'EEV17-01-05', self.EEV17_metodo_utilizado)

    def _default_EEV17_obs(self):
        return self._get_default('EEV17', 'EEV17-01-06')
    EEV17_obs = fields.Char(
        'Observações', readonly=False, default=_default_EEV17_obs
    )

    def _write_EEV17_obs(self):
        self._set_result('EEV17', 'EEV17-01-06', self.EEV17_obs)

    def _do_result_updt_EEV17(self):

        self._write_EEV17_data_entrada_material()
        self._write_EEV17_liberacao_resultado()
        self._write_EEV17_resultado()
        self._write_EEV17_examinador()
        self._write_EEV17_metodo_utilizado()
        self._write_EEV17_obs()

        return True
