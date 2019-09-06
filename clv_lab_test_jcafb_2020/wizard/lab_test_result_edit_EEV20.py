# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestResultEdit(models.TransientModel):
    _inherit = 'clv.lab_test.result.edit'

    #
    # EEV20
    #

    def _default_is_EEV20(self):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EEV20':
            is_EEV20 = True
        else:
            is_EEV20 = False
        return is_EEV20
    is_EEV20 = fields.Boolean('Is EEV20', readonly=True, default=_default_is_EEV20)

    def _default_EEV20_data_entrada_material(self):
        return self._get_default('EEV20', 'EEV20-01-01')
    EEV20_data_entrada_material = fields.Date(
        'Data de Entrada do Material', readonly=False, default=_default_EEV20_data_entrada_material
    )

    def _write_EEV20_data_entrada_material(self):
        self._set_result('EEV20', 'EEV20-01-01', self.EEV20_data_entrada_material)

    def _default_EEV20_liberacao_resultado(self):
        return self._get_default('EEV20', 'EEV20-01-02')
    EEV20_liberacao_resultado = fields.Date(
        'Liberação do Resultado', readonly=False, default=_default_EEV20_liberacao_resultado
    )

    def _write_EEV20_liberacao_resultado(self):
        self._set_result('EEV20', 'EEV20-01-02', self.EEV20_liberacao_resultado)

    def _default_EEV20_resultado(self):
        return self._get_default('EEV20', 'EEV20-01-03')
    EEV20_resultado = fields.Selection([
        ('POSITIVO', 'POSITIVO'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não realizado', 'Não realizado'),
    ], 'Resultado', readonly=False, default=_default_EEV20_resultado)

    def _write_EEV20_resultado(self):
        self._set_result('EEV20', 'EEV20-01-03', self.EEV20_resultado)

    def _default_EEV20_examinador(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EEV20', 'EEV20-01-04')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EEV20_examinador = fields.Many2one(
        'hr.employee',
        string='Examinador',
        readonly=False,
        default=_default_EEV20_examinador
    )

    def _write_EEV20_examinador(self):
        self._set_result(
            'EEV20', 'EEV20-01-04',
            self.EEV20_examinador.name + ' [' + self.EEV20_examinador.code + ']'
        )

    def _default_EEV20_metodo_utilizado(self):
        return self._get_default('EEV20', 'EEV20-01-05')
    EEV20_metodo_utilizado = fields.Selection([
        ('Swab anal', 'Swab anal'),
        ('Outro', 'Outro'),
    ], 'Método utilizado', readonly=False, default=_default_EEV20_metodo_utilizado)

    def _write_EEV20_metodo_utilizado(self):
        self._set_result('EEV20', 'EEV20-01-05', self.EEV20_metodo_utilizado)

    def _default_EEV20_obs(self):
        return self._get_default('EEV20', 'EEV20-01-06')
    EEV20_obs = fields.Char(
        'Observações', readonly=False, default=_default_EEV20_obs
    )

    def _write_EEV20_obs(self):
        self._set_result('EEV20', 'EEV20-01-06', self.EEV20_obs)

    def _do_result_updt_EEV20(self):

        self._write_EEV20_data_entrada_material()
        self._write_EEV20_liberacao_resultado()
        self._write_EEV20_resultado()
        self._write_EEV20_examinador()
        self._write_EEV20_metodo_utilizado()
        self._write_EEV20_obs()

        return True
