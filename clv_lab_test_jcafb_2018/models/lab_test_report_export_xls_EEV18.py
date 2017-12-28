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


class LabTestReport(models.Model):
    _name = "clv.lab_test.report"
    _inherit = 'clv.lab_test.report'

    def lab_test_report_export_xls_EEV18(self, sheet, row_nr):

        ExportXLS = self.env['clv.export_xls']

        # lab_test_type = self.lab_test_type_id.code
        lab_test_request_code = self.lab_test_request_id.code
        # lab_test_result_code = self.code

        ExportXLS.setOutCell(sheet, 17, row_nr, u'Jornada Científica dos Acadêmicos de Farmácia-Bioquímica')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 23, row_nr, u'JCAFB-2018 - FERNÃO - SP')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 12, row_nr,
                             u'Faculdade de Ciências Farmacêuticas - Centro Acadêmico de Farmácia-Bioquímica')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 23, row_nr, u'Universidade dde São Paulo')
        row_nr += 2

        # ExportXLS.setOutCell(sheet, 0, row_nr, u'Código da Requisição:')
        # ExportXLS.setOutCell(sheet, 10, row_nr, lab_test_request_code)
        # ExportXLS.setOutCell(sheet, 25, row_nr, u'Código do Resultado:')
        # ExportXLS.setOutCell(sheet, 35, row_nr, lab_test_result_code)
        # row_nr += 1

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Nome:')
        ExportXLS.setOutCell(sheet, 4, row_nr, self.person_id.name)
        # row_nr += 1
        ExportXLS.setOutCell(sheet, 30, row_nr, u'Cadastro:')
        ExportXLS.setOutCell(sheet, 35, row_nr, self.person_id.code)
        row_nr += 2

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Data do Exame:')
        ExportXLS.setOutCell(sheet, 8, row_nr, self.date_approved)
        # row_nr += 1
        ExportXLS.setOutCell(sheet, 30, row_nr, u'Código do Exame:')
        ExportXLS.setOutCell(sheet, 38, row_nr, lab_test_request_code)
        row_nr += 2

        ExportXLS.setOutCell(sheet, 15, row_nr, u'PESQUISA DE Enterobius vermicularis')
        row_nr += 5

        result = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EEV18-01-03'),
        ]).result
        ExportXLS.setOutCell(sheet, 18, row_nr, u'Resultado:')
        ExportXLS.setOutCell(sheet, 23, row_nr, result)
        row_nr += 5

        result = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EEV18-01-05'),
        ]).result
        ExportXLS.setOutCell(sheet, 0, row_nr, u'Métodos utilizados:')
        ExportXLS.setOutCell(sheet, 10, row_nr, result)
        row_nr += 1

        result = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EEV18-01-03'),
        ]).normal_range
        ExportXLS.setOutCell(sheet, 0, row_nr, u'Valor de referência:')
        ExportXLS.setOutCell(sheet, 10, row_nr, result)
        row_nr += 2

        result = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EEV18-01-06'),
        ]).result
        ExportXLS.setOutCell(sheet, 0, row_nr, u'Observações:')
        ExportXLS.setOutCell(sheet, 7, row_nr, result)
        row_nr += 5

        ExportXLS.setOutCell(sheet, 10, row_nr, u'Farmacêutico(a) Responsável:')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 25, row_nr, self.employee_id.name)
        row_nr += 1
        ExportXLS.setOutCell(sheet, 25, row_nr, self.employee_id.professional_id)

        for i in range(0, 49):
            sheet.col(i).width = 256 * 2
        sheet.show_grid = False

        return True
