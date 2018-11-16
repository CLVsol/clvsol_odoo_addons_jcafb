# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestResultEdit(models.TransientModel):
    _inherit = 'clv.lab_test.result.edit'

    #
    # EAN19
    #

    def _default_is_EAN19(self):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EAN19':
            is_EAN19 = True
        else:
            is_EAN19 = False
        return is_EAN19
    is_EAN19 = fields.Boolean('Is EAN19', readonly=True, default=_default_is_EAN19)

    def _default_EAN19_peso(self):
        return self._get_default('EAN19', 'EAN19-01-01')
    EAN19_peso = fields.Char(
        'Peso', readonly=False, default=_default_EAN19_peso
    )

    def _write_EAN19_peso(self):
        self._set_result('EAN19', 'EAN19-01-01', self.EAN19_peso)

    def _default_EAN19_peso_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EAN19', 'EAN19-01-02')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EAN19_peso_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida do Peso',
        readonly=False,
        default=_default_EAN19_peso_resp
    )

    def _write_EAN19_peso_resp(self):
        if self.EAN19_peso_resp.name is not False:
            self._set_result(
                'EAN19', 'EAN19-01-02', self.EAN19_peso_resp.name + ' [' + self.EAN19_peso_resp.code + ']'
            )
        else:
            self._set_result('EAN19', 'EAN19-01-02', False)

    def _default_EAN19_altura(self):
        return self._get_default('EAN19', 'EAN19-01-03')
    EAN19_altura = fields.Char(
        'Altura', readonly=False, default=_default_EAN19_altura
    )

    def _write_EAN19_altura(self):
        self._set_result('EAN19', 'EAN19-01-03', self.EAN19_altura)

    def _default_EAN19_altura_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EAN19', 'EAN19-01-04')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EAN19_altura_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida da Altura',
        readonly=False,
        default=_default_EAN19_altura_resp
    )

    def _write_EAN19_altura_resp(self):
        if self.EAN19_altura_resp.name is not False:
            self._set_result(
                'EAN19', 'EAN19-01-04', self.EAN19_altura_resp.name + ' [' + self.EAN19_altura_resp.code + ']'
            )
        else:
            self._set_result('EAN19', 'EAN19-01-04', False)

    def _default_EAN19_hemoglobina_coleta_horario(self):
        return self._get_default('EAN19', 'EAN19-02-01')
    EAN19_hemoglobina_coleta_horario = fields.Datetime(
        'Horário da coleta', readonly=False, default=_default_EAN19_hemoglobina_coleta_horario
    )

    def _write_EAN19_hemoglobina_coleta_horario(self):
        self._set_result('EAN19', 'EAN19-02-01', self.EAN19_hemoglobina_coleta_horario)

    def _default_EAN19_hemoglobina_coleta_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EAN19', 'EAN19-02-02')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EAN19_hemoglobina_coleta_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela coleta',
        readonly=False,
        default=_default_EAN19_hemoglobina_coleta_resp
    )

    def _write_EAN19_hemoglobina_coleta_resp(self):
        if self.EAN19_hemoglobina_coleta_resp.name is not False:
            self._set_result(
                'EAN19', 'EAN19-02-02',
                self.EAN19_hemoglobina_coleta_resp.name + ' [' + self.EAN19_hemoglobina_coleta_resp.code + ']'
            )
        else:
            self._set_result('EAN19', 'EAN19-02-02', False)

    def _default_EAN19_hemoglobina_valor(self):
        return self._get_default('EAN19', 'EAN19-02-03')
    EAN19_hemoglobina_valor = fields.Char(
        'Valor da Hemoglobina', readonly=False, default=_default_EAN19_hemoglobina_valor
    )

    def _write_EAN19_hemoglobina_valor(self):
        self._set_result('EAN19', 'EAN19-02-03', self.EAN19_hemoglobina_valor)

    def _default_EAN19_hemoglobina_valor_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EAN19', 'EAN19-02-04')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EAN19_hemoglobina_valor_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela dosagem',
        readonly=False,
        default=_default_EAN19_hemoglobina_valor_resp
    )

    def _write_EAN19_hemoglobina_valor_resp(self):
        _logger.info(u'%s %s', '>>>>>>>>>>', self.EAN19_hemoglobina_valor_resp.name)
        if self.EAN19_hemoglobina_valor_resp.name is not False:
            self._set_result(
                'EAN19', 'EAN19-02-04',
                self.EAN19_hemoglobina_valor_resp.name + ' [' + self.EAN19_hemoglobina_valor_resp.code + ']'
            )
        else:
            self._set_result('EAN19', 'EAN19-02-04', False)

    def _default_EAN19_hemoglobina_interpretacao(self):
        return self._get_default('EAN19', 'EAN19-02-05')
    EAN19_hemoglobina_interpretacao = fields.Selection([
        ('a) Normal', 'a) Normal'),
        ('b) Abaixo do normal (anemia)', 'b) Abaixo do normal (anemia)'),
        ('c) Acima do normal', 'c) Acima do normal'),
    ], 'Interpretação do Resultado de Hemoglobina', readonly=False, default=_default_EAN19_hemoglobina_interpretacao)

    def _write_EAN19_hemoglobina_interpretacao(self):
        self._set_result('EAN19', 'EAN19-02-05', self.EAN19_hemoglobina_interpretacao)

    def _default_EAN19_obs(self):
        return self._get_default('EAN19', 'EAN19-02-06')
    EAN19_obs = fields.Char(
        'Observações', readonly=False, default=_default_EAN19_obs
    )

    def _write_EAN19_obs(self):
        self._set_result('EAN19', 'EAN19-02-06', self.EAN19_obs)

    def _do_result_updt_EAN19(self):

        self._write_EAN19_peso()
        self._write_EAN19_peso_resp()
        self._write_EAN19_altura()
        self._write_EAN19_altura_resp()
        self._write_EAN19_hemoglobina_coleta_horario()
        self._write_EAN19_hemoglobina_coleta_resp()
        self._write_EAN19_hemoglobina_valor()
        self._write_EAN19_hemoglobina_valor_resp()
        self._write_EAN19_hemoglobina_interpretacao()
        self._write_EAN19_obs()

        return True
