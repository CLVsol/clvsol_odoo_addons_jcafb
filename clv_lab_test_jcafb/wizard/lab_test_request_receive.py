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

        for lab_test_request in self.lab_test_request_ids:

            _logger.info(u'%s %s %s', '>>>>>', lab_test_request.code, lab_test_request.person_id.name)

            if lab_test_request.state == 'draft':

                _logger.info(u'%s %s %s', '>>>>>', self.employee_id.name, self.date_received)

                lab_test_request.employee_id = self.employee_id
                lab_test_request.date_received = self.date_received
                lab_test_request.state = 'received'

        return True
