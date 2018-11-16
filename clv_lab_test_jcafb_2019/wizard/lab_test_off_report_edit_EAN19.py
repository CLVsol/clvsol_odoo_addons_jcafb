# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestOffReportEdit(models.TransientModel):
    _inherit = 'clv.lab_test.off.report.edit'

    #
    # EAN19
    #

    def _default_is_EAN19(self):
        active_id = self.env['clv.lab_test.off.report'].browse(self._context.get('active_id'))
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

    def _default_EAN19_altura(self):
        return self._get_default('EAN19', 'EAN19-01-03')
    EAN19_altura = fields.Char(
        'Altura', readonly=False, default=_default_EAN19_altura
    )

    def _write_EAN19_altura(self):
        self._set_result('EAN19', 'EAN19-01-03', self.EAN19_altura)

    def _default_EAN19_circ_abdominal(self):
        return self._get_default('EAN19', 'EAN19-01-05')
    EAN19_circ_abdominal = fields.Char(
        'Circunferência abdominal', readonly=False, default=_default_EAN19_circ_abdominal
    )

    def _write_EAN19_circ_abdominal(self):
        self._set_result('EAN19', 'EAN19-01-05', self.EAN19_circ_abdominal)

    def _default_EAN19_hemoglobina_valor(self):
        return self._get_default('EAN19', 'EAN19-02-03')
    EAN19_hemoglobina_valor = fields.Char(
        'Valor da Hemoglobina', readonly=False, default=_default_EAN19_hemoglobina_valor
    )

    def _write_EAN19_hemoglobina_valor(self):
        self._set_result('EAN19', 'EAN19-02-03', self.EAN19_hemoglobina_valor)

    def _default_EAN19_hemoglobina_interpretacao(self):
        return self._get_default('EAN19', 'EAN19-02-05')
    EAN19_hemoglobina_interpretacao = fields.Selection([
        ('a) Normal', 'a) Normal'),
        ('b) Abaixo do normal (anemia)', 'b) Abaixo do normal (anemia)'),
        ('c) Acima do normal', 'c) Acima do normal'),
    ], 'Interpretação do Reportado de Hemoglobina', readonly=False, default=_default_EAN19_hemoglobina_interpretacao)

    def _write_EAN19_hemoglobina_interpretacao(self):
        self._set_result('EAN19', 'EAN19-02-05', self.EAN19_hemoglobina_interpretacao)

    def _default_EAN19_obs(self):
        return self._get_default('EAN19', 'EAN19-02-06')
    EAN19_obs = fields.Char(
        'Observações', readonly=False, default=_default_EAN19_obs
    )

    def _write_EAN19_obs(self):
        self._set_result('EAN19', 'EAN19-02-06', self.EAN19_obs)

    def _do_report_updt_EAN19(self):

        self._write_EAN19_peso()
        self._write_EAN19_altura()
        self._write_EAN19_circ_abdominal()
        self._write_EAN19_hemoglobina_valor()
        self._write_EAN19_hemoglobina_interpretacao()
        self._write_EAN19_obs()

        return True
