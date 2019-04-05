# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import os
import datetime

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


def modification_date(filepath):
    t = os.path.getmtime(filepath)
    return datetime.datetime.fromtimestamp(t)


class MfileFileSearch(models.TransientModel):
    _description = 'Media File - File Search'
    _name = 'clv.mfile.file_search'

    def _default_mfile_ids(self):
        return self._context.get('active_ids')
    mfile_ids = fields.Many2many(
        comodel_name='clv.mfile',
        relation='clv_mfile_mfile_file_search_rel',
        string='Documents',
        default=_default_mfile_ids
    )

    dir_path = fields.Char(
        'Directory Path',
        required=True,
        help="Directory Path",
        default='/opt/odoo/clvsol_filestore/clvhealth_jcafb/survey_files/archive'
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
    def do_mfile_file_search(self):
        self.ensure_one()

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', self.dir_path),
        ])

        # SurveyQuestion = self.env['survey.question']

        listdir = os.listdir(self.dir_path)

        for mfile in self.mfile_ids:

            _logger.info(u'%s %s (%s)', '>>>>>', mfile.name, mfile.state)

            if mfile.name in listdir and \
               mfile.state in ['archived']:

                filepath = self.dir_path + '/' + mfile.name
                _logger.info(u'%s %s', '>>>>>>>>>>', filepath)

                values = {}
                values['directory_id'] = file_system_directory.id
                values['file_name'] = mfile.name
                values['stored_file_name'] = mfile.name
                mfile.write(values)

        return True

    @api.multi
    def do_populate_all_mfiles(self):
        self.ensure_one()

        Mfile = self.env['clv.mfile']
        mfiles = Mfile.search([])

        self.mfile_ids = mfiles

        return self._reopen_form()
