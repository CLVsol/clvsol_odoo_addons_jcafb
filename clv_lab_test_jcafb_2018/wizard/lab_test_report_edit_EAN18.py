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
    # EAN18
    #

    def _default_is_EAN18(self):
        active_id = self.env['clv.lab_test.report'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EAN18':
            is_EAN18 = True
        else:
            is_EAN18 = False
        return is_EAN18
    is_EAN18 = fields.Boolean('Is EAN18', readonly=True, default=_default_is_EAN18)

    def _default_EAN18_peso(self):
        return self._get_default('EAN18', 'EAN18-01-01')
    EAN18_peso = fields.Char(
        'Peso', readonly=False, default=_default_EAN18_peso
    )

    def _write_EAN18_peso(self):
        self._set_result('EAN18', 'EAN18-01-01', self.EAN18_peso)

    def _default_EAN18_altura(self):
        return self._get_default('EAN18', 'EAN18-01-03')
    EAN18_altura = fields.Char(
        'Altura', readonly=False, default=_default_EAN18_altura
    )

    def _write_EAN18_altura(self):
        self._set_result('EAN18', 'EAN18-01-03', self.EAN18_altura)

    def _default_EAN18_circ_abdominal(self):
        return self._get_default('EAN18', 'EAN18-01-05')
    EAN18_circ_abdominal = fields.Char(
        'Circunferência abdominal', readonly=False, default=_default_EAN18_circ_abdominal
    )

    def _write_EAN18_circ_abdominal(self):
        self._set_result('EAN18', 'EAN18-01-05', self.EAN18_circ_abdominal)

    def _default_EAN18_hemoglobina_valor(self):
        return self._get_default('EAN18', 'EAN18-02-03')
    EAN18_hemoglobina_valor = fields.Char(
        'Valor da Hemoglobina', readonly=False, default=_default_EAN18_hemoglobina_valor
    )

    def _write_EAN18_hemoglobina_valor(self):
        self._set_result('EAN18', 'EAN18-02-03', self.EAN18_hemoglobina_valor)

    def _default_EAN18_hemoglobina_interpretacao(self):
        return self._get_default('EAN18', 'EAN18-02-05')
    EAN18_hemoglobina_interpretacao = fields.Selection([
        ('a) Normal', 'a) Normal'),
        ('b) Abaixo do normal (anemia)', 'b) Abaixo do normal (anemia)'),
        ('c) Acima do normal', 'c) Acima do normal'),
    ], 'Interpretação do Reportado de Hemoglobina', readonly=False, default=_default_EAN18_hemoglobina_interpretacao)

    def _write_EAN18_hemoglobina_interpretacao(self):
        self._set_result('EAN18', 'EAN18-02-05', self.EAN18_hemoglobina_interpretacao)

    def _default_EAN18_obs(self):
        return self._get_default('EAN18', 'EAN18-02-06')
    EAN18_obs = fields.Char(
        'Observações', readonly=False, default=_default_EAN18_obs
    )

    def _write_EAN18_obs(self):
        self._set_result('EAN18', 'EAN18-02-06', self.EAN18_obs)

    def _do_report_updt_EAN18(self):

        self._write_EAN18_peso()
        self._write_EAN18_altura()
        self._write_EAN18_circ_abdominal()
        self._write_EAN18_hemoglobina_valor()
        self._write_EAN18_hemoglobina_interpretacao()
        self._write_EAN18_obs()

        return True
