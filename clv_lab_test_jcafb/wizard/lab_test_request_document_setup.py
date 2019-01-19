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


class LabTestRequestDocumentSetUp(models.TransientModel):
    _name = 'clv.lab_test.request.document_setup'

    def _default_lab_test_request_ids(self):
        return self._context.get('active_ids')
    lab_test_request_ids = fields.Many2many(
        comodel_name='clv.lab_test.request',
        relation='clv_lab_test_request_lab_test_request_document_setup_rel',
        string='Lab Test Requests',
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
    def do_lab_test_request_document_setup(self):
        self.ensure_one()

        Document = self.env['clv.document']

        for lab_test_request in self.lab_test_request_ids:

            _logger.info(u'%s %s %s %s', '>>>>>', lab_test_request.code, lab_test_request.ref_id.name,
                         lab_test_request.lab_test_type_ids.survey_id.id)

            if lab_test_request.lab_test_type_ids.survey_id.id:
                person_id = False
                if lab_test_request.ref_id._name == 'clv.person':
                    person_id = lab_test_request.ref_id.id
                ref_id = lab_test_request.ref_id._name + ',' + str(person_id)
                survey_id = lab_test_request.lab_test_type_ids.survey_id.id
                documents = Document.search([
                    ('ref_id', '=', ref_id),
                    ('survey_id', '=', survey_id),
                    ('state', '!=', 'discarded'),
                ])
                _logger.info(u'%s %s', '>>>>>>>>>>', documents.name)

                lab_test_request.document_id = documents.id

        return True

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

        LabTestRequest = self.env['clv.lab_test.request']
        lab_test_requests = LabTestRequest.search([('document_id', '=', False)])

        new_lab_test_requests = []
        for lab_test_request in lab_test_requests:
            new_lab_test_requests.append(lab_test_request.id)

        self.lab_test_request_ids = new_lab_test_requests

        return self._reopen_form()
