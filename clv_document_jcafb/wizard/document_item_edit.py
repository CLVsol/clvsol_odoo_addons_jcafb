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


class DocumentItemEdit(models.TransientModel):
    _inherit = 'clv.document.item_edit'

    def _default_person_id(self):
        return self.env['clv.document'].browse(self._context.get('active_id')).person_id
    person_id = fields.Many2one(
        comodel_name='clv.person',
        string='Person',
        readonly=True,
        default=_default_person_id
    )

    def _default_address_id(self):
        return self.env['clv.document'].browse(self._context.get('active_id')).address_id
    address_id = fields.Many2one(
        comodel_name='clv.address',
        string='Address',
        readonly=True,
        default=_default_address_id
    )

    @api.multi
    def do_document_updt(self):
        self.ensure_one()

        super(DocumentItemEdit, self).do_document_updt()

        document = self.env['clv.document'].browse(self._context.get('active_id'))

        _logger.info(u'%s %s', '>>>>>>>>>>', document.code)

        return True
