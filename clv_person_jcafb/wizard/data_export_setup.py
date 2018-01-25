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
from datetime import *
import xlwt

from odoo import api, models

_logger = logging.getLogger(__name__)


class DataExportSetUp(models.TransientModel):
    _inherit = 'clv.data_export.setup'

    @api.multi
    def do_data_export_setup(self):
        self.ensure_one()

        category = 'Person'

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', self.dir_path),
        ])

        for data_export in self.data_export_ids:

            _logger.info(u'%s %s', '>>>>>', data_export.name)

            data_export.date_data_export = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            code = data_export.code
            file_name = self.file_name.replace('<category>', category).replace('<code>', code)
            file_path = self.dir_path + '/' + file_name
            _logger.info(u'%s %s', '>>>>>>>>>>', file_path)

            book = xlwt.Workbook()

            sheet = book.add_sheet(file_name)
            row_nr = 0

            row = sheet.row(row_nr)
            col_nr = 0
            for field in data_export.data_export_field_ids:
                row.write(col_nr, field.field_id.field_description)
                col_nr += 1

            for lab_test_criterion in data_export.data_export_lab_test_criterion_ids:
                row.write(col_nr, lab_test_criterion.lab_test_criterion_id.code)
                col_nr += 1

            for document_item in data_export.data_export_document_item_ids:
                row.write(col_nr, document_item.document_item_id.code)
                col_nr += 1

            for item in eval('data_export.' + data_export.model_items):
                row_nr += 1
                row = sheet.row(row_nr)
                col_nr = 0
                for field in data_export.data_export_field_ids:
                    if field.field_id.ttype == 'char':
                        cmd = 'item.' + field.field_id.name
                    if field.field_id.ttype == 'date':
                        cmd = 'item.' + field.field_id.name
                    if field.field_id.ttype == 'many2many':
                        cmd = 'item.' + field.field_id.name + '.name'
                    if field.field_id.ttype == 'many2one':
                        cmd = 'item.' + field.field_id.name + '.name'
                    if field.field_id.ttype == 'selection':
                        cmd = 'item.' + field.field_id.name
                    if eval(cmd) is not False:
                        row.write(col_nr, eval(cmd))
                    col_nr += 1

                for lab_test_criterion in data_export.data_export_lab_test_criterion_ids:
                    result = None
                    for lab_test_result in item.lab_test_result_ids:
                        if lab_test_result.lab_test_type_id.id == \
                           lab_test_criterion.lab_test_criterion_id.lab_test_type_id.id:
                            result = lab_test_result.criterion_ids.search([
                                ('lab_test_result_id', '=', lab_test_result.id),
                                ('code', '=', lab_test_criterion.lab_test_criterion_id.code),
                            ]).result
                            break
                    row.write(col_nr, result)
                    col_nr += 1

                for document_item in data_export.data_export_document_item_ids:
                    value = None
                    for document in item.document_ids:
                        if document.person_id.id is not False:
                            if document.document_type_id.id == \
                               document_item.document_item_id.document_type_id.id:
                                value = document.survey_user_input_id.get_value(document_item.document_item_id.code)
                                break
                    for document in item.address_id.document_ids:
                        if document.address_id.id is not False:
                            if document.document_type_id.id == \
                               document_item.document_item_id.document_type_id.id:
                                value = document.survey_user_input_id.get_value(document_item.document_item_id.code)
                                break
                    row.write(col_nr, value)
                    col_nr += 1

            book.save(file_path)

            data_export.directory_id = file_system_directory.id
            data_export.file_name = file_name
            data_export.stored_file_name = file_name

        return True
