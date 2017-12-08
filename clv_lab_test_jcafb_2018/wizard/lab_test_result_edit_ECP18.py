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


class LabTestResultEdit(models.TransientModel):
    _inherit = 'clv.lab_test.result.edit'

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

    # Exame Coproparasitológico (1)

    def _default_ECP18_metodo_utilizado_1(self):
        return self._get_default('ECP18', 'ECP18-01-01')
    ECP18_metodo_utilizado_1 = fields.Selection([
        ('Ritchie', 'Ritchie'),
        ('Hoffmann', 'Hoffmann'),
        ('Willis', 'Willis'),
    ], 'Metodologia Empregada (1)', readonly=False, default=_default_ECP18_metodo_utilizado_1)

    def _write_ECP18_metodo_utilizado_1(self):
        self._set_result('ECP18', 'ECP18-01-01', self.ECP18_metodo_utilizado_1)

    def _default_ECP18_resultado_1(self):
        return self._get_default('ECP18', 'ECP18-01-02')
    ECP18_resultado_1 = fields.Selection([
        ('POSITIVO', 'POSITIVO'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não realizado', 'Não realizado'),
    ], 'Resultado (1)', readonly=False, default=_default_ECP18_resultado_1)

    def _write_ECP18_resultado_1(self):
        self._set_result('ECP18', 'ECP18-01-02', self.ECP18_resultado_1)

    def _default_ECP18_examinador_1(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('ECP18', 'ECP18-01-03')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    ECP18_examinador_1 = fields.Many2one(
        'hr.employee',
        string='Examinador (1)',
        readonly=False,
        default=_default_ECP18_examinador_1
    )

    def _write_ECP18_examinador_1(self):
        if self.ECP18_examinador_1.name is not False:
            self._set_result(
                'ECP18', 'ECP18-01-03',
                self.ECP18_examinador_1.name + ' [' + self.ECP18_examinador_1.code + ']'
            )
        else:
            self._set_result('ECP18', 'ECP18-01-03', False)

    def _default_ECP18_parasitas_1(self):
        return self._get_default('ECP18', 'ECP18-01-04')
    ECP18_parasitas_1 = fields.Char(
        'Parasitas (1)', readonly=False, default=_default_ECP18_parasitas_1
    )

    def _write_ECP18_parasitas_1(self):
        self._set_result('ECP18', 'ECP18-01-04', self.ECP18_lab_test_parasite_1_names)

    def _default_ECP18_lab_test_parasite_1_ids(self):
        LabTestParasite = self.env['clv.lab_test.parasite']
        parasite_ids = []
        if self._get_default('ECP18', 'ECP18-01-04') is not False:
            parasitas = self._get_default('ECP18', 'ECP18-01-04').split(', ')
            for parasita in parasitas:
                parasite = LabTestParasite.search([
                    ('name', '=', parasita),
                ])
                if parasite.id is not False:
                    parasite_ids.append((4, parasite.id))
        return parasite_ids
    ECP18_lab_test_parasite_1_ids = fields.Many2many(
        comodel_name='clv.lab_test.parasite',
        relation='clv_lab_test_parasite_1_lab_test_result_edit_rel',
        string='Lab Test Parasites (1)',
        default=_default_ECP18_lab_test_parasite_1_ids
    )

    ECP18_lab_test_parasite_1_names = fields.Char(
        string='Parasitas (1)',
        compute='_compute_ECP18_lab_test_parasite_1_names',
        store=True
    )
    ECP18_lab_test_parasite_1_names_suport = fields.Char(
        string='Parasite Names Suport (1)',
        compute='_compute_ECP18_lab_test_parasite_1_names_suport',
        store=False
    )

    @api.depends('ECP18_lab_test_parasite_1_ids')
    def _compute_ECP18_lab_test_parasite_1_names(self):
        for r in self:
            r.ECP18_lab_test_parasite_1_names = r.ECP18_lab_test_parasite_1_names_suport

    @api.multi
    def _compute_ECP18_lab_test_parasite_1_names_suport(self):
        for r in self:
            ECP18_lab_test_parasite_1_names = False
            for parasite in r.ECP18_lab_test_parasite_1_ids:
                if ECP18_lab_test_parasite_1_names is False:
                    ECP18_lab_test_parasite_1_names = parasite.name
                else:
                    ECP18_lab_test_parasite_1_names = ECP18_lab_test_parasite_1_names + ', ' + parasite.name
            r.ECP18_lab_test_parasite_1_names_suport = ECP18_lab_test_parasite_1_names

    # Exame Coproparasitológico (2)

    def _default_ECP18_metodo_utilizado_2(self):
        return self._get_default('ECP18', 'ECP18-02-01')
    ECP18_metodo_utilizado_2 = fields.Selection([
        ('Ritchie', 'Ritchie'),
        ('Hoffmann', 'Hoffmann'),
        ('Willis', 'Willis'),
    ], 'Metodologia Empregada (2)', readonly=False, default=_default_ECP18_metodo_utilizado_2)

    def _write_ECP18_metodo_utilizado_2(self):
        self._set_result('ECP18', 'ECP18-02-01', self.ECP18_metodo_utilizado_2)

    def _default_ECP18_resultado_2(self):
        return self._get_default('ECP18', 'ECP18-02-02')
    ECP18_resultado_2 = fields.Selection([
        ('POSITIVO', 'POSITIVO'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não realizado', 'Não realizado'),
    ], 'Resultado (2)', readonly=False, default=_default_ECP18_resultado_2)

    def _write_ECP18_resultado_2(self):
        self._set_result('ECP18', 'ECP18-02-02', self.ECP18_resultado_2)

    def _default_ECP18_examinador_2(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('ECP18', 'ECP18-02-03')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    ECP18_examinador_2 = fields.Many2one(
        'hr.employee',
        string='Examinador (2)',
        readonly=False,
        default=_default_ECP18_examinador_2
    )

    def _write_ECP18_examinador_2(self):
        if self.ECP18_examinador_2.name is not False:
            self._set_result(
                'ECP18', 'ECP18-02-03',
                self.ECP18_examinador_2.name + ' [' + self.ECP18_examinador_2.code + ']'
            )
        else:
            self._set_result('ECP18', 'ECP18-02-03', False)

    def _default_ECP18_parasitas_2(self):
        return self._get_default('ECP18', 'ECP18-02-04')
    ECP18_parasitas_2 = fields.Char(
        'Parasitas (2)', readonly=False, default=_default_ECP18_parasitas_2
    )

    def _write_ECP18_parasitas_2(self):
        self._set_result('ECP18', 'ECP18-02-04', self.ECP18_lab_test_parasite_2_names)

    def _default_ECP18_lab_test_parasite_2_ids(self):
        LabTestParasite = self.env['clv.lab_test.parasite']
        parasite_ids = []
        if self._get_default('ECP18', 'ECP18-02-04') is not False:
            parasitas = self._get_default('ECP18', 'ECP18-02-04').split(', ')
            for parasita in parasitas:
                parasite = LabTestParasite.search([
                    ('name', '=', parasita),
                ])
                if parasite.id is not False:
                    parasite_ids.append((4, parasite.id))
        return parasite_ids
    ECP18_lab_test_parasite_2_ids = fields.Many2many(
        comodel_name='clv.lab_test.parasite',
        relation='clv_lab_test_parasite_2_lab_test_result_edit_rel',
        string='Lab Test Parasites (2)',
        default=_default_ECP18_lab_test_parasite_2_ids
    )

    ECP18_lab_test_parasite_2_names = fields.Char(
        string='Parasitas (2)',
        compute='_compute_ECP18_lab_test_parasite_2_names',
        store=True
    )
    ECP18_lab_test_parasite_2_names_suport = fields.Char(
        string='Parasite Names Suport (2)',
        compute='_compute_ECP18_lab_test_parasite_2_names_suport',
        store=False
    )

    @api.depends('ECP18_lab_test_parasite_2_ids')
    def _compute_ECP18_lab_test_parasite_2_names(self):
        for r in self:
            r.ECP18_lab_test_parasite_2_names = r.ECP18_lab_test_parasite_2_names_suport

    @api.multi
    def _compute_ECP18_lab_test_parasite_2_names_suport(self):
        for r in self:
            ECP18_lab_test_parasite_2_names = False
            for parasite in r.ECP18_lab_test_parasite_2_ids:
                if ECP18_lab_test_parasite_2_names is False:
                    ECP18_lab_test_parasite_2_names = parasite.name
                else:
                    ECP18_lab_test_parasite_2_names = ECP18_lab_test_parasite_2_names + ', ' + parasite.name
            r.ECP18_lab_test_parasite_2_names_suport = ECP18_lab_test_parasite_2_names

    # Exame Coproparasitológico (3)

    def _default_ECP18_metodo_utilizado_3(self):
        return self._get_default('ECP18', 'ECP18-03-01')
    ECP18_metodo_utilizado_3 = fields.Selection([
        ('Ritchie', 'Ritchie'),
        ('Hoffmann', 'Hoffmann'),
        ('Willis', 'Willis'),
    ], 'Metodologia Empregada (3)', readonly=False, default=_default_ECP18_metodo_utilizado_3)

    def _write_ECP18_metodo_utilizado_3(self):
        self._set_result('ECP18', 'ECP18-03-01', self.ECP18_metodo_utilizado_3)

    def _default_ECP18_resultado_3(self):
        return self._get_default('ECP18', 'ECP18-03-02')
    ECP18_resultado_3 = fields.Selection([
        ('POSITIVO', 'POSITIVO'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não realizado', 'Não realizado'),
    ], 'Resultado (3)', readonly=False, default=_default_ECP18_resultado_3)

    def _write_ECP18_resultado_3(self):
        self._set_result('ECP18', 'ECP18-03-02', self.ECP18_resultado_3)

    def _default_ECP18_examinador_3(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('ECP18', 'ECP18-03-03')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    ECP18_examinador_3 = fields.Many2one(
        'hr.employee',
        string='Examinador (3)',
        readonly=False,
        default=_default_ECP18_examinador_3
    )

    def _write_ECP18_examinador_3(self):
        if self.ECP18_examinador_3.name is not False:
            self._set_result(
                'ECP18', 'ECP18-03-03',
                self.ECP18_examinador_3.name + ' [' + self.ECP18_examinador_3.code + ']'
            )
        else:
            self._set_result('ECP18', 'ECP18-03-03', False)

    def _default_ECP18_parasitas_3(self):
        return self._get_default('ECP18', 'ECP18-03-04')
    ECP18_parasitas_3 = fields.Char(
        'Parasitas (3)', readonly=False, default=_default_ECP18_parasitas_3
    )

    def _write_ECP18_parasitas_3(self):
        self._set_result('ECP18', 'ECP18-03-04', self.ECP18_lab_test_parasite_3_names)

    def _default_ECP18_lab_test_parasite_3_ids(self):
        LabTestParasite = self.env['clv.lab_test.parasite']
        parasite_ids = []
        if self._get_default('ECP18', 'ECP18-03-04') is not False:
            parasitas = self._get_default('ECP18', 'ECP18-03-04').split(', ')
            for parasita in parasitas:
                parasite = LabTestParasite.search([
                    ('name', '=', parasita),
                ])
                if parasite.id is not False:
                    parasite_ids.append((4, parasite.id))
        return parasite_ids
    ECP18_lab_test_parasite_3_ids = fields.Many2many(
        comodel_name='clv.lab_test.parasite',
        relation='clv_lab_test_parasite_3_lab_test_result_edit_rel',
        string='Lab Test Parasites (3)',
        default=_default_ECP18_lab_test_parasite_3_ids
    )

    ECP18_lab_test_parasite_3_names = fields.Char(
        string='Parasitas (3)',
        compute='_compute_ECP18_lab_test_parasite_3_names',
        store=True
    )
    ECP18_lab_test_parasite_3_names_suport = fields.Char(
        string='Parasite Names Suport (3)',
        compute='_compute_ECP18_lab_test_parasite_3_names_suport',
        store=False
    )

    @api.depends('ECP18_lab_test_parasite_3_ids')
    def _compute_ECP18_lab_test_parasite_3_names(self):
        for r in self:
            r.ECP18_lab_test_parasite_3_names = r.ECP18_lab_test_parasite_3_names_suport

    @api.multi
    def _compute_ECP18_lab_test_parasite_3_names_suport(self):
        for r in self:
            ECP18_lab_test_parasite_3_names = False
            for parasite in r.ECP18_lab_test_parasite_3_ids:
                if ECP18_lab_test_parasite_3_names is False:
                    ECP18_lab_test_parasite_3_names = parasite.name
                else:
                    ECP18_lab_test_parasite_3_names = ECP18_lab_test_parasite_3_names + ', ' + parasite.name
            r.ECP18_lab_test_parasite_3_names_suport = ECP18_lab_test_parasite_3_names

    # Exame Coproparasitológico (4)

    def _default_ECP18_metodo_utilizado_4(self):
        return self._get_default('ECP18', 'ECP18-04-01')
    # ECP18_metodo_utilizado_4 = fields.Selection([
    #     ('Ritchie', 'Ritchie'),
    #     ('Hoffmann', 'Hoffmann'),
    #     ('Willis', 'Willis'),
    # ], 'Metodologia Empregada (4)', readonly=False, default=_default_ECP18_metodo_utilizado_4)
    ECP18_metodo_utilizado_4 = fields.Char(
        string='Metodologia(s) Empregada(s)',
        default=_default_ECP18_metodo_utilizado_4,
    )

    def _write_ECP18_metodo_utilizado_4(self):
        self._set_result('ECP18', 'ECP18-04-01', self.ECP18_metodo_utilizado_4)

    def _default_ECP18_resultado_4(self):
        return self._get_default('ECP18', 'ECP18-04-02')
    ECP18_resultado_4 = fields.Selection([
        ('POSITIVO', 'POSITIVO'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não realizado', 'Não realizado'),
    ], 'Resultado (4)', readonly=False, default=_default_ECP18_resultado_4)

    def _write_ECP18_resultado_4(self):
        self._set_result('ECP18', 'ECP18-04-02', self.ECP18_resultado_4)

    def _default_ECP18_examinador_4(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('ECP18', 'ECP18-04-03')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    ECP18_examinador_4 = fields.Many2one(
        'hr.employee',
        string='Examinador (4)',
        readonly=False,
        default=_default_ECP18_examinador_4
    )

    def _write_ECP18_examinador_4(self):
        if self.ECP18_examinador_4.name is not False:
            self._set_result(
                'ECP18', 'ECP18-04-03',
                self.ECP18_examinador_4.name + ' [' + self.ECP18_examinador_4.code + ']'
            )
        else:
            self._set_result('ECP18', 'ECP18-04-03', False)

    def _default_ECP18_parasitas_4(self):
        return self._get_default('ECP18', 'ECP18-04-04')
    ECP18_parasitas_4 = fields.Char(
        'Parasitas (4)', readonly=False, default=_default_ECP18_parasitas_4
    )

    def _write_ECP18_parasitas_4(self):
        self._set_result('ECP18', 'ECP18-04-04', self.ECP18_lab_test_parasite_4_names)

    def _default_ECP18_lab_test_parasite_4_ids(self):
        LabTestParasite = self.env['clv.lab_test.parasite']
        parasite_ids = []
        if self._get_default('ECP18', 'ECP18-04-04') is not False:
            parasitas = self._get_default('ECP18', 'ECP18-04-04').split(', ')
            for parasita in parasitas:
                parasite = LabTestParasite.search([
                    ('name', '=', parasita),
                ])
                if parasite.id is not False:
                    parasite_ids.append((4, parasite.id))
        return parasite_ids
    ECP18_lab_test_parasite_4_ids = fields.Many2many(
        comodel_name='clv.lab_test.parasite',
        relation='clv_lab_test_parasite_4_lab_test_result_edit_rel',
        string='Lab Test Parasites (4)',
        default=_default_ECP18_lab_test_parasite_4_ids
    )

    ECP18_lab_test_parasite_4_names = fields.Char(
        string='Parasitas (4)',
        compute='_compute_ECP18_lab_test_parasite_4_names',
        store=True
    )
    ECP18_lab_test_parasite_4_names_suport = fields.Char(
        string='Parasite Names Suport (4)',
        compute='_compute_ECP18_lab_test_parasite_4_names_suport',
        store=False
    )

    @api.depends('ECP18_lab_test_parasite_4_ids')
    def _compute_ECP18_lab_test_parasite_4_names(self):
        for r in self:
            r.ECP18_lab_test_parasite_4_names = r.ECP18_lab_test_parasite_4_names_suport

    @api.multi
    def _compute_ECP18_lab_test_parasite_4_names_suport(self):
        for r in self:
            ECP18_lab_test_parasite_4_names = False
            for parasite in r.ECP18_lab_test_parasite_4_ids:
                if ECP18_lab_test_parasite_4_names is False:
                    ECP18_lab_test_parasite_4_names = parasite.name
                else:
                    ECP18_lab_test_parasite_4_names = ECP18_lab_test_parasite_4_names + ', ' + parasite.name
            r.ECP18_lab_test_parasite_4_names_suport = ECP18_lab_test_parasite_4_names

    # Exame Coproparasitológico

    def _default_ECP18_data_entrada_material(self):
        return self._get_default('ECP18', 'ECP18-05-01')
    ECP18_data_entrada_material = fields.Date(
        'Data de Entrada do Material', readonly=False, default=_default_ECP18_data_entrada_material
    )

    def _write_ECP18_data_entrada_material(self):
        self._set_result('ECP18', 'ECP18-05-01', self.ECP18_data_entrada_material)

    def _default_ECP18_liberacao_resultado(self):
        return self._get_default('ECP18', 'ECP18-05-02')
    ECP18_liberacao_resultado = fields.Date(
        'Liberação do Resultado', readonly=False, default=_default_ECP18_liberacao_resultado
    )

    def _write_ECP18_liberacao_resultado(self):
        self._set_result('ECP18', 'ECP18-05-02', self.ECP18_liberacao_resultado)

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
        default=_default_ECP18_metodos_utilizados,
        compute='_compute_ECP18_metodos_utilizados',
        store=True
    )

    def _write_ECP18_metodos_utilizados(self):
        self._set_result('ECP18', 'ECP18-05-03', self.ECP18_metodos_utilizados)

    def _default_ECP18_resultado(self):
        return self._get_default('ECP18', 'ECP18-05-04')
    ECP18_resultado = fields.Selection([
        ('POSITIVO', 'POSITIVO'),
        ('NEGATIVO', 'NEGATIVO'),
        ('Não realizado', 'Não realizado'),
    ],
        string='Resultado',
        readonly=False,
        default=_default_ECP18_resultado
    )

    def _write_ECP18_resultado(self):
        self._set_result('ECP18', 'ECP18-05-04', self.ECP18_resultado)

    def _default_ECP18_parasitas(self):
        return self._get_default('ECP18', 'ECP18-05-05')
    ECP18_parasitas = fields.Char(
        'Parasitas', readonly=False, default=_default_ECP18_parasitas
    )

    def _write_ECP18_parasitas(self):
        self._set_result('ECP18', 'ECP18-05-05', self.ECP18_lab_test_parasite_names)

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
        relation='clv_lab_test_parasite_lab_test_result_edit_rel',
        string='Lab Test Parasites',
        default=_default_ECP18_lab_test_parasite_ids,
        compute='_compute_ECP18_lab_test_parasite_ids',
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

    @api.depends(
        'ECP18_metodo_utilizado_1',
        'ECP18_metodo_utilizado_2',
        'ECP18_metodo_utilizado_3',
        'ECP18_metodo_utilizado_4',
    )
    def _compute_ECP18_metodos_utilizados(self):
        for r in self:
            ECP18_metodos_utilizados = False
            if r.ECP18_metodo_utilizado_1 is not False:
                ECP18_metodos_utilizados = r.ECP18_metodo_utilizado_1
                if r.ECP18_metodo_utilizado_2 is not False:
                    ECP18_metodos_utilizados = ECP18_metodos_utilizados + ', ' + r.ECP18_metodo_utilizado_2
                if r.ECP18_metodo_utilizado_3 is not False:
                    ECP18_metodos_utilizados = ECP18_metodos_utilizados + ', ' + r.ECP18_metodo_utilizado_3
                if r.ECP18_metodo_utilizado_4 is not False:
                    ECP18_metodos_utilizados = ECP18_metodos_utilizados + ', ' + r.ECP18_metodo_utilizado_4
            elif r.ECP18_metodo_utilizado_2 is not False:
                ECP18_metodos_utilizados = r.ECP18_metodo_utilizado_2
                if r.ECP18_metodo_utilizado_3 is not False:
                    ECP18_metodos_utilizados = ECP18_metodos_utilizados + ', ' + r.ECP18_metodo_utilizado_3
                if r.ECP18_metodo_utilizado_4 is not False:
                    ECP18_metodos_utilizados = ECP18_metodos_utilizados + ', ' + r.ECP18_metodo_utilizado_4
            elif r.ECP18_metodo_utilizado_3 is not False:
                ECP18_metodos_utilizados = r.ECP18_metodo_utilizado_3
                if r.ECP18_metodo_utilizado_4 is not False:
                    ECP18_metodos_utilizados = ECP18_metodos_utilizados + ', ' + r.ECP18_metodo_utilizado_4
            elif r.ECP18_metodo_utilizado_4 is not False:
                ECP18_metodos_utilizados = r.ECP18_metodo_utilizado_4
            r.ECP18_metodos_utilizados = ECP18_metodos_utilizados

    @api.depends(
        'ECP18_lab_test_parasite_1_ids',
        'ECP18_lab_test_parasite_2_ids',
        'ECP18_lab_test_parasite_3_ids',
        'ECP18_lab_test_parasite_4_ids',
    )
    def _compute_ECP18_lab_test_parasite_ids(self):
        parasite_ids = []
        for r in self:
            for parasite in self.ECP18_lab_test_parasite_1_ids:
                if parasite.id is not False:
                    parasite_ids.append((4, parasite.id))
            for parasite in self.ECP18_lab_test_parasite_2_ids:
                if parasite.id is not False:
                    parasite_ids.append((4, parasite.id))
            for parasite in self.ECP18_lab_test_parasite_3_ids:
                if parasite.id is not False:
                    parasite_ids.append((4, parasite.id))
            for parasite in self.ECP18_lab_test_parasite_4_ids:
                if parasite.id is not False:
                    parasite_ids.append((4, parasite.id))
            r.ECP18_lab_test_parasite_ids = parasite_ids

    def _do_result_updt_ECP18(self):

        self._write_ECP18_metodo_utilizado_1()
        self._write_ECP18_resultado_1()
        self._write_ECP18_examinador_1()
        self._write_ECP18_parasitas_1()

        self._write_ECP18_metodo_utilizado_2()
        self._write_ECP18_resultado_2()
        self._write_ECP18_examinador_2()
        self._write_ECP18_parasitas_2()

        self._write_ECP18_metodo_utilizado_3()
        self._write_ECP18_resultado_3()
        self._write_ECP18_examinador_3()
        self._write_ECP18_parasitas_3()

        self._write_ECP18_metodo_utilizado_4()
        self._write_ECP18_resultado_4()
        self._write_ECP18_examinador_4()
        self._write_ECP18_parasitas_4()

        self._write_ECP18_data_entrada_material()
        self._write_ECP18_liberacao_resultado()
        self._write_ECP18_metodos_utilizados()
        self._write_ECP18_resultado()
        self._write_ECP18_parasitas()
        self._write_ECP18_obs()

        return True
