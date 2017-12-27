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

from odoo import api, models

_logger = logging.getLogger(__name__)


class DocumentItemEdit(models.TransientModel):
    _inherit = 'clv.document.item_edit'

    @api.multi
    def do_document_updt(self):
        self.ensure_one()

        super(DocumentItemEdit, self).do_document_updt()

        document = self.env['clv.document'].browse(self._context.get('active_id'))

        _logger.info(u'%s %s', '>>>>>>>>>>', document.code)

        if document.document_type_id.code == 'QAN17':
            pass

        if document.document_type_id.code == 'QDH17':
            pass

        if document.document_type_id.code == 'QMD17':
            pass

        if document.document_type_id.code == 'QSC17':
            pass

        if document.document_type_id.code == 'QSF17':
            pass

        if document.document_type_id.code == 'QSI17':
            pass

        if document.document_type_id.code == 'TCP17':
            self._do_document_updt_TCP17()

        if document.document_type_id.code == 'TCR17':
            self._do_document_updt_TCR17()

        if document.document_type_id.code == 'TID17':
            self._do_document_updt_TID17()

        return True
