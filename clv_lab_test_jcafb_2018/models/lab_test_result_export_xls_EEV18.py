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
# import xlwt

from odoo import models

_logger = logging.getLogger(__name__)


class LabTestResult(models.Model):
    _name = "clv.lab_test.result"
    _inherit = 'clv.lab_test.result'

    def lab_test_result_export_xls_EEV18(self, sheet, row_nr):

        ExportXLS = self.env['clv.export_xls']

        lab_test_type = self.lab_test_type_id.code
        lab_test_request_code = self.lab_test_request_id.code
        lab_test_result_code = self.code

        ExportXLS.setOutCell(sheet, 0, row_nr, u'JCAFB-2018 - FERNÃO - SP')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 0, row_nr, lab_test_type + ' - ' +
                             u'PESQUISA DE Enterobius vermicularis - RESULTADO')
        row_nr += 2

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Código da Requisição:')
        ExportXLS.setOutCell(sheet, 10, row_nr, lab_test_request_code)
        ExportXLS.setOutCell(sheet, 25, row_nr, u'Código do Resultado:')
        ExportXLS.setOutCell(sheet, 35, row_nr, lab_test_result_code)
        row_nr += 1

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Nome da Pessoa:')
        ExportXLS.setOutCell(sheet, 10, row_nr, self.person_id.name)
        row_nr += 1
        ExportXLS.setOutCell(sheet, 0, row_nr, u'Código da Pessoa:')
        ExportXLS.setOutCell(sheet, 10, row_nr, self.person_id.code)
        row_nr += 2

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Recebido por:')
        ExportXLS.setOutCell(sheet, 10, row_nr, self.lab_test_request_id.employee_id.name)
        row_nr += 1
        ExportXLS.setOutCell(sheet, 0, row_nr, u'Código do Recebedor:')
        ExportXLS.setOutCell(sheet, 10, row_nr, self.lab_test_request_id.employee_id.code)
        row_nr += 2

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Data do Exame:')
        row_nr += 2

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Método Utilizado: SWAB ANAL')
        row_nr += 2

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Resultado:')
        row_nr += 4

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Analisador(a):')
        row_nr += 2

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Observações:')
        row_nr += 3

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Revisado por:')
        ExportXLS.setOutCell(sheet, 25, row_nr, u'Data:')
        row_nr += 2

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Resultado Confirmado (   )')
        ExportXLS.setOutCell(sheet, 25, row_nr, u'Resultado Alterado (   )')
        row_nr += 2

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Resultado digitado em:')
        ExportXLS.setOutCell(sheet, 25, row_nr, u'Digitado por:')
        row_nr += 2

        for i in range(0, 49):
            sheet.col(i).width = 256 * 2
        sheet.show_grid = False

        return True
