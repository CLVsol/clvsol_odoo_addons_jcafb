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
import os
import datetime
import xlrd

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


def modification_date(filepath):
    t = os.path.getmtime(filepath)
    return datetime.datetime.fromtimestamp(t)


class MfileRefresh(models.TransientModel):
    _name = 'clv.mfile.refresh'

    def _default_mfile_ids(self):
        return self._context.get('active_ids')
    mfile_ids = fields.Many2many(
        comodel_name='clv.mfile',
        relation='clv_mfile_mfile_refresh_rel',
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
    def do_mfile_refresh(self):
        self.ensure_one()

        listdir = os.listdir(self.dir_path)

        for mfile in self.mfile_ids:

            _logger.info(u'%s %s', '>>>>>', mfile.name)

            if mfile.name in listdir:

                filepath = self.dir_path + '/' + mfile.name
                _logger.info(u'%s %s', '>>>>>>>>>>', filepath)

                if mfile.state in ['new', 'returned', 'checked', 'validated']:

                    mfile.state = 'checked'
                    mfile.document_code = False
                    mfile.person_code = False
                    mfile.address_code = False
                    mfile.notes = False

                    book = xlrd.open_workbook(filepath)
                    sheet = book.sheet_by_index(0)
                    survey_title = sheet.cell_value(0, 0)

                    mfile.date_survey_file = modification_date(filepath)

                    mfile.survey_title = survey_title
                    if mfile.document_id.survey_id.title != survey_title:
                        mfile.state = 'returned'
                        if mfile.notes is False:
                            mfile.notes = u'Erro: Tipo de Questionário inconsistente com o Documento!'
                        else:
                            mfile.notes += u'\nErro: Tipo de Questionário inconsistente com o Documento!'

                    document_code = False
                    person_code = False
                    address_code = False

                    for i in range(sheet.nrows):

                        code_row = sheet.cell_value(i, 0)

                        if code_row == '[]':
                            code_cols = {}
                            for k in range(sheet.ncols):
                                code_col = sheet.cell_value(i, k)
                                if code_col != xlrd.empty_cell.value:
                                    code_cols.update({k: code_col})

                        for j in range(sheet.ncols):

                            if sheet.cell_value(i, j) != xlrd.empty_cell.value:

                                if sheet.cell_value(i, j) == '.':
                                    try:
                                        value = sheet.cell_value(i, j + 1)
                                    except Exception:
                                        value = xlrd.empty_cell.value
                                    if value != xlrd.empty_cell.value:
                                        if survey_title == '[QAN17]' and code_row == '[QAN17_01_01]' or \
                                           survey_title == '[QDH17]' and code_row == '[QDH17_01_01]' or \
                                           survey_title == '[QMD17]' and code_row == '[QMD17_01_01]' or \
                                           survey_title == '[QSC17]' and code_row == '[QSC17_01_01]' or \
                                           survey_title == '[QSF17]' and code_row == '[QSF17_01_01]' or \
                                           survey_title == '[QSI17]' and code_row == '[QSI17_01_01]' or \
                                           survey_title == '[TCP17]' and code_row == '[TCP17_01_01]' or \
                                           survey_title == '[TCR17]' and code_row == '[TCR17_01_01]' or \
                                           survey_title == '[TID17]' and code_row == '[TID17_01_01]':
                                            document_code = value

                                        if survey_title == '[QAN17]' and code_row == '[QAN17_02_02]' or \
                                           survey_title == '[QDH17]' and code_row == '[QDH17_02_02]' or \
                                           survey_title == '[QMD17]' and code_row == '[QMD17_02_02]' or \
                                           survey_title == '[QSC17]' and code_row == '[QSC17_02_02]' or \
                                           survey_title == '[QSI17]' and code_row == '[QSI17_02_02]' or \
                                           survey_title == '[TCP17]' and code_row == '[TCP17_02_02]' or \
                                           survey_title == '[TCR17]' and code_row == '[TCR17_02_02]' or \
                                           survey_title == '[TID17]' and code_row == '[TID17_02_02]':
                                            person_code = value

                                        if survey_title == '[QAN17]' and code_row == '[QAN17_02_05]' or \
                                           survey_title == '[QDH17]' and code_row == '[QDH17_02_05]' or \
                                           survey_title == '[QMD17]' and code_row == '[QMD17_02_05]' or \
                                           survey_title == '[QSC17]' and code_row == '[QSC17_02_05]' or \
                                           survey_title == '[QSF17]' and code_row == '[QSF17_02_02]' or \
                                           survey_title == '[QSI17]' and code_row == '[QSI17_02_05]':
                                            address_code = value

                    mfile.document_code = document_code
                    if mfile.document_id.code != document_code:
                        mfile.state = 'returned'
                        if mfile.notes is False:
                            mfile.notes = u'Erro: Código do Documento inválido!'
                        else:
                            mfile.notes += u'\nErro: Código do Documento inválido!'

                    mfile.person_code = person_code
                    if mfile.person_id.code != person_code and \
                       survey_title != '[QSF17]':
                        mfile.state = 'returned'
                        if mfile.notes is False:
                            mfile.notes = u'Erro: Código da Pessoa inválido!'
                        else:
                            mfile.notes += u'\nErro: Código da Pessoa inválido!'

                    mfile.address_code = address_code
                    if mfile.address_id.code != address_code and \
                       survey_title == '[QSF17]':
                        mfile.state = 'returned'
                        if mfile.notes is False:
                            mfile.notes = u'Erro: Código do Endereço inválido!'
                        else:
                            mfile.notes += u'\nErro: Código do Endereço inválido!'

            else:

                if mfile.state in ['new', 'returned', 'checked', 'validated']:

                    mfile.state = 'new'
                    mfile.document_code = False
                    mfile.person_code = False
                    mfile.address_code = False
                    mfile.notes = False

        return True
