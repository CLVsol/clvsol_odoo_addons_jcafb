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


class DocumentOffCopyToDocument(models.TransientModel):
    _name = 'clv.document.off.copy_to_document'

    def _default_document_off_ids(self):
        return self._context.get('active_ids')
    document_off_ids = fields.Many2many(
        comodel_name='clv.document.off',
        relation='clv_document_off_copy_to_document_rel',
        string='Documents (Off)',
        domain=['|', ('active', '=', False), ('active', '=', True)],
        default=_default_document_off_ids
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
    def do_document_off_copy_to_document(self):
        self.ensure_one()

        Document = self.env['clv.document']

        for document_off in self.document_off_ids:

            _logger.info(u'%s %s', '>>>>>', document_off.code)

            document = Document.search([
                ('code', '=', document_off.code),
            ])

            if document.id is False:

                values = {
                    'name': document_off.name,
                    'code': document_off.code,
                    'code_sequence': 'clv.document.code',
                    'date_requested': document_off.date_requested,
                    # 'date_document': self.date_document,
                    # 'date_foreseen': document_off.date_foreseen,
                    # 'date_deadline': document_off.date_deadline,
                    'survey_id': document_off.survey_id.id,
                    # 'category_id': self.category_id.id,
                    'person_id': document_off.person_off_id.person_id.id,
                    'history_marker_id': self.history_marker_id.id,
                }
                new_document = Document.create(values)

                category_id = new_document.get_document_category_id(document_off.survey_id)

                if category_id is not False:

                    values = {
                        'category_ids': [(4, category_id)],
                    }
                    new_document.write(values)

                document_off.state = 'done'
                document_off.document_id = new_document.id

                _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', new_document.code)

        return True
