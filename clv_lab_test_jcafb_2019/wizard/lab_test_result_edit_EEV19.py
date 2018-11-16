# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestResultEdit(models.TransientModel):
    _inherit = 'clv.lab_test.result.edit'

    #
    # EEV19
    #

    def _default_is_EEV19(self):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EEV19':
            is_EEV19 = True
        else:
            is_EEV19 = False
        return is_EEV19
    is_EEV19 = fields.Boolean('Is EEV19', readonly=True, default=_default_is_EEV19)

    def _default_EEV19_data_entrada_material(self):
        return self._get_default('EEV19', 'EEV19-01-01')
    EEV19_data_entrada_material = fields.Date(
        'Data de Entrada do Material', readonly=False, default=_default_EEV19_data_entrada_material
    )

    def _write_EEV19_data_entrada_material(self):
        self._set_result('EEV19', 'EEV19-01-01', self.EEV19_data_entrada_material)

    def _default_EEV19_liberacao_resultado(self):
        return self._get_default('EEV19', 'EEV19-01-02')
    EEV19_liberacao_resultado = fields.Date(
        'Liberação do Resultado', readonly=False, default=_default_EEV19_liberacao_resultado
    )

    def _write_EEV19_liberacao_resultado(self):
        self._set_result('EEV19', 'EEV19-01-02', self.EEV19_liberacao_resultado)

    def _default_EEV19_resultado(self):
        return self._get_default('EEV19', 'EEV19-01-03')
    EEV19_resultado = fields.Selection([
        ('POSITIVO', 'POSITIVO'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não realizado', 'Não realizado'),
    ], 'Resultado', readonly=False, default=_default_EEV19_resultado)

    def _write_EEV19_resultado(self):
        self._set_result('EEV19', 'EEV19-01-03', self.EEV19_resultado)

    def _default_EEV19_examinador(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EEV19', 'EEV19-01-04')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EEV19_examinador = fields.Many2one(
        'hr.employee',
        string='Examinador',
        readonly=False,
        default=_default_EEV19_examinador
    )

    def _write_EEV19_examinador(self):
        self._set_result(
            'EEV19', 'EEV19-01-04',
            self.EEV19_examinador.name + ' [' + self.EEV19_examinador.code + ']'
        )

    def _default_EEV19_metodo_utilizado(self):
        return self._get_default('EEV19', 'EEV19-01-05')
    EEV19_metodo_utilizado = fields.Selection([
        ('Swab anal', 'Swab anal'),
        ('Outro', 'Outro'),
    ], 'Método utilizado', readonly=False, default=_default_EEV19_metodo_utilizado)

    def _write_EEV19_metodo_utilizado(self):
        self._set_result('EEV19', 'EEV19-01-05', self.EEV19_metodo_utilizado)

    def _default_EEV19_obs(self):
        return self._get_default('EEV19', 'EEV19-01-06')
    EEV19_obs = fields.Char(
        'Observações', readonly=False, default=_default_EEV19_obs
    )

    def _write_EEV19_obs(self):
        self._set_result('EEV19', 'EEV19-01-06', self.EEV19_obs)

    def _do_result_updt_EEV19(self):

        self._write_EEV19_data_entrada_material()
        self._write_EEV19_liberacao_resultado()
        self._write_EEV19_resultado()
        self._write_EEV19_examinador()
        self._write_EEV19_metodo_utilizado()
        self._write_EEV19_obs()

        return True
