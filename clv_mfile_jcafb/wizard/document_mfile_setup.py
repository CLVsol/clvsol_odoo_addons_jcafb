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


class DocumentMfileSetUp(models.TransientModel):
    _name = 'clv.document.mfile_setup'

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        comodel_name='clv.document',
        relation='clv_document_mfile_setup_rel',
        string='Documents',
        domain=['|', ('active', '=', False), ('active', '=', True)],
        default=_default_document_ids
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
    def do_document_mfile_setup(self):
        self.ensure_one()

        MFile = self.env['clv.mfile']
        LabTestRequest = self.env['clv.lab_test.request']

        for document in self.document_ids:

            mfile_name = document.survey_id.code + '_' + document.code + '.xls'

            _logger.info(u'%s %s', '>>>>>', mfile_name)

            mfile = MFile.search([
                ('name', '=', mfile_name),
            ])

            if mfile.id is False:

                lab_test_request = LabTestRequest.search([
                    ('document_id', '=', document.id),
                    ('person_id', '=', document.person_id.id),
                ])
                lab_test_request_id = False
                if lab_test_request.id != []:
                    lab_test_request_id = lab_test_request.id

                values = {
                    'name': mfile_name,
                    'code': document.code,
                    'document_id': document.id,
                    'survey_id': document.survey_id.id,
                    'person_id': document.person_id.id,
                    'address_id': document.address_id.id,
                    'lab_test_request_id': lab_test_request_id,
                    'history_marker_id': document.history_marker_id.id,
                }
                mfile = MFile.create(values)
                _logger.info(u'%s %s', '>>>>>>>>>>', mfile.name)

                document.state = 'returned'

        return True

    @api.multi
    def do_populate_all_documents(self):
        self.ensure_one()

        Document = self.env['clv.document']
        documents = Document.search([])

        self.document_ids = documents

        return self._reopen_form()

    @api.multi
    def do_populate_new_documents(self):
        self.ensure_one()

        MFile = self.env['clv.mfile']

        Document = self.env['clv.document']
        documents = Document.search([])

        new_documents = []
        for document in documents:
            mfile = MFile.search([
                ('code', '=', document.code),
            ])
            if mfile.id is False:
                new_documents.append(document.id)

        self.document_ids = new_documents

        return self._reopen_form()
