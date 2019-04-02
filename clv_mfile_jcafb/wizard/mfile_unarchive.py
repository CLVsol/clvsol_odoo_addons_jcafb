# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import shutil

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MfileUnarchive(models.TransientModel):
    _name = 'clv.mfile.unarchive'

    def _default_mfile_ids(self):
        return self._context.get('active_ids')
    mfile_ids = fields.Many2many(
        comodel_name='clv.mfile',
        relation='clv_mfile_mfile_unarchive_rel',
        string='Media Files',
        default=_default_mfile_ids
    )

    dir_path = fields.Char(
        'Directory Path (Input)',
        required=True,
        help="Input Directory Path",
        default='/opt/openerp/clvsol_clvhealth_jcafb/survey_files/input'
    )

    archive_dir_path = fields.Char(
        'Directory Path (Archive)',
        required=True,
        help="Archive Directory Path",
        default='/opt/openerp/clvsol_clvhealth_jcafb/survey_files/archive'
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
    def do_mfile_unarchive(self):
        self.ensure_one()

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', self.dir_path),
        ])

        for mfile in self.mfile_ids:

            filepath = self.dir_path + '/' + mfile.name
            archive_filepath = self.archive_dir_path + '/' + mfile.name

            _logger.info(u'%s %s', '>>>>>', mfile.name)

            if mfile.state == 'archived':

                shutil.move(archive_filepath, filepath)

                mfile.directory_id = file_system_directory.id
                mfile.file_name = mfile.name
                mfile.stored_file_name = mfile.name

                mfile.state = 'imported'

        return True
