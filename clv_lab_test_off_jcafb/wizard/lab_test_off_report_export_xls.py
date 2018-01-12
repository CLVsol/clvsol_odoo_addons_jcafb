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


class LabTestOffReportExportXLS(models.TransientModel):
    _name = 'clv.lab_test.off.report.export_xls'

    def _default_lab_test_off_report_ids(self):
        return self._context.get('active_ids')
    lab_test_off_report_ids = fields.Many2many(
        comodel_name='clv.lab_test.off.report',
        relation='clv_lab_test_off_report_export_xls_rel',
        string='Lab Test (off) Reports',
        default=_default_lab_test_off_report_ids
    )

    def _default_dir_path(self):
        LabTestReport = self.env['clv.lab_test.report']
        return LabTestReport.lab_test_report_export_xls_dir_path()
    dir_path = fields.Char(
        string='Directory Path',
        required=True,
        help="Directory Path",
        default=_default_dir_path
    )

    def _default_file_name(self):
        LabTestReport = self.env['clv.lab_test.report']
        return LabTestReport.lab_test_report_export_xls_file_name()
    file_name = fields.Char(
        string='File Name',
        required=True,
        help="File Name",
        default=_default_file_name
    )

    use_template = fields.Boolean(string='Use Template', default=True)

    def _default_templates_dir_path(self):
        LabTestReport = self.env['clv.lab_test.report']
        return LabTestReport.lab_test_report_export_templates_dir_path()
    templates_dir_path = fields.Char(
        string='Template Directory Path',
        required=True,
        help="Template Directory Path",
        default=_default_templates_dir_path
    )

    @api.multi
    def do_lab_test_off_report_export_xls(self):
        self.ensure_one()

        for lab_test_off_report_reg in self.lab_test_off_report_ids:

            _logger.info(u'%s %s', '>>>>>', lab_test_off_report_reg.code)

            lab_test_off_report_reg.lab_test_off_report_export_xls(self.dir_path, self.file_name,
                                                                   self.use_template, self.templates_dir_path)

        return True
