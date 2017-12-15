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

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class LabTestResultCopyToReport(models.TransientModel):
    _inherit = 'clv.lab_test.result.copy_to_report'

    #
    # ECP18
    #

    def _default_is_ECP18(self):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'ECP18':
            is_ECP18 = True
        else:
            is_ECP18 = False
        return is_ECP18
    is_ECP18 = fields.Boolean('Is ECP18', readonly=True, default=_default_is_ECP18)

    def _default_ECP18_metodos_utilizados(self):
        return self._get_default('ECP18', 'ECP18-05-03')
    # ECP18_metodos_utilizados = fields.Selection([
    #     ('Ritchie', 'Ritchie'),
    #     ('Hoffmann', 'Hoffmann'),
    #     ('Willis', 'Willis'),
    #     ('Ritchie, Hoffmann', 'Ritchie, Hoffmann'),
    #     ('Ritchie, Hoffmann, Willis', 'Ritchie, Hoffmann, Willis'),
    # ], 'Metodologia(s) Empregada(s)', readonly=False, default=_default_ECP18_metodos_utilizados)
    ECP18_metodos_utilizados = fields.Char(
        string='Metodologia(s) Empregada(s)',
        default=_default_ECP18_metodos_utilizados
    )

    def _write_ECP18_metodos_utilizados(self):
        self._set_result('ECP18', 'ECP18-05-03', self.ECP18_metodos_utilizados)
        self._copy_result('ECP18', 'ECP18-05-03', self.ECP18_metodos_utilizados)

    def _default_ECP18_resultado(self):
        return self._get_default('ECP18', 'ECP18-05-04')
    ECP18_resultado = fields.Selection([
        ('POSITIVO', 'POSITIVO'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não realizado', 'Não realizado'),
    ], 'Resultado', readonly=False, default=_default_ECP18_resultado)

    def _write_ECP18_resultado(self):
        self._set_result('ECP18', 'ECP18-05-04', self.ECP18_resultado)
        self._copy_result('ECP18', 'ECP18-05-04', self.ECP18_resultado)

    def _default_ECP18_parasitas(self):
        return self._get_default('ECP18', 'ECP18-05-05')
    ECP18_parasitas = fields.Char(
        'Parasitas', readonly=False, default=_default_ECP18_parasitas
    )

    def _write_ECP18_parasitas(self):
        self._set_result('ECP18', 'ECP18-05-05', self.ECP18_lab_test_parasite_names)
        self._copy_result('ECP18', 'ECP18-05-05', self.ECP18_lab_test_parasite_names)

    def _default_ECP18_lab_test_parasite_ids(self):
        LabTestParasite = self.env['clv.lab_test.parasite']
        parasite_ids = []
        if self._get_default('ECP18', 'ECP18-05-05') is not False:
            parasitas = self._get_default('ECP18', 'ECP18-05-05').split(', ')
            for parasita in parasitas:
                parasite = LabTestParasite.search([
                    ('name', '=', parasita),
                ])
                if parasite.id is not False:
                    parasite_ids.append((4, parasite.id))
        return parasite_ids
    ECP18_lab_test_parasite_ids = fields.Many2many(
        comodel_name='clv.lab_test.parasite',
        relation='clv_lab_test_parasite_lab_test_result_copy_to_report_rel',
        string='Lab Test Parasites',
        default=_default_ECP18_lab_test_parasite_ids
    )

    ECP18_lab_test_parasite_names = fields.Char(
        string='Parasitas',
        compute='_compute_ECP18_lab_test_parasite_names',
        store=True
    )
    ECP18_lab_test_parasite_names_suport = fields.Char(
        string='Parasite Names Suport',
        compute='_compute_ECP18_lab_test_parasite_names_suport',
        store=False
    )

    @api.depends('ECP18_lab_test_parasite_ids')
    def _compute_ECP18_lab_test_parasite_names(self):
        for r in self:
            r.ECP18_lab_test_parasite_names = r.ECP18_lab_test_parasite_names_suport

    @api.multi
    def _compute_ECP18_lab_test_parasite_names_suport(self):
        for r in self:
            ECP18_lab_test_parasite_names = False
            for parasite in r.ECP18_lab_test_parasite_ids:
                if ECP18_lab_test_parasite_names is False:
                    ECP18_lab_test_parasite_names = parasite.name
                else:
                    ECP18_lab_test_parasite_names = ECP18_lab_test_parasite_names + ', ' + parasite.name
            r.ECP18_lab_test_parasite_names_suport = ECP18_lab_test_parasite_names

    def _default_ECP18_obs(self):
        return self._get_default('ECP18', 'ECP18-05-06')
    ECP18_obs = fields.Text(
        'Observações', readonly=False, default=_default_ECP18_obs
    )

    def _write_ECP18_obs(self):
        self._set_result('ECP18', 'ECP18-05-06', self.ECP18_obs)
        self._copy_result('ECP18', 'ECP18-05-06', self.ECP18_obs)

    def do_result_copy_to_report(self):

        self._write_ECP18_metodos_utilizados()
        self._write_ECP18_resultado()
        self._write_ECP18_parasitas()
        self._write_ECP18_obs()

        return True
