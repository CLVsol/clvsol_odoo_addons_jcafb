# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class LabTestResultEditEDH20(models.TransientModel):
    _description = 'Lab Test Result Edit (EDH20)'
    _name = 'clv.lab_test.result.edit_edh20'

    def _get_default(self, lab_test_type_id_code, criterion_code):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == lab_test_type_id_code:
            result = active_id.criterion_ids.search([
                ('lab_test_result_id', '=', active_id.id),
                ('code', '=', criterion_code),
            ]).result
        else:
            result = False
        return result

    def _set_result(self, lab_test_type_id_code, criterion_code, result):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == lab_test_type_id_code:
            criterion_reg = active_id.criterion_ids.search([
                ('lab_test_result_id', '=', active_id.id),
                ('code', '=', criterion_code),
            ])
            criterion_reg.result = result

    def _default_result_id(self):
        return self._context.get('active_id')
    result_id = fields.Many2one(
        comodel_name='clv.lab_test.result',
        string='Result',
        readonly=True,
        default=_default_result_id
    )

    def _default_lab_test_type_id(self):
        return self.env['clv.lab_test.result'].browse(self._context.get('active_id')).lab_test_type_id
    lab_test_type_id = fields.Many2one(
        comodel_name='clv.lab_test.type',
        string='Lab Test Type',
        readonly=True,
        default=_default_lab_test_type_id
    )

    def _default_lab_test_request_id(self):
        return self.env['clv.lab_test.result'].browse(self._context.get('active_id')).lab_test_request_id
    lab_test_request_id = fields.Many2one(
        comodel_name='clv.lab_test.request',
        string='Lab Test Request',
        readonly=True,
        default=_default_lab_test_request_id
    )

    #
    # EDH20
    #

    def _default_EDH20_tempo_jejum(self):
        return self._get_default('EDH20', 'EDH20-01-01')
    EDH20_tempo_jejum = fields.Char(
        'Tempo de Jejum', readonly=False, default=_default_EDH20_tempo_jejum
    )

    def _write_EDH20_tempo_jejum(self):
        self._set_result('EDH20', 'EDH20-01-01', self.EDH20_tempo_jejum)

    def _default_EDH20_peso(self):
        return self._get_default('EDH20', 'EDH20-02-01')
    EDH20_peso = fields.Char(
        'Peso', readonly=False, default=_default_EDH20_peso
    )

    def _write_EDH20_peso(self):
        self._set_result('EDH20', 'EDH20-02-01', self.EDH20_peso)

    def _default_EDH20_peso_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EDH20', 'EDH20-02-02')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EDH20_peso_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida do Peso',
        readonly=False,
        default=_default_EDH20_peso_resp
    )

    def _write_EDH20_peso_resp(self):
        if self.EDH20_peso_resp.name is not False:
            self._set_result(
                'EDH20', 'EDH20-02-02', self.EDH20_peso_resp.name + ' [' + self.EDH20_peso_resp.code + ']'
            )
        else:
            self._set_result('EDH20', 'EDH20-02-02', False)

    def _default_EDH20_altura(self):
        return self._get_default('EDH20', 'EDH20-02-03')
    EDH20_altura = fields.Char(
        'Altura', readonly=False, default=_default_EDH20_altura
    )

    def _write_EDH20_altura(self):
        self._set_result('EDH20', 'EDH20-02-03', self.EDH20_altura)

    def _default_EDH20_altura_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EDH20', 'EDH20-02-04')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EDH20_altura_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida da Altura',
        readonly=False,
        default=_default_EDH20_altura_resp
    )

    def _write_EDH20_altura_resp(self):
        if self.EDH20_altura_resp.name is not False:
            self._set_result(
                'EDH20', 'EDH20-02-04', self.EDH20_altura_resp.name + ' [' + self.EDH20_altura_resp.code + ']'
            )
        else:
            self._set_result('EDH20', 'EDH20-02-04', False)

    def _default_EDH20_imc(self):
        return self._get_default('EDH20', 'EDH20-02-05')
    EDH20_imc = fields.Char(
        'IMC', readonly=False, default=_default_EDH20_imc
    )

    def _write_EDH20_imc(self):
        self._set_result('EDH20', 'EDH20-02-05', self.EDH20_imc)

    def _default_EDH20_imc_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EDH20', 'EDH20-02-06')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EDH20_imc_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida do IMC',
        readonly=False,
        default=_default_EDH20_imc_resp
    )

    def _write_EDH20_imc_resp(self):
        if self.EDH20_imc_resp.name is not False:
            self._set_result(
                'EDH20', 'EDH20-02-06', self.EDH20_imc_resp.name + ' [' + self.EDH20_imc_resp.code + ']'
            )
        else:
            self._set_result('EDH20', 'EDH20-02-06', False)

    def _default_EDH20_interpretacao_imc(self):
        return self._get_default('EDH20', 'EDH20-02-07')
    EDH20_interpretacao_imc = fields.Selection([
        (u'a) Baixo peso (Adultos:menor que 18,5; Idosos (M e F): menor que 21,9)',
            u'a) Baixo peso (Adultos:menor que 18,5; Idosos (M e F): menor que 21,9)'),
        (u'b) Peso Normal (Adultos: 18,5 a 24,9; Idosos (M e F): 22,0 a 27,0)',
            u'b) Peso Normal (Adultos: 18,5 a 24,9; Idosos (M e F): 22,0 a 27,0)'),
        (u'c) Sobrepeso (Pré-obeso) (Adultos: 25,0 a 29,9; Idosos(M): 27,1 a 30,0/Idosos(F): 27,1 a 32,0)',
            u'c) Sobrepeso (Pré-obeso) (Adultos: 25,0 a 29,9; Idosos(M): 27,1 a 30,0/Idosos(F): 27,1 a 32,0)'),
        (u'd) Obesidade Grau I (Adultos: 30,0 a 34,9; Idosos(M): 30,1,1 a 35,0/Idosos(F): 32,1 a 37,0)',
            u'd) Obesidade Grau I (Adultos: 30,0 a 34,9; Idosos(M): 30,1,1 a 35,0/Idosos(F): 32,1 a 37,0)'),
        (u'e) Obesidade Grau II (Adultos: 35,0 a 39,9; Idosos(M): 35,1 a 39,0/Idosos(F): 37,1 a 41,9)',
            u'e) Obesidade Grau II (Adultos: 35,0 a 39,9; Idosos(M): 35,1 a 39,0/Idosos(F): 37,1 a 41,9)'),
        (u'f) Obesidade Grau III (Adultos:maior ou igual a 40,0; Idosos(M):maior ou igual a 40,0/Idosos(F):maior ou igual a 42,0)',
            'f) Obesidade Grau III (Adultos:maior ou igual a 40,0; Idosos(M):maior ou igual a 40,0/Idosos(F):maior ou igual a 42,0)'),
        (u'g) Não interpretado (justificar em "Observações")',
            u'g) Não interpretado (justificar em "Observações")'),
        (u'h) Não se aplica',
            u'h) Não se aplica'),
    ], 'Interpretação do valor de IMC', readonly=False, default=_default_EDH20_interpretacao_imc)

    def _write_EDH20_interpretacao_imc(self):
        self._set_result('EDH20', 'EDH20-02-07', self.EDH20_interpretacao_imc)

    def _default_EDH20_interpretacao_imc_obs(self):
        return self._get_default('EDH20', 'EDH20-02-08')
    EDH20_interpretacao_imc_obs = fields.Char(
        'Observações (IMC)', readonly=False, default=_default_EDH20_interpretacao_imc_obs
    )

    def _write_EDH20_interpretacao_imc_obs(self):
        self._set_result('EDH20', 'EDH20-02-08', self.EDH20_interpretacao_imc_obs)

    def _default_EDH20_circ_abdominal(self):
        return self._get_default('EDH20', 'EDH20-02-09')
    EDH20_circ_abdominal = fields.Char(
        'Circunferência abdominal', readonly=False, default=_default_EDH20_circ_abdominal
    )

    def _write_EDH20_circ_abdominal(self):
        self._set_result('EDH20', 'EDH20-02-09', self.EDH20_circ_abdominal)

    def _default_EDH20_circ_abdominal_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EDH20', 'EDH20-02-10')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EDH20_circ_abdominal_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida da Circunferência abdominal',
        readonly=False,
        default=_default_EDH20_circ_abdominal_resp
    )

    def _write_EDH20_circ_abdominal_resp(self):
        if self.EDH20_circ_abdominal_resp.name is not False:
            self._set_result(
                'EDH20', 'EDH20-02-10',
                self.EDH20_circ_abdominal_resp.name + ' [' + self.EDH20_circ_abdominal_resp.code + ']'
            )
        else:
            self._set_result('EDH20', 'EDH20-02-10', False)

    def _default_EDH20_interpretacao_circ_abdominal(self):
        return self._get_default('EDH20', 'EDH20-02-11')
    EDH20_interpretacao_circ_abdominal = fields.Selection([
        (u'a) Normal (H:menor que 94 cm; M:menor que 80 cm)',
            u'a) Normal (H:menor que 94 cm; M:menor que 80 cm)'),
        (u'b) Risco aumentado (H:maior ou igual a 94 cm; M:maior ou igual a 80 cm)',
            u'b) Risco aumentado (H:maior ou igual a 94 cm; M:maior ou igual a 80 cm)'),
        (u'c) Risco aumentado substancialmente (H:maior ou igual a 102 cm; M:maior ou igual a 88 cm))',
            u'c) Risco aumentado substancialmente (H:maior ou igual a 102 cm; M:maior ou igual a 88 cm))'),
        (u'd) Não interpretado (justificar em observações)',
            u'd) Não interpretado (justificar em observações)'),
        (u'e) Não se aplica',
            u'e) Não se aplica'),
    ], 'Interpretação do valor de Circunferência Abdominal',
        readonly=False, default=_default_EDH20_interpretacao_circ_abdominal)

    def _write_EDH20_interpretacao_circ_abdominal(self):
        self._set_result('EDH20', 'EDH20-02-11', self.EDH20_interpretacao_circ_abdominal)

    def _default_EDH20_interpretacao_circ_abdominal_obs(self):
        return self._get_default('EDH20', 'EDH20-02-12')
    EDH20_interpretacao_circ_abdominal_obs = fields.Char(
        'Observações (Circ Abdm)', readonly=False, default=_default_EDH20_interpretacao_circ_abdominal_obs
    )

    def _write_EDH20_interpretacao_circ_abdominal_obs(self):
        self._set_result('EDH20', 'EDH20-02-12', self.EDH20_interpretacao_circ_abdominal_obs)

    def _default_EDH20_pa_automatica(self):
        return self._get_default('EDH20', 'EDH20-03-01')
    EDH20_pa_automatica = fields.Char(
        'Pressão arterial automática', readonly=False, default=_default_EDH20_pa_automatica
    )

    def _write_EDH20_pa_automatica(self):
        self._set_result('EDH20', 'EDH20-03-01', self.EDH20_pa_automatica)

    def _default_EDH20_pa_automatica_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EDH20', 'EDH20-03-02')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EDH20_pa_automatica_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida da Pressão arterial automática',
        readonly=False,
        default=_default_EDH20_pa_automatica_resp
    )

    def _write_EDH20_pa_automatica_resp(self):
        if self.EDH20_pa_automatica_resp.name is not False:
            self._set_result(
                'EDH20', 'EDH20-03-02',
                self.EDH20_pa_automatica_resp.name + ' [' + self.EDH20_pa_automatica_resp.code + ']'
            )
        else:
            self._set_result('EDH20', 'EDH20-03-02', False)

    def _default_EDH20_pa_manual(self):
        return self._get_default('EDH20', 'EDH20-03-03')
    EDH20_pa_manual = fields.Char(
        'Pressão arterial manual', readonly=False, default=_default_EDH20_pa_manual
    )

    def _write_EDH20_pa_manual(self):
        self._set_result('EDH20', 'EDH20-03-03', self.EDH20_pa_manual)

    def _default_EDH20_pa_manual_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EDH20', 'EDH20-03-04')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EDH20_pa_manual_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida da Pressão arterial manual',
        readonly=False,
        default=_default_EDH20_pa_manual_resp
    )

    def _write_EDH20_pa_manual_resp(self):
        if self.EDH20_pa_manual_resp.name is not False:
            self._set_result(
                'EDH20', 'EDH20-03-04',
                self.EDH20_pa_manual_resp.name + ' [' + self.EDH20_pa_manual_resp.code + ']'
            )
        else:
            self._set_result('EDH20', 'EDH20-03-04', False)

    def _default_EDH20_pa(self):
        return self._get_default('EDH20', 'EDH20-03-05')
    EDH20_pa = fields.Char(
        'Pressão arterial', readonly=False, default=_default_EDH20_pa
    )

    def _write_EDH20_pa(self):
        self._set_result('EDH20', 'EDH20-03-05', self.EDH20_pa)

    def _default_EDH20_PAS(self):
        return self._get_default('EDH20', 'EDH20-03-06')
    EDH20_PAS = fields.Char(
        'PAS', readonly=False, default=_default_EDH20_PAS
    )

    def _write_EDH20_PAS(self):
        self._set_result('EDH20', 'EDH20-03-06', self.EDH20_PAS)

    def _default_EDH20_PAD(self):
        return self._get_default('EDH20', 'EDH20-03-07')
    EDH20_PAD = fields.Char(
        'PAD', readonly=False, default=_default_EDH20_PAD
    )

    def _write_EDH20_PAD(self):
        self._set_result('EDH20', 'EDH20-03-07', self.EDH20_PAD)

    def _default_EDH20_interpretacao_pa(self):
        return self._get_default('EDH20', 'EDH20-03-08')
    EDH20_interpretacao_pa = fields.Selection([
        (u'a) Normal (PAS menor que 130 mmHg e PAD menor que 85 mmHg)',
            u'a) Normal (PAS menor que 130 mmHg e PAD menor que 85 mmHg)'),
        (u'b) Limítrofe (PAS:130-139 mmHg e PAD:85-89 mmHg)',
            u'b) Limítrofe (PAS:130-139 mmHg e PAD:85-89 mmHg)'),
        (u'c) Alta (PAS:maior ou igual a 140 mmHg e PAD:maior ou igual a 90 mmHg)',
            u'c) Alta (PAS:maior ou igual a 140 mmHg e PAD:maior ou igual a 90 mmHg)'),
        (u'd) Não interpretado (justificar em observações)',
            u'd) Não interpretado (justificar em observações)'),
        (u'e) Não se aplica',
            u'e) Não se aplica'),
    ], 'Interpretação do valor de Pressão Arterial',
        readonly=False, default=_default_EDH20_interpretacao_pa)

    def _write_EDH20_interpretacao_pa(self):
        self._set_result('EDH20', 'EDH20-03-08', self.EDH20_interpretacao_pa)

    def _default_EDH20_interpretacao_pa_obs(self):
        return self._get_default('EDH20', 'EDH20-03-09')
    EDH20_interpretacao_pa_obs = fields.Char(
        'Observações (PA)', readonly=False, default=_default_EDH20_interpretacao_pa_obs
    )

    def _write_EDH20_interpretacao_pa_obs(self):
        self._set_result('EDH20', 'EDH20-03-09', self.EDH20_interpretacao_pa_obs)

    def _default_EDH20_glicemia(self):
        return self._get_default('EDH20', 'EDH20-04-01')
    EDH20_glicemia = fields.Char(
        'Glicemia', readonly=False, default=_default_EDH20_glicemia
    )

    def _write_EDH20_glicemia(self):
        self._set_result('EDH20', 'EDH20-04-01', self.EDH20_glicemia)

    def _default_EDH20_glicemia_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EDH20', 'EDH20-04-02')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EDH20_glicemia_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida da Glicemia',
        readonly=False,
        default=_default_EDH20_glicemia_resp
    )

    def _write_EDH20_glicemia_resp(self):
        if self.EDH20_glicemia_resp.name is not False:
            self._set_result(
                'EDH20', 'EDH20-04-02',
                self.EDH20_glicemia_resp.name + ' [' + self.EDH20_glicemia_resp.code + ']'
            )
        else:
            self._set_result('EDH20', 'EDH20-04-02', False)

    def _default_EDH20_interpretacao_glicemia(self):
        return self._get_default('EDH20', 'EDH20-04-03')
    EDH20_interpretacao_glicemia = fields.Selection([
        (u'a) Normal para jejum de 8-12 hs(menor ou igual a 99 mg/dL)',
            u'a) Normal para jejum de 8-12 hs(menor ou igual a 99 mg/dL)'),
        (u'b) Pré-diabetes (para jejum de 8-12 hs) = risco aumentado para diabetes (100-125 mg/dL)',
            u'b) Pré-diabetes (para jejum de 8-12 hs) = risco aumentado para diabetes (100-125 mg/dL)'),
        (u'c) Diabetes - para jejum de 8-12 hs (maior que 126 mg/dL, )',
            u'c) Diabetes - para jejum de 8-12 hs (maior que 126 mg/dL, )'),
        (u'd) Jejum INFERIOR a 8 hs: Normal (até 140 mg/dL)',
            u'd) Jejum INFERIOR a 8 hs: Normal (até 140 mg/dL)'),
        (u'e) Jejum INFERIOR a 8 hs: Aumentado (maior ou igual a 140 mg/dL)',
            u'e) Jejum INFERIOR a 8 hs: Aumentado (maior ou igual a 140 mg/dL)'),
        (u'f) Não avaliado (justificar)',
            u'f) Não avaliado (justificar)'),
        (u'g) Não se aplica',
            u'g) Não se aplica'),
    ], 'Interpretação do valor de Glicemia',
        readonly=False, default=_default_EDH20_interpretacao_glicemia)

    def _write_EDH20_interpretacao_glicemia(self):
        self._set_result('EDH20', 'EDH20-04-03', self.EDH20_interpretacao_glicemia)

    def _default_EDH20_interpretacao_glicemia_obs(self):
        return self._get_default('EDH20', 'EDH20-04-04')
    EDH20_interpretacao_glicemia_obs = fields.Char(
        'Observações (Glicemia)', readonly=False, default=_default_EDH20_interpretacao_glicemia_obs
    )

    def _write_EDH20_interpretacao_glicemia_obs(self):
        self._set_result('EDH20', 'EDH20-04-04', self.EDH20_interpretacao_glicemia_obs)

    def _default_EDH20_colesterol(self):
        return self._get_default('EDH20', 'EDH20-04-05')
    EDH20_colesterol = fields.Char(
        'Colesterol', readonly=False, default=_default_EDH20_colesterol
    )

    def _write_EDH20_colesterol(self):
        self._set_result('EDH20', 'EDH20-04-05', self.EDH20_colesterol)

    def _default_EDH20_colesterol_resp(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EDH20', 'EDH20-04-06')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EDH20_colesterol_resp = fields.Many2one(
        'hr.employee',
        string='Responsável pela medida da Colesterol',
        readonly=False,
        default=_default_EDH20_colesterol_resp
    )

    def _write_EDH20_colesterol_resp(self):
        if self.EDH20_colesterol_resp.name is not False:
            self._set_result(
                'EDH20', 'EDH20-04-06',
                self.EDH20_colesterol_resp.name + ' [' + self.EDH20_colesterol_resp.code + ']'
            )
        else:
            self._set_result('EDH20', 'EDH20-04-06', False)

    def _default_EDH20_interpretacao_colesterol(self):
        return self._get_default('EDH20', 'EDH20-04-07')
    EDH20_interpretacao_colesterol = fields.Selection([
        (u'a) Desejável:Acima de 20 anos:menor que 200 mg/dL;2-19 anos:menor que 150 mg/dL',
            u'a) Desejável:Acima de 20 anos:menor que 200 mg/dL;2-19 anos:menor que 150 mg/dL'),
        (u'b) Limítrofe:Acima de 20 anos:200–239 mg/dL;2-19 anos:150-169 mg/dL',
            u'b) Limítrofe:Acima de 20 anos:200–239 mg/dL;2-19 anos:150-169 mg/dL'),
        (u'c) Elevado: Acima de 20 anos:maior ou igual a 240 mg/dL;2-19 anos:maior ou igual a 180 mg/dL',
            u'c) Elevado: Acima de 20 anos:maior ou igual a 240 mg/dL;2-19 anos:maior ou igual a 180 mg/dL'),
        (u'd) Não interpretado (justificar em "Observações")',
            u'd) Não interpretado (justificar em "Observações")'),
        (u'e) Não se aplica',
            u'e) Não se aplica'),
    ], 'Interpretação do valor de Colesterol',
        readonly=False, default=_default_EDH20_interpretacao_colesterol)

    def _write_EDH20_interpretacao_colesterol(self):
        self._set_result('EDH20', 'EDH20-04-07', self.EDH20_interpretacao_colesterol)

    def _default_EDH20_interpretacao_colesterol_obs(self):
        return self._get_default('EDH20', 'EDH20-04-08')
    EDH20_interpretacao_colesterol_obs = fields.Char(
        'Observações (Colesterol)', readonly=False, default=_default_EDH20_interpretacao_colesterol_obs
    )

    def _write_EDH20_interpretacao_colesterol_obs(self):
        self._set_result('EDH20', 'EDH20-04-08', self.EDH20_interpretacao_colesterol_obs)

    def _default_EDH20_obs(self):
        return self._get_default('EDH20', 'EDH20-05-01')
    EDH20_obs = fields.Char(
        'Observações', readonly=False, default=_default_EDH20_obs
    )

    def _write_EDH20_obs(self):
        self._set_result('EDH20', 'EDH20-05-01', self.EDH20_obs)

    def do_result_updt_EDH20(self):

        self._write_EDH20_tempo_jejum()
        self._write_EDH20_peso()
        self._write_EDH20_peso_resp()
        self._write_EDH20_altura()
        self._write_EDH20_altura_resp()
        self._write_EDH20_imc()
        self._write_EDH20_imc_resp()
        self._write_EDH20_interpretacao_imc()
        self._write_EDH20_interpretacao_imc_obs()
        self._write_EDH20_circ_abdominal()
        self._write_EDH20_circ_abdominal_resp()
        self._write_EDH20_interpretacao_circ_abdominal()
        self._write_EDH20_interpretacao_circ_abdominal_obs()
        self._write_EDH20_pa_automatica()
        self._write_EDH20_pa_automatica_resp()
        self._write_EDH20_pa_manual()
        self._write_EDH20_pa_manual_resp()
        self._write_EDH20_interpretacao_pa()
        self._write_EDH20_pa()
        self._write_EDH20_PAS()
        self._write_EDH20_PAD()
        self._write_EDH20_interpretacao_pa_obs()
        self._write_EDH20_glicemia()
        self._write_EDH20_glicemia_resp()
        self._write_EDH20_interpretacao_glicemia()
        self._write_EDH20_interpretacao_glicemia_obs()
        self._write_EDH20_colesterol()
        self._write_EDH20_colesterol_resp()
        self._write_EDH20_interpretacao_colesterol()
        self._write_EDH20_interpretacao_colesterol_obs()
        self._write_EDH20_obs()

        return True

    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
        return action

    @api.multi
    def do_result_updt(self):
        self.ensure_one()

        result = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))

        _logger.info(u'%s %s', '>>>>>', result.code)

        return True
