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
from datetime import datetime

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class SummaryRefresh(models.TransientModel):
    _name = 'clv.summary.refresh'

    def _default_summary_ids(self):
        return self._context.get('active_ids')
    summary_ids = fields.Many2many(
        comodel_name='clv.summary',
        relation='clv_summary_refresh_rel',
        string='Summaries',
        default=_default_summary_ids
    )

    def _default_dir_path(self):
        Summary = self.env['clv.summary']
        return Summary.summary_export_xls_dir_path()
    dir_path = fields.Char(
        string='Directory Path',
        required=True,
        help="Directory Path",
        default=_default_dir_path
    )

    def _default_file_name(self):
        Summary = self.env['clv.summary']
        return Summary.summary_export_xls_file_name()
    file_name = fields.Char(
        string='File Name',
        required=True,
        help="File Name",
        default=_default_file_name
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
    def do_summary_refresh(self):
        self.ensure_one()

        for summary in self.summary_ids:

            _logger.info(u'%s %s', '>>>>>', summary.name)

            if summary.is_address_summary:

                _logger.info(u'%s %s', '>>>>>>>>>>', 'is_address_summary')

                summary.addres_id.address_summary_setup(self.dir_path, self.file_name)

            elif summary.is_person_summary:

                _logger.info(u'%s %s', '>>>>>>>>>>', 'is_person_summary')

                summary.person_id.person_summary_setup(self.dir_path, self.file_name)

        return True

    @api.multi
    def do_populate_all_summaries(self):
        self.ensure_one()

        Summary = self.env['clv.summary']
        summaries = Summary.search([])

        self.summary_ids = summaries

        return self._reopen_form()
