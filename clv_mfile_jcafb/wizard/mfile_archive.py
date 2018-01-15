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
import shutil

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MfileArchive(models.TransientModel):
    _name = 'clv.mfile.archive'

    def _default_mfile_ids(self):
        return self._context.get('active_ids')
    mfile_ids = fields.Many2many(
        comodel_name='clv.mfile',
        relation='clv_mfile_mfile_archive_rel',
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
    def do_mfile_archive(self):
        self.ensure_one()

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', self.archive_dir_path),
        ])

        for mfile in self.mfile_ids:

            filepath = self.dir_path + '/' + mfile.name
            archive_filepath = self.archive_dir_path + '/' + mfile.name

            _logger.info(u'%s %s', '>>>>>', mfile.name)

            if mfile.state == 'imported':

                shutil.move(filepath, archive_filepath)

                mfile.directory_id = file_system_directory.id
                mfile.file_name = mfile.name
                mfile.stored_file_name = mfile.name

                mfile.state = 'archived'

        return True
