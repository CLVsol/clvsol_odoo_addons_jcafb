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
from datetime import datetime

from odoo import models

_logger = logging.getLogger(__name__)


class LabTestReport(models.Model):
    _name = "clv.lab_test.report"
    _inherit = 'clv.lab_test.report'

    def lab_test_report_export_xls_EUR18(self, sheet, row_nr, logo_file_path, use_template):

        ExportXLS = self.env['clv.export_xls']

        # lab_test_type = self.lab_test_type_id.code
        lab_test_request_code = self.lab_test_request_id.code
        # lab_test_result_code = self.code

        sheet.header_str = ''
        sheet.footer_str = ''

        for i in range(0, 49):
            sheet.col(i).width = 256 * 2
        sheet.show_grid = False

        # row_nr += 2

        sheet.insert_bitmap(logo_file_path, row_nr, 3)

        ExportXLS.setOutCell(sheet, 13, row_nr, u'Jornada Científica dos Acadêmicos de Farmácia-Bioquímica')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 19, row_nr, u'JCAFB-2018 - FERNÃO - SP')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 17, row_nr,
                             u'Centro Acadêmico de Farmácia-Bioquímica')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 18, row_nr,
                             u'Faculdade de Ciências Farmacêuticas')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Universidade de São Paulo')
        row_nr += 3

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Nome:')
        ExportXLS.setOutCell(sheet, 4, row_nr, self.person_id.name)
        ExportXLS.setOutCell(sheet, 30, row_nr, u'Cadastro:')
        ExportXLS.setOutCell(sheet, 35, row_nr, self.person_id.code)
        row_nr += 2

        ExportXLS.setOutCell(sheet, 0, row_nr, u'Data do Exame:')
        if self.date_approved is not False:
            date = datetime.strptime(self.date_approved, '%Y-%m-%d')
            date = datetime.strftime(date, '%d-%m-%Y')
            ExportXLS.setOutCell(sheet, 8, row_nr, date)
        else:
            ExportXLS.setOutCell(sheet, 8, row_nr, None)
        ExportXLS.setOutCell(sheet, 30, row_nr, u'Código do Exame:')
        ExportXLS.setOutCell(sheet, 38, row_nr, lab_test_request_code)
        row_nr += 3

        ExportXLS.setOutCell(sheet, 20, row_nr, u'URINA TIPO I')
        row_nr += 2

        ExportXLS.setOutCell(sheet, 10, row_nr, u'Resultados')
        # ExportXLS.setOutCell(sheet, 18, row_nr, u'Unidade')
        ExportXLS.setOutCell(sheet, 28, row_nr, u'Valores de Referência')
        row_nr += 1

        ExportXLS.setOutCell(sheet, 4, row_nr, u'Exame Físico')
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-02-01'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Volume:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-02-02'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Densidade:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-02-03'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Aspecto:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-02-04'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Cor:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-02-05'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Odor:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 2

        ExportXLS.setOutCell(sheet, 4, row_nr, u'Exame Químico (Tiras Reagentes)')
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-03-01'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'pH:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-03-02'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Proteínas:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-03-03'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Glicose:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-03-04'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Cetona:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-03-05'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Pigmentos biliares:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-03-06'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Sangue:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-03-07'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Urobilinogênio:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-03-08'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Nitrito:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 2

        ExportXLS.setOutCell(sheet, 4, row_nr, u'Exame Microscópico')
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-01'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Células epiteliais:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-02'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Muco (filamentos):')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-03'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Cristais:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 3

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-04'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Leucócitos:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-05'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Hemácias:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-06'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Cilindros:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-07'),
        ])
        ExportXLS.setOutCell(sheet, 5, row_nr, u'Hialinos:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-08'),
        ])
        ExportXLS.setOutCell(sheet, 5, row_nr, u'Granulosos:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-09'),
        ])
        ExportXLS.setOutCell(sheet, 5, row_nr, u'Leucocitários:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-10'),
        ])
        ExportXLS.setOutCell(sheet, 5, row_nr, u'Hemáticos:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-11'),
        ])
        ExportXLS.setOutCell(sheet, 5, row_nr, u'Céreos:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 1

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-04-12'),
        ])
        ExportXLS.setOutCell(sheet, 5, row_nr, u'Outros:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, criterion.result)
        if criterion.unit_id.name is not False:
            ExportXLS.setOutCell(sheet, 21, row_nr, criterion.unit_id.name)
        if criterion.normal_range is not False:
            ExportXLS.setOutCell(sheet, 28, row_nr, criterion.normal_range)
        row_nr += 2

        criterion = self.criterion_ids.search([
            ('lab_test_report_id', '=', self.id),
            ('code', '=', 'EUR18-05-01'),
        ])
        ExportXLS.setOutCell(sheet, 4, row_nr, u'Observações:')
        if criterion.result is not False:
            ExportXLS.setOutCell(sheet, 8, row_nr, criterion.result)
        row_nr += 6

        ExportXLS.setOutCell(sheet, 17, row_nr, u'Farmacêutico(a) Responsável:')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 33, row_nr, self.employee_id.name)
        row_nr += 1
        ExportXLS.setOutCell(sheet, 36, row_nr, self.employee_id.professional_id)

        return True
