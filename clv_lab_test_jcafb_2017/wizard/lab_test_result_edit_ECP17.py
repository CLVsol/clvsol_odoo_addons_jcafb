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
    # ECP17
    #

    def _default_is_ECP17(self):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'ECP17':
            is_ECP17 = True
        else:
            is_ECP17 = False
        return is_ECP17
    is_ECP17 = fields.Boolean('Is ECP17', readonly=True, default=_default_is_ECP17)

    def _default_ECP17_data_entrada_material(self):
        return self._get_default('ECP17', 'ECP17-01-01')
    ECP17_data_entrada_material = fields.Date(
        'Data de Entrada do Material', readonly=False, default=_default_ECP17_data_entrada_material
    )

    def _write_ECP17_data_entrada_material(self):
        self._set_result('ECP17', 'ECP17-01-01', self.ECP17_data_entrada_material)

    def _default_ECP17_liberacao_resultado(self):
        return self._get_default('ECP17', 'ECP17-01-02')
    ECP17_liberacao_resultado = fields.Date(
        'Liberação do Resultado', readonly=False, default=_default_ECP17_liberacao_resultado
    )

    def _write_ECP17_liberacao_resultado(self):
        self._set_result('ECP17', 'ECP17-01-02', self.ECP17_liberacao_resultado)

    def _default_ECP17_resultado(self):
        return self._get_default('ECP17', 'ECP17-01-03')
    ECP17_resultado = fields.Selection([
        ('Positivo', 'Positivo'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não Realizado', 'Não Realizado'),
    ], 'Resultado', readonly=False, default=_default_ECP17_resultado)

    def _write_ECP17_resultado(self):
        self._set_result('ECP17', 'ECP17-01-03', self.ECP17_resultado)

    def _default_ECP17_obs(self):
        return self._get_default('ECP17', 'ECP17-01-04')
    ECP17_obs = fields.Char(
        'Observações', readonly=False, default=_default_ECP17_obs
    )

    def _write_ECP17_obs(self):
        self._set_result('ECP17', 'ECP17-01-04', self.ECP17_obs)

    def _default_ECP17_metodo_utilizado(self):
        return self._get_default('ECP17', 'ECP17-01-05')
    ECP17_metodo_utilizado = fields.Selection([
        ('Ritchie', 'Ritchie'),
        ('Hoffmann', 'Hoffmann'),
        ('Ritchie e Hoffmann', 'Ritchie e Hoffmann'),
    ], 'Medtodologia(s) Empregada(s)', readonly=False, default=_default_ECP17_metodo_utilizado)

    def _write_ECP17_metodo_utilizado(self):
        self._set_result('ECP17', 'ECP17-01-05', self.ECP17_metodo_utilizado)

    def _default_ECP17_ritchie_resultado(self):
        return self._get_default('ECP17', 'ECP17-02-01')
    ECP17_ritchie_resultado = fields.Selection([
        ('Não Realizado', 'Não Realizado'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Cistos de Endolimax nana', 'Cistos de Endolimax nana'),
        ('Cistos de Entamoeba coli', 'Cistos de Entamoeba coli'),
        ('Cistos de Entamoeba histolytica', 'Cistos de Entamoeba histolytica'),
        ('Cistos de Giardia lamblia', 'Cistos de Giardia lamblia'),
        ('Cistos de Iodamoeba butschlii', 'Cistos de Iodamoeba butschlii'),
        ('Cistos de Chilomastix mesnil', 'Cistos de Chilomastix mesnil'),
        ('Oocistos de Isospora belli', 'Oocistos de Isospora belli'),
        ('Ovos de Ascaris lumbricoides', 'Ovos de Ascaris lumbricoides'),
        ('Ovos de Ancilostomídeo', 'Ovos de Ancilostomídeo'),
        ('Ovos de Trichuris trichiura', 'Ovos de Trichuris trichiura'),
        ('Ovos de Taenia sp', 'Ovos de Taenia sp'),
        ('Ovos de Hymenolepis nana', 'Ovos de Hymenolepis nana'),
        ('Ovos de Schistosoma mansoni', 'Ovos de Schistosoma mansoni'),
        ('Ovos de Enterobius vermicularis', 'Ovos de Enterobius vermicularis'),
        ('Larvas de Strongyloides stercoralis', 'Larvas de Strongyloides stercoralis'),
        ('Outro', 'Outro'),
    ], 'Resultado', readonly=False, default=_default_ECP17_ritchie_resultado)

    def _write_ECP17_ritchie_resultado(self):
        self._set_result('ECP17', 'ECP17-02-01', self.ECP17_ritchie_resultado)

    def _do_result_updt_ECP17(self):

        self._write_ECP17_data_entrada_material()
        self._write_ECP17_liberacao_resultado()
        self._write_ECP17_resultado()
        self._write_ECP17_obs()
        self._write_ECP17_metodo_utilizado()
        self._write_ECP17_ritchie_resultado()

        return True
