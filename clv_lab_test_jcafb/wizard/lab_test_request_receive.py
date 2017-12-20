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


class LabTestRequestReceive(models.TransientModel):
    _name = 'clv.lab_test.request.receive'

    def _default_lab_test_request_ids(self):
        return self._context.get('active_ids')
    lab_test_request_ids = fields.Many2many(
        comodel_name='clv.lab_test.request',
        relation='clv_lab_test_request_lab_test_request_receive_rel',
        string='Lab Test Requests',
        readonly=True,
        default=_default_lab_test_request_ids
    )

    def _default_employee_id(self):
        HrEmployee = self.env['hr.employee']
        employee = HrEmployee.search([
            ('user_id', '=', self.env.uid),
        ])
        if employee.id is not False:
            return employee.id
        return False
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Received by',
        required=True,
        default=_default_employee_id
    )

    date_received = fields.Datetime(
        string='Received Date',
        required=True,
        default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    def _default_dir_path_report(self):
        LabTestReport = self.env['clv.lab_test.report']
        return LabTestReport.lab_test_report_export_xls_dir_path()
    dir_path_report = fields.Char(
        string='Directory Path (Report)',
        required=True,
        help="Directory Path (Report)",
        default=_default_dir_path_report
    )

    def _default_file_name_report(self):
        LabTestReport = self.env['clv.lab_test.report']
        return LabTestReport.lab_test_report_export_xls_file_name()
    file_name_report = fields.Char(
        string='File Name (Report)',
        required=True,
        help="File Name (Report)",
        default=_default_file_name_report
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
    def do_lab_test_request_receive(self):
        self.ensure_one()

        LabTestResult = self.env['clv.lab_test.result']
        LabTestReport = self.env['clv.lab_test.report']

        for lab_test_request in self.lab_test_request_ids:

            _logger.info(u'%s %s %s', '>>>>>', lab_test_request.code, lab_test_request.person_id.name)

            if lab_test_request.state == 'draft':

                _logger.info(u'%s %s %s', '>>>>>', self.employee_id.name, self.date_received)

                lab_test_request.employee_id = self.employee_id
                lab_test_request.date_received = self.date_received
                lab_test_request.state = 'received'

            if lab_test_request.state not in ['draft', 'cancelled']:

                for lab_test_type in lab_test_request.lab_test_type_ids:

                    _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_type.name)

                    criteria = []
                    for criterion in lab_test_type.criterion_ids:
                        if criterion.result_display:
                            criteria.append((0, 0, {'code': criterion.code,
                                                    'name': criterion.name,
                                                    'sequence': criterion.sequence,
                                                    'normal_range': criterion.normal_range,
                                                    'unit_id': criterion.unit_id.id,
                                                    }))

                    values = {
                        'code_sequence': 'clv.lab_test.result.code',
                        'lab_test_type_id': lab_test_type.id,
                        'person_id': lab_test_request.person_id.id,
                        'lab_test_request_id': lab_test_request.id,
                        'history_marker_id': lab_test_request.history_marker_id.id,
                        'criterion_ids': criteria,
                    }
                    lab_test_result = LabTestResult.create(values)

                    _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', lab_test_result.code)

                    criteria = []
                    for criterion in lab_test_type.criterion_ids:
                        if criterion.report_display:
                            criteria.append((0, 0, {'code': criterion.code,
                                                    'name': criterion.name,
                                                    'sequence': criterion.sequence,
                                                    'normal_range': criterion.normal_range,
                                                    'unit_id': criterion.unit_id.id,
                                                    }))

                    values = {
                        'code_sequence': 'clv.lab_test.report.code',
                        'lab_test_type_id': lab_test_type.id,
                        'person_id': lab_test_request.person_id.id,
                        'lab_test_request_id': lab_test_request.id,
                        'history_marker_id': lab_test_request.history_marker_id.id,
                        'criterion_ids': criteria,
                    }
                    lab_test_report = LabTestReport.create(values)

                    lab_test_report.lab_test_report_export_xls(self.dir_path_report, self.file_name_report)

                    _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', lab_test_report.code)

                    lab_test_result.lab_test_report_id = lab_test_report.id

        return True
