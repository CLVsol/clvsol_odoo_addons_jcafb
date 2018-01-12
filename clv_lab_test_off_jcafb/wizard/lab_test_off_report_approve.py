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
# You should have approved a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import logging
from datetime import datetime

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class LabTestOffReportApprove(models.TransientModel):
    _name = 'clv.lab_test.off.report.approve'

    def _default_lab_test_off_report_ids(self):
        return self._context.get('active_ids')
    lab_test_off_report_ids = fields.Many2many(
        comodel_name='clv.lab_test.off.report',
        relation='clv_lab_test_off_report_report_approve_rel',
        string='Lab Test (Off) Reports',
        readonly=True,
        default=_default_lab_test_off_report_ids
    )

    approved = fields.Boolean(string='Approved', default=True)

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
        string='Approved by',
        # required=True,
        default=_default_employee_id
    )

    date_approved = fields.Date(
        string='Approved Date',
        # required=True,
        default=lambda *a: datetime.now().strftime('%Y-%m-%d'),
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
    def do_lab_test_off_report_approve(self):
        self.ensure_one()

        for lab_test_off_report in self.lab_test_off_report_ids:

            _logger.info(u'%s %s %s', '>>>>>', lab_test_off_report.code, lab_test_off_report.person_off_id.name)

            # if lab_test_off_report.state == 'available':

            _logger.info(u'%s %s %s', '>>>>>', self.employee_id.name, self.date_approved)

            lab_test_off_report.approved = self.approved
            lab_test_off_report.employee_id = self.employee_id
            lab_test_off_report.date_approved = self.date_approved
            # lab_test_off_report.state = 'approved'

            # lab_test_off_report.lab_test_off_report_id.approved = self.approved
            # lab_test_off_report.lab_test_off_report_id.employee_id = self.employee_id
            # lab_test_off_report.lab_test_off_report_id.date_approved = self.date_approved
            # # lab_test_off_report.lab_test_off_report_id.state = 'approved'

        return True
