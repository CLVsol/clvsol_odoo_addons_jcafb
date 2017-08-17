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
import xlrd
import datetime

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MfileImport(models.TransientModel):
    _name = 'clv.mfile.import'

    def _default_mfile_ids(self):
        return self._context.get('active_ids')
    mfile_ids = fields.Many2many(
        comodel_name='clv.mfile',
        relation='clv_mfile_mfile_import_rel',
        string='Documents',
        default=_default_mfile_ids
    )

    dir_path = fields.Char(
        'Directory Path',
        required=True,
        help="Directory Path",
        default='/opt/openerp/clvsol_clvhealth_jcafb/survey_files/input'
    )

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
    def do_mfile_import(self):
        self.ensure_one()

        SurveyQuestion = self.env['survey.question']
        SurveyLabel = self.env['survey.label']
        SurveyUserInput = self.env['survey.user_input']
        SurveyUserInputLine = self.env['survey.user_input_line']

        for mfile in self.mfile_ids:

            filepath = self.dir_path + '/' + mfile.name
            _logger.info(u'>>>>> %s', filepath)

            if mfile.state == 'validated':

                book = xlrd.open_workbook(filepath)
                sheet = book.sheet_by_index(0)

                values = {
                    'survey_id': mfile.survey_id.id,
                    'state': 'done',
                }
                survey_user_input = SurveyUserInput.create(values)
                _logger.info(u'>>>>>>>>>> %s', survey_user_input)

                for i in range(sheet.nrows):

                    code_row = sheet.cell_value(i, 0)

                    if code_row == xlrd.empty_cell.value:
                        continue

                    if code_row == '[]':
                        code_cols = {}
                        for k in range(sheet.ncols):
                            code_col = sheet.cell_value(i, k)
                            if code_col != xlrd.empty_cell.value:
                                code_cols.update({k: code_col})

                    row_code = code_row.replace('[', '').replace(']', '')

                    for j in range(sheet.ncols):

                        if sheet.cell_value(i, j) == '.':

                            try:
                                value = sheet.cell_value(i, j + 1)
                            except Exception:
                                value = xlrd.empty_cell.value

                            if value != xlrd.empty_cell.value:

                                question_code = row_code[:11]
                                survey_question_search = SurveyQuestion.search([
                                    ('code', '=', question_code),
                                ])
                                if survey_question_search.id is not False:
                                    question_type = survey_question_search.type
                                    question_matrix_subtype = False
                                    if question_type == 'matrix':
                                        question_matrix_subtype = survey_question_search.matrix_subtype

                                _logger.info(u'>>>>>>>>>> (%s, %s) %s %s %s', i, j + 1,
                                             row_code, question_type, question_matrix_subtype)

                                if survey_question_search.type == 'textbox':

                                    question_code = row_code[:11]
                                    survey_question_search = SurveyQuestion.search([
                                        ('code', '=', question_code),
                                    ])
                                    if survey_question_search.id is not False:
                                        question_parameter = survey_question_search.parameter

                                        if question_parameter == 'date':
                                            date = value
                                            if date != 0:
                                                try:
                                                    datetime.datetime.strptime(value, '%Y-%m-%d')
                                                except Exception:
                                                    date = datetime.datetime(
                                                        *xlrd.xldate_as_tuple(
                                                            date, book.datemode)).strftime('%Y-%m-%d')
                                                    value = date

                                    # print '>>>>>>>>>>>>>>>>>>>>', value
                                    values = {
                                        'survey_id': survey_question_search.survey_id.id,
                                        'question_id': survey_question_search.id,
                                        'user_input_id': survey_user_input.id,
                                        'answer_type': 'text',
                                        'value_text': value,
                                    }
                                    SurveyUserInputLine.create(values)

                                elif survey_question_search.type == 'simple_choice':

                                    if row_code != question_code:
                                        survey_label_code = row_code
                                        survey_label_search = SurveyLabel.search([
                                            ('code', '=', survey_label_code),
                                        ])
                                        if survey_label_search.id is not False:

                                            values = {
                                                'survey_id': survey_question_search.survey_id.id,
                                                'question_id': survey_question_search.id,
                                                'user_input_id': survey_user_input.id,
                                                'answer_type': 'suggestion',
                                                'value_suggested': survey_label_search.id,
                                                'quizz_mark': 0.0
                                            }
                                            SurveyUserInputLine.create(values)

                                    else:
                                        values = {
                                            'survey_id': survey_question_search.survey_id.id,
                                            'question_id': survey_question_search.id,
                                            'user_input_id': survey_user_input.id,
                                            'answer_type': 'text',
                                            'value_text': value,
                                            # 'quizz_mark': 0.0
                                        }
                                        SurveyUserInputLine.create(values)

                                elif survey_question_search.type == 'multiple_choice':

                                    if row_code != question_code:
                                        survey_label_code = row_code
                                        survey_label_search = SurveyLabel.search([
                                            ('code', '=', survey_label_code),
                                        ])
                                        if survey_label_search.id is not False:

                                            values = {
                                                'survey_id': survey_question_search.survey_id.id,
                                                'question_id': survey_question_search.id,
                                                'user_input_id': survey_user_input.id,
                                                'answer_type': 'suggestion',
                                                'value_suggested': survey_label_search.id,
                                                'quizz_mark': 0.0
                                            }
                                            SurveyUserInputLine.create(values)

                                    else:
                                        values = {
                                            'survey_id': survey_question_search.survey_id.id,
                                            'question_id': survey_question_search.id,
                                            'user_input_id': survey_user_input.id,
                                            'answer_type': 'text',
                                            'value_text': value,
                                            # 'quizz_mark': 0.0
                                        }
                                        SurveyUserInputLine.create(values)

                                elif survey_question_search.type == 'matrix':

                                    if survey_question_search.matrix_subtype == 'simple':

                                        col_code = code_cols[j].replace('[', '').replace(']', '')

                                        survey_label_row_search = SurveyLabel.search([
                                            ('code', '=', row_code),
                                        ])
                                        survey_label_col_search = SurveyLabel.search([
                                            ('code', '=', col_code),
                                        ])
                                        if survey_label_row_search.id is not False and\
                                           survey_label_col_search.id is not False:

                                            values = {
                                                'survey_id': survey_question_search.survey_id.id,
                                                'question_id': survey_question_search.id,
                                                'user_input_id': survey_user_input.id,
                                                'answer_type': 'suggestion',
                                                'value_suggested_row': survey_label_row_search.id,
                                                'value_suggested': survey_label_col_search.id,
                                                'quizz_mark': 0.0
                                            }
                                            SurveyUserInputLine.create(values)

                survey_user_input.linked_code = mfile.document_code
                survey_user_input.linked_state = 'linked'
                mfile.state = 'imported'
                mfile.survey_user_input_id = survey_user_input.id
                mfile.document_id.survey_user_input_id = survey_user_input.id
                # mfile.document_id.state = 'done'

        return True

    @api.multi
    def do_populate_all_mfiles(self):
        self.ensure_one()

        Mfile = self.env['clv.mfile']
        mfiles = Mfile.search([])

        self.mfile_ids = mfiles

        return self._reopen_form()
