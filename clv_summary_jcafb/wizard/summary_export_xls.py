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

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class SummaryExportXLS(models.TransientModel):
    _name = 'clv.summary.export_xls'

    def _default_summary_ids(self):
        return self._context.get('active_ids')
    summary_ids = fields.Many2many(
        comodel_name='clv.summary',
        relation='clv_summary_export_xls_rel',
        string='Summaries',
        default=_default_summary_ids
    )

    dir_path = fields.Char(
        string='Directory Path',
        required=True,
        help="Directory Path",
        default='/opt/openerp/clvsol_clvhealth_jcafb/summary_files/xls'
    )

    file_name = fields.Char(
        string='File Name',
        required=True,
        help="File Name",
        default='<category>_<code>.xls'
    )

    @api.multi
    def do_summary_export_xls(self):
        self.ensure_one()

        for summary_reg in self.summary_ids:

            if summary_reg.is_address_summary:
                category = 'Address'
                code = summary_reg.address_code
            elif summary_reg.is_person_summary:
                category = 'Person'
                code = summary_reg.person_code
            else:
                break

            file_path = self.dir_path + '/' + \
                self.file_name.replace('<category>', category).replace('<code>', code)

            _logger.info(u'%s %s', '>>>>>', file_path)

            summary_reg.summary_export_xls(file_path)

        return True
