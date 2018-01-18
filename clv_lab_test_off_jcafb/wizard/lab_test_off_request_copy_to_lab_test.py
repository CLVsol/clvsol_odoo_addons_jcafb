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


class LabTestOffRequestCopyToLabTest(models.TransientModel):
    _name = 'clv.lab_test.off.request.copy_to_lab_test'

    def _default_lab_test_off_request_ids(self):
        return self._context.get('active_ids')
    lab_test_off_request_ids = fields.Many2many(
        comodel_name='clv.lab_test.off.request',
        relation='clv_lab_test_off_request_copy_to_lab_test_rel',
        string='Lab Test (Off) Requests',
        domain=['|', ('active', '=', False), ('active', '=', True)],
        default=_default_lab_test_off_request_ids
    )

    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict'
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
    def do_lab_test_off_request_copy_to_lab_test(self):
        self.ensure_one()

        # LabTestRequest = self.env['clv.lab_test.request']
        # LabTestReport = self.env['clv.lab_test.report']
        # LabTestOffReport = self.env['clv.lab_test.off.report']

        for lab_test_off_request in self.lab_test_off_request_ids:

            _logger.info(u'%s %s', '>>>>>', lab_test_off_request.code)

            # lab_test_request = LabTestRequest.search([
            #     ('code', '=', lab_test_off_request.code),
            # ])

            # if lab_test_request.id is False:

            #     m2m_list = []
            #     for lab_test_type in lab_test_off_request.lab_test_type_ids:
            #         m2m_list.append((4, lab_test_type.id))

            #     values = {
            #         'code': lab_test_off_request.code,
            #         'code_sequence': 'clv.lab_test.request.code',
            #         'date_requested': lab_test_off_request.date_requested,
            #         'lab_test_type_ids': m2m_list,
            #         'person_id': lab_test_off_request.person_off_id.person_id.id,
            #         'history_marker_id': self.history_marker_id.id,
            #         'state': 'tested'
            #     }
            #     new_lab_test_request = LabTestRequest.create(values)

            #     # lab_test_off_request.state = 'done'
            #     lab_test_off_request.lab_test_request_id = new_lab_test_request.id

            #     _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', new_lab_test_request.code)

            #     lab_test_off_report = LabTestOffReport.search([
            #         ('lab_test_off_request_id', '=', lab_test_off_request.id),
            #     ])

            #     if lab_test_off_report.id is not False:

            #         lab_test_report = LabTestReport.search([
            #             ('code', '=', lab_test_off_report.code),
            #         ])

            #         if lab_test_report.id is False:

            #             values = {
            #                 'code': lab_test_off_report.code,
            #                 'code_sequence': 'clv.lab_test.report.code',
            #                 'date_requested': lab_test_off_report.date_requested,
            #                 'lab_test_type_ids': m2m_list,
            #                 'person_id': lab_test_off_report.person_off_id.person_id.id,
            #                 'history_marker_id': self.history_marker_id.id,
            #                 'reg_state': 'tested',
            #                 'state': 'tested'
            #             }
            #             new_lab_test_report = LabTestRequest.create(values)

            #             _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', new_lab_test_report.code)

        return True
