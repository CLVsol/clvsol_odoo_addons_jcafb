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


class LabTestOffRequestSetCode(models.TransientModel):
    _name = 'clv.lab_test.off.request.set_code'

    def _default_lab_test_off_request_ids(self):
        return self._context.get('active_ids')
    lab_test_off_request_ids = fields.Many2many(
        comodel_name='clv.lab_test.off.request',
        relation='clv_lab_test_off_request_set_code_rel',
        string='Lab Test (Off) Requests',
        domain=['|', ('active', '=', False), ('active', '=', True)],
        default=_default_lab_test_off_request_ids
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
    def do_lab_test_off_request_set_code(self):
        self.ensure_one()

        LabTestOffRequestCode = self.env['clv.lab_test.off.request.code']

        for lab_test_off_request in self.lab_test_off_request_ids:

            if lab_test_off_request.code is False:

                _logger.info(u'%s %s', '>>>>>', lab_test_off_request.code)

                lab_test_off_request_codes = LabTestOffRequestCode.search([
                    ('off_instance_id', '=', lab_test_off_request.off_instance_id.id),
                    ('lab_test_off_request_id', '=', False),
                ])
                for lab_test_off_request_code in lab_test_off_request_codes:
                    _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_off_request_code.code)
                    lab_test_off_request.code = lab_test_off_request_code.code
                    lab_test_off_request_code.lab_test_off_request_id = lab_test_off_request.id
                    break

        return True
