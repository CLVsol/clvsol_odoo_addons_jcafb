# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class LabTestResultCopyToReport(models.TransientModel):
    _inherit = 'clv.lab_test.result.copy_to_report'

    #
    # ECP19
    #

    def _default_is_ECP19(self):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'ECP19':
            is_ECP19 = True
        else:
            is_ECP19 = False
        return is_ECP19
    is_ECP19 = fields.Boolean('Is ECP19', readonly=True, default=_default_is_ECP19)

    def _default_ECP19_metodos_utilizados(self):
        return self._get_default('ECP19', 'ECP19-05-03')
    # ECP19_metodos_utilizados = fields.Selection([
    #     ('Ritchie', 'Ritchie'),
    #     ('Hoffmann', 'Hoffmann'),
    #     ('Willis', 'Willis'),
    #     ('Ritchie, Hoffmann', 'Ritchie, Hoffmann'),
    #     ('Ritchie, Hoffmann, Willis', 'Ritchie, Hoffmann, Willis'),
    # ], 'Metodologia(s) Empregada(s)', readonly=False, default=_default_ECP19_metodos_utilizados)
    ECP19_metodos_utilizados = fields.Char(
        string='Metodologia(s) Empregada(s)',
        default=_default_ECP19_metodos_utilizados
    )

    def _write_ECP19_metodos_utilizados(self):
        self._set_result('ECP19', 'ECP19-05-03', self.ECP19_metodos_utilizados)
        self._copy_result('ECP19', 'ECP19-05-03', self.ECP19_metodos_utilizados)

    def _default_ECP19_resultado(self):
        return self._get_default('ECP19', 'ECP19-05-04')
    ECP19_resultado = fields.Selection([
        ('POSITIVO', 'POSITIVO'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não realizado', 'Não realizado'),
    ], 'Resultado', readonly=False, default=_default_ECP19_resultado)

    def _write_ECP19_resultado(self):
        self._set_result('ECP19', 'ECP19-05-04', self.ECP19_resultado)
        self._copy_result('ECP19', 'ECP19-05-04', self.ECP19_resultado)

    def _default_ECP19_parasitas(self):
        return self._get_default('ECP19', 'ECP19-05-05')
    ECP19_parasitas = fields.Char(
        'Parasitas', readonly=False, default=_default_ECP19_parasitas
    )

    def _write_ECP19_parasitas(self):
        self._set_result('ECP19', 'ECP19-05-05', self.ECP19_lab_test_parasite_names)
        self._copy_result('ECP19', 'ECP19-05-05', self.ECP19_lab_test_parasite_names)

    def _default_ECP19_lab_test_parasite_ids(self):
        LabTestParasite = self.env['clv.lab_test.parasite']
        parasite_ids = []
        if self._get_default('ECP19', 'ECP19-05-05') is not False:
            parasitas = self._get_default('ECP19', 'ECP19-05-05').split(', ')
            for parasita in parasitas:
                parasite = LabTestParasite.search([
                    ('name', '=', parasita),
                ])
                if parasite.id is not False:
                    parasite_ids.append((4, parasite.id))
        return parasite_ids
    ECP19_lab_test_parasite_ids = fields.Many2many(
        comodel_name='clv.lab_test.parasite',
        relation='clv_lab_test_parasite_lab_test_result_copy_to_report_rel',
        string='Lab Test Parasites',
        default=_default_ECP19_lab_test_parasite_ids
    )

    ECP19_lab_test_parasite_names = fields.Char(
        string='Parasitas',
        compute='_compute_ECP19_lab_test_parasite_names',
        store=True
    )
    ECP19_lab_test_parasite_names_suport = fields.Char(
        string='Parasite Names Suport',
        compute='_compute_ECP19_lab_test_parasite_names_suport',
        store=False
    )

    @api.depends('ECP19_lab_test_parasite_ids')
    def _compute_ECP19_lab_test_parasite_names(self):
        for r in self:
            r.ECP19_lab_test_parasite_names = r.ECP19_lab_test_parasite_names_suport

    @api.multi
    def _compute_ECP19_lab_test_parasite_names_suport(self):
        for r in self:
            ECP19_lab_test_parasite_names = False
            for parasite in r.ECP19_lab_test_parasite_ids:
                if ECP19_lab_test_parasite_names is False:
                    ECP19_lab_test_parasite_names = parasite.name
                else:
                    ECP19_lab_test_parasite_names = ECP19_lab_test_parasite_names + ', ' + parasite.name
            r.ECP19_lab_test_parasite_names_suport = ECP19_lab_test_parasite_names

    def _default_ECP19_obs(self):
        return self._get_default('ECP19', 'ECP19-05-06')
    ECP19_obs = fields.Text(
        'Observações', readonly=False, default=_default_ECP19_obs
    )

    def _write_ECP19_obs(self):
        self._set_result('ECP19', 'ECP19-05-06', self.ECP19_obs)
        self._copy_result('ECP19', 'ECP19-05-06', self.ECP19_obs)

    def _do_result_copy_to_report_ECP19(self):

        self._write_ECP19_metodos_utilizados()
        self._write_ECP19_resultado()
        self._write_ECP19_parasitas()
        self._write_ECP19_obs()

        return True
