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


class LabTestOffReportEdit(models.TransientModel):
    _inherit = 'clv.lab_test.off.report.edit'

    #
    # EDH18
    #

    def _default_is_EDH18(self):
        active_id = self.env['clv.lab_test.off.report'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EDH18':
            is_EDH18 = True
        else:
            is_EDH18 = False
        return is_EDH18
    is_EDH18 = fields.Boolean('Is EDH18', readonly=True, default=_default_is_EDH18)

    def _default_EDH18_peso(self):
        return self._get_default('EDH18', 'EDH18-02-01')
    EDH18_peso = fields.Char(
        'Peso', readonly=False, default=_default_EDH18_peso
    )

    def _write_EDH18_peso(self):
        self._set_result('EDH18', 'EDH18-02-01', self.EDH18_peso)

    def _default_EDH18_altura(self):
        return self._get_default('EDH18', 'EDH18-02-03')
    EDH18_altura = fields.Char(
        'Altura', readonly=False, default=_default_EDH18_altura
    )

    def _write_EDH18_altura(self):
        self._set_result('EDH18', 'EDH18-02-03', self.EDH18_altura)

    def _default_EDH18_circ_abdominal(self):
        return self._get_default('EDH18', 'EDH18-02-09')
    EDH18_circ_abdominal = fields.Char(
        'Circunferência abdominal', readonly=False, default=_default_EDH18_circ_abdominal
    )

    def _write_EDH18_circ_abdominal(self):
        self._set_result('EDH18', 'EDH18-02-09', self.EDH18_circ_abdominal)

    def _default_EDH18_pa(self):
        return self._get_default('EDH18', 'EDH18-03-05')
    EDH18_pa = fields.Char(
        'Pressão arterial', readonly=False, default=_default_EDH18_pa
    )

    def _write_EDH18_pa(self):
        self._set_result('EDH18', 'EDH18-03-05', self.EDH18_pa)

    def _default_EDH18_PAS(self):
        return self._get_default('EDH18', 'EDH18-03-06')
    EDH18_PAS = fields.Char(
        'PAS', readonly=False, default=_default_EDH18_PAS
    )

    def _write_EDH18_PAS(self):
        self._set_result('EDH18', 'EDH18-03-06', self.EDH18_PAS)

    def _default_EDH18_PAD(self):
        return self._get_default('EDH18', 'EDH18-03-07')
    EDH18_PAD = fields.Char(
        'PAD', readonly=False, default=_default_EDH18_PAD
    )

    def _write_EDH18_PAD(self):
        self._set_result('EDH18', 'EDH18-03-07', self.EDH18_PAD)

    def _default_EDH18_glicemia(self):
        return self._get_default('EDH18', 'EDH18-04-01')
    EDH18_glicemia = fields.Char(
        'Glicemia', readonly=False, default=_default_EDH18_glicemia
    )

    def _write_EDH18_glicemia(self):
        self._set_result('EDH18', 'EDH18-04-01', self.EDH18_glicemia)

    def _default_EDH18_colesterol(self):
        return self._get_default('EDH18', 'EDH18-04-05')
    EDH18_colesterol = fields.Char(
        'Colesterol', readonly=False, default=_default_EDH18_colesterol
    )

    def _write_EDH18_colesterol(self):
        self._set_result('EDH18', 'EDH18-04-05', self.EDH18_colesterol)

    def _default_EDH18_obs(self):
        return self._get_default('EDH18', 'EDH18-05-01')
    EDH18_obs = fields.Char(
        'Observações', readonly=False, default=_default_EDH18_obs
    )

    def _write_EDH18_obs(self):
        self._set_result('EDH18', 'EDH18-05-01', self.EDH18_obs)

    def _do_report_updt_EDH18(self):

        self._write_EDH18_peso()
        self._write_EDH18_altura()
        self._write_EDH18_circ_abdominal()
        self._write_EDH18_pa()
        self._write_EDH18_PAS()
        self._write_EDH18_PAD()
        self._write_EDH18_glicemia()
        self._write_EDH18_colesterol()
        self._write_EDH18_obs()

        return True
