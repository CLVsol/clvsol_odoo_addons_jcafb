# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class LabTestResultCopyToReportEDH20(models.TransientModel):
    _description = 'Lab Test Result Copy to Report (EDH20)'
    _name = 'clv.lab_test.result.copy_to_report_edh20'

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

    def _copy_result(self, lab_test_type_id_code, criterion_code, result):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id')).lab_test_report_id
        if active_id.lab_test_type_id.code == lab_test_type_id_code:
            criterion_reg = active_id.criterion_ids.search([
                ('lab_test_report_id', '=', active_id.id),
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

    def _default_is_EDH20(self):
        active_id = self.env['clv.lab_test.report'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EDH20':
            is_EDH20 = True
        else:
            is_EDH20 = False
        return is_EDH20
    is_EDH20 = fields.Boolean('Is EDH20', readonly=True, default=_default_is_EDH20)

    def _default_EDH20_peso(self):
        return self._get_default('EDH20', 'EDH20-02-01')
    EDH20_peso = fields.Char(
        'Peso', readonly=False, default=_default_EDH20_peso
    )

    def _write_EDH20_peso(self):
        self._set_result('EDH20', 'EDH20-02-01', self.EDH20_peso)
        self._copy_result('EDH20', 'EDH20-02-01', self.EDH20_peso)

    def _default_EDH20_altura(self):
        return self._get_default('EDH20', 'EDH20-02-03')
    EDH20_altura = fields.Char(
        'Altura', readonly=False, default=_default_EDH20_altura
    )

    def _write_EDH20_altura(self):
        self._set_result('EDH20', 'EDH20-02-03', self.EDH20_altura)
        self._copy_result('EDH20', 'EDH20-02-03', self.EDH20_altura)

    def _default_EDH20_circ_abdominal(self):
        return self._get_default('EDH20', 'EDH20-02-09')
    EDH20_circ_abdominal = fields.Char(
        'Circunferência abdominal', readonly=False, default=_default_EDH20_circ_abdominal
    )

    def _write_EDH20_circ_abdominal(self):
        self._set_result('EDH20', 'EDH20-02-09', self.EDH20_circ_abdominal)
        self._copy_result('EDH20', 'EDH20-02-09', self.EDH20_circ_abdominal)

    def _default_EDH20_pa(self):
        return self._get_default('EDH20', 'EDH20-03-05')
    EDH20_pa = fields.Char(
        'Pressão arterial', readonly=False, default=_default_EDH20_pa
    )

    def _write_EDH20_pa(self):
        self._set_result('EDH20', 'EDH20-03-05', self.EDH20_pa)
        self._copy_result('EDH20', 'EDH20-03-05', self.EDH20_pa)

    def _default_EDH20_PAS(self):
        return self._get_default('EDH20', 'EDH20-03-06')
    EDH20_PAS = fields.Char(
        'PAS', readonly=False, default=_default_EDH20_PAS
    )

    def _write_EDH20_PAS(self):
        self._set_result('EDH20', 'EDH20-03-06', self.EDH20_PAS)
        self._copy_result('EDH20', 'EDH20-03-06', self.EDH20_PAS)

    def _default_EDH20_PAD(self):
        return self._get_default('EDH20', 'EDH20-03-07')
    EDH20_PAD = fields.Char(
        'PAD', readonly=False, default=_default_EDH20_PAD
    )

    def _write_EDH20_PAD(self):
        self._set_result('EDH20', 'EDH20-03-07', self.EDH20_PAD)
        self._copy_result('EDH20', 'EDH20-03-07', self.EDH20_PAD)

    def _default_EDH20_glicemia(self):
        return self._get_default('EDH20', 'EDH20-04-01')
    EDH20_glicemia = fields.Char(
        'Glicemia', readonly=False, default=_default_EDH20_glicemia
    )

    def _write_EDH20_glicemia(self):
        self._set_result('EDH20', 'EDH20-04-01', self.EDH20_glicemia)
        self._copy_result('EDH20', 'EDH20-04-01', self.EDH20_glicemia)

    def _default_EDH20_colesterol(self):
        return self._get_default('EDH20', 'EDH20-04-05')
    EDH20_colesterol = fields.Char(
        'Colesterol', readonly=False, default=_default_EDH20_colesterol
    )

    def _write_EDH20_colesterol(self):
        self._set_result('EDH20', 'EDH20-04-05', self.EDH20_colesterol)
        self._copy_result('EDH20', 'EDH20-04-05', self.EDH20_colesterol)

    def _default_EDH20_obs(self):
        return self._get_default('EDH20', 'EDH20-05-01')
    EDH20_obs = fields.Char(
        'Observações', readonly=False, default=_default_EDH20_obs
    )

    def _write_EDH20_obs(self):
        self._set_result('EDH20', 'EDH20-05-01', self.EDH20_obs)
        self._copy_result('EDH20', 'EDH20-05-01', self.EDH20_obs)

    def do_result_copy_to_report_EDH20(self):

        self._write_EDH20_peso()
        self._write_EDH20_altura()
        self._write_EDH20_circ_abdominal()
        self._write_EDH20_pa()
        self._write_EDH20_PAS()
        self._write_EDH20_PAD()
        self._write_EDH20_glicemia()
        self._write_EDH20_colesterol()
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
    def do_result_copy_to_report(self):
        self.ensure_one()

        result = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))

        _logger.info(u'%s %s', '>>>>>', result.code)

        return True
