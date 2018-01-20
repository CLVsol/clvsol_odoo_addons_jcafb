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


class DocumentTypeSetUp(models.TransientModel):
    _name = 'clv.document.type_setup'

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        comodel_name='clv.document',
        relation='clv_document_type_setup_rel',
        string='Documents',
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
    def do_document_type_setup(self):
        self.ensure_one()

        DocumentType = self.env['clv.document.type']

        for document in self.document_ids:

            _logger.info(u'%s %s %s', '>>>>>', document.code, document.survey_id.code)

            document_type = DocumentType.search([
                ('code', '=', document.survey_id.code),
            ])

            document_type_id = False
            if document_type.id is not False:
                document_type_id = document_type.id

            document.document_type_id = document_type_id

            _logger.info(u'%s %s', '>>>>>>>>>>', document.document_type_id.code)

        return True
