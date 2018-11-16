# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestReportEdit(models.TransientModel):
    _inherit = 'clv.lab_test.report.edit'

    #
    # EDH19
    #

    def _default_is_EDH19(self):
        active_id = self.env['clv.lab_test.report'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EDH19':
            is_EDH19 = True
        else:
            is_EDH19 = False
        return is_EDH19
    is_EDH19 = fields.Boolean('Is EDH19', readonly=True, default=_default_is_EDH19)

    def _default_EDH19_peso(self):
        return self._get_default('EDH19', 'EDH19-02-01')
    EDH19_peso = fields.Char(
        'Peso', readonly=False, default=_default_EDH19_peso
    )

    def _write_EDH19_peso(self):
        self._set_result('EDH19', 'EDH19-02-01', self.EDH19_peso)

    def _default_EDH19_altura(self):
        return self._get_default('EDH19', 'EDH19-02-03')
    EDH19_altura = fields.Char(
        'Altura', readonly=False, default=_default_EDH19_altura
    )

    def _write_EDH19_altura(self):
        self._set_result('EDH19', 'EDH19-02-03', self.EDH19_altura)

    def _default_EDH19_circ_abdominal(self):
        return self._get_default('EDH19', 'EDH19-02-09')
    EDH19_circ_abdominal = fields.Char(
        'Circunferência abdominal', readonly=False, default=_default_EDH19_circ_abdominal
    )

    def _write_EDH19_circ_abdominal(self):
        self._set_result('EDH19', 'EDH19-02-09', self.EDH19_circ_abdominal)

    def _default_EDH19_pa(self):
        return self._get_default('EDH19', 'EDH19-03-05')
    EDH19_pa = fields.Char(
        'Pressão arterial', readonly=False, default=_default_EDH19_pa
    )

    def _write_EDH19_pa(self):
        self._set_result('EDH19', 'EDH19-03-05', self.EDH19_pa)

    def _default_EDH19_PAS(self):
        return self._get_default('EDH19', 'EDH19-03-06')
    EDH19_PAS = fields.Char(
        'PAS', readonly=False, default=_default_EDH19_PAS
    )

    def _write_EDH19_PAS(self):
        self._set_result('EDH19', 'EDH19-03-06', self.EDH19_PAS)

    def _default_EDH19_PAD(self):
        return self._get_default('EDH19', 'EDH19-03-07')
    EDH19_PAD = fields.Char(
        'PAD', readonly=False, default=_default_EDH19_PAD
    )

    def _write_EDH19_PAD(self):
        self._set_result('EDH19', 'EDH19-03-07', self.EDH19_PAD)

    def _default_EDH19_glicemia(self):
        return self._get_default('EDH19', 'EDH19-04-01')
    EDH19_glicemia = fields.Char(
        'Glicemia', readonly=False, default=_default_EDH19_glicemia
    )

    def _write_EDH19_glicemia(self):
        self._set_result('EDH19', 'EDH19-04-01', self.EDH19_glicemia)

    def _default_EDH19_colesterol(self):
        return self._get_default('EDH19', 'EDH19-04-05')
    EDH19_colesterol = fields.Char(
        'Colesterol', readonly=False, default=_default_EDH19_colesterol
    )

    def _write_EDH19_colesterol(self):
        self._set_result('EDH19', 'EDH19-04-05', self.EDH19_colesterol)

    def _default_EDH19_obs(self):
        return self._get_default('EDH19', 'EDH19-05-01')
    EDH19_obs = fields.Char(
        'Observações', readonly=False, default=_default_EDH19_obs
    )

    def _write_EDH19_obs(self):
        self._set_result('EDH19', 'EDH19-05-01', self.EDH19_obs)

    def _do_report_updt_EDH19(self):

        self._write_EDH19_peso()
        self._write_EDH19_altura()
        self._write_EDH19_circ_abdominal()
        self._write_EDH19_pa()
        self._write_EDH19_PAS()
        self._write_EDH19_PAD()
        self._write_EDH19_glicemia()
        self._write_EDH19_colesterol()
        self._write_EDH19_obs()

        return True
