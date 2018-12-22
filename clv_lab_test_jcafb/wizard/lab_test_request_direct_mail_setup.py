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


class LabTestRequestDirectMailSetUp(models.TransientModel):
    _name = 'clv.lab_test.request.direct_mail.setup'

    def _default_lab_test_request_ids(self):
        return self._context.get('active_ids')
    lab_test_request_ids = fields.Many2many(
        comodel_name='clv.lab_test.request',
        relation='clv_lab_test_request_direct_mail_setup_rel',
        string='Lab Test Requests',
        readonly=True,
        default=_default_lab_test_request_ids
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
    def do_lab_test_request_direct_mail_setup(self):
        self.ensure_one()

        LabTestRequestDirectMail = self.env['clv.lab_test.request.direct_mail']

        for lab_test_request in self.lab_test_request_ids:

            _logger.info(u'%s %s', '>>>>>', lab_test_request.code)

            request_code = lab_test_request.code
            lab_test_type = lab_test_request.lab_test_type_ids.name
            # person_name = lab_test_request.person_id.name
            person_name = lab_test_request.ref_id.name
            # person_code = lab_test_request.person_id.code
            person_code = lab_test_request.ref_id.code
            # person_age_reference = lab_test_request.person_id.age_reference
            person_age_reference = lab_test_request.ref_id.age_reference
            # person_category = lab_test_request.person_id.category_ids.name
            person_category = lab_test_request.ref_id.category_ids.name
            person_state = lab_test_request.ref_id.state

            values = {
                'request_code': request_code,
                'lab_test_type': lab_test_type,
                'person_name': person_name,
                'person_code': person_code,
                'person_age_reference': person_age_reference,
                'person_category': person_category,
                'person_state': person_state,
            }
            LabTestRequestDirectMail.create(values)

        return True

    @api.multi
    def do_delete_all(self):
        self.ensure_one()

        LabTestRequestDirectMail = self.env['clv.lab_test.request.direct_mail']

        all_lab_test_request_direct_mail = LabTestRequestDirectMail.search([])
        all_lab_test_request_direct_mail.unlink()

        return self._reopen_form()

    @api.multi
    def do_populate_all_lab_test_requests(self):
        self.ensure_one()

        LabTestRequest = self.env['clv.lab_test.request']
        lab_test_requests = LabTestRequest.search([])

        self.lab_test_request_ids = lab_test_requests

        return self._reopen_form()

    @api.multi
    def do_populate_new_lab_test_requests(self):
        self.ensure_one()

        LabTestRequestDirectMail = self.env['clv.lab_test.request.direct_mail']

        LabTestRequest = self.env['clv.lab_test.request']
        lab_test_requests = LabTestRequest.search([])

        new_lab_test_requests = []
        for lab_test_request in lab_test_requests:
            lab_test_request_direct_mail = LabTestRequestDirectMail.search([
                ('code', '=', lab_test_request.code),
            ])
            if lab_test_request_direct_mail.id is False:
                new_lab_test_requests.append(lab_test_request.id)

        self.lab_test_request_ids = new_lab_test_requests

        return self._reopen_form()
