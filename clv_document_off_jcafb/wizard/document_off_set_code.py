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


class DocumentOffSetCode(models.TransientModel):
    _name = 'clv.document.off.set_code'

    def _default_document_off_ids(self):
        return self._context.get('active_ids')
    document_off_ids = fields.Many2many(
        comodel_name='clv.document.off',
        relation='clv_document_off_set_code_rel',
        string='Documents (Off)',
        domain=['|', ('active', '=', False), ('active', '=', True)],
        default=_default_document_off_ids
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
    def do_document_off_set_code(self):
        self.ensure_one()

        DocumentOffCode = self.env['clv.document.off.code']

        for document_off in self.document_off_ids:

            if document_off.code is False:

                _logger.info(u'%s %s', '>>>>>', document_off.name)

                # if document_off.document_id.id is not False:
                #     document_off.code = document_off.document_id.code
                # else:

                #     document_off_codes = DocumentOffCode.search([
                #         ('off_instance_id', '=', document_off.off_instance_id.id),
                #         ('document_off_id', '=', False),
                #     ])
                #     for document_off_code in document_off_codes:
                #         _logger.info(u'%s %s', '>>>>>>>>>>', document_off_code.code)
                #         document_off.code = document_off_code.code
                #         document_off_code.document_off_id = document_off.id
                #         break

                document_off_codes = DocumentOffCode.search([
                    ('off_instance_id', '=', document_off.off_instance_id.id),
                    ('document_off_id', '=', False),
                ])
                for document_off_code in document_off_codes:
                    _logger.info(u'%s %s', '>>>>>>>>>>', document_off_code.code)
                    document_off.code = document_off_code.code
                    document_off_code.document_off_id = document_off.id
                    break

        return True
