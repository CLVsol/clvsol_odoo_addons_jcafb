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


class LabTestOffReportSetup(models.TransientModel):
    _name = 'clv.lab_test.off.report.setup'

    def _default_lab_test_off_request_ids(self):
        return self._context.get('active_ids')
    lab_test_off_request_ids = fields.Many2many(
        comodel_name='clv.lab_test.off.request',
        relation='clv_lab_test_off_request_lab_test_off_report_setup_rel',
        string='Lab Test Off Requests',
        default=_default_lab_test_off_request_ids
    )

    def _default_lab_test_type_ids(self):
        lab_test_off_request_ids = self._context.get('active_ids')
        LabTestOffRequest = self.env['clv.lab_test.off.request']
        lab_test_off_request = LabTestOffRequest.search([
            ('id', '=', lab_test_off_request_ids[0]),
        ])
        return lab_test_off_request.lab_test_type_ids
    lab_test_type_ids = fields.Many2many(
        comodel_name='clv.lab_test.type',
        relation='clv_lab_test_type_lab_test_off_report_setup_rel',
        string='Lab Test Types',
        default=_default_lab_test_type_ids
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
    def do_lab_test_off_report_setup(self):
        self.ensure_one()

        LabTestOffReport = self.env['clv.lab_test.off.report']
        LabTestOffReportCode = self.env['clv.lab_test.off.report.code']

        for lab_test_off_request in self.lab_test_off_request_ids:

            _logger.info(u'%s %s %s', '>>>>>', lab_test_off_request.code, lab_test_off_request.person_off_id.name)

            # if lab_test_off_request.state not in ['draft', 'cancelled']:

            for lab_test_type in self.lab_test_type_ids:

                _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_type.name)

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
                    'lab_test_type_id': lab_test_type.id,
                    'person_off_id': lab_test_off_request.person_off_id.id,
                    'lab_test_off_request_id': lab_test_off_request.id,
                    'criterion_ids': criteria,
                    'off_instance_id': lab_test_off_request.off_instance_id.id,
                }
                lab_test_off_report = LabTestOffReport.create(values)

                lab_test_off_report_codes = LabTestOffReportCode.search([
                    ('off_instance_id', '=', lab_test_off_request.off_instance_id.id),
                    ('lab_test_off_report_id', '=', False),
                ])
                for lab_test_off_report_code in lab_test_off_report_codes:
                    lab_test_off_report.code = lab_test_off_report_code.code
                    lab_test_off_report_code.lab_test_off_report_id = lab_test_off_report.id
                    break

                _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', lab_test_off_report.code)

        return True
