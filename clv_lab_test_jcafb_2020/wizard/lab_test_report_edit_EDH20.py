# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestReportEdit(models.TransientModel):
    _inherit = 'clv.lab_test.report.edit'

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

    def _default_EDH20_altura(self):
        return self._get_default('EDH20', 'EDH20-02-03')
    EDH20_altura = fields.Char(
        'Altura', readonly=False, default=_default_EDH20_altura
    )

    def _write_EDH20_altura(self):
        self._set_result('EDH20', 'EDH20-02-03', self.EDH20_altura)

    def _default_EDH20_circ_abdominal(self):
        return self._get_default('EDH20', 'EDH20-02-09')
    EDH20_circ_abdominal = fields.Char(
        'Circunferência abdominal', readonly=False, default=_default_EDH20_circ_abdominal
    )

    def _write_EDH20_circ_abdominal(self):
        self._set_result('EDH20', 'EDH20-02-09', self.EDH20_circ_abdominal)

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

    def _default_EDH20_glicemia(self):
        return self._get_default('EDH20', 'EDH20-04-01')
    EDH20_glicemia = fields.Char(
        'Glicemia', readonly=False, default=_default_EDH20_glicemia
    )

    def _write_EDH20_glicemia(self):
        self._set_result('EDH20', 'EDH20-04-01', self.EDH20_glicemia)

    def _default_EDH20_colesterol(self):
        return self._get_default('EDH20', 'EDH20-04-05')
    EDH20_colesterol = fields.Char(
        'Colesterol', readonly=False, default=_default_EDH20_colesterol
    )

    def _write_EDH20_colesterol(self):
        self._set_result('EDH20', 'EDH20-04-05', self.EDH20_colesterol)

    def _default_EDH20_obs(self):
        return self._get_default('EDH20', 'EDH20-05-01')
    EDH20_obs = fields.Char(
        'Observações', readonly=False, default=_default_EDH20_obs
    )

    def _write_EDH20_obs(self):
        self._set_result('EDH20', 'EDH20-05-01', self.EDH20_obs)

    def _do_report_updt_EDH20(self):

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
