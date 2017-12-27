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

        if document.document_type_id.code == 'QAN18':
            pass

        if document.document_type_id.code == 'QDH18':
            pass

        if document.document_type_id.code == 'QMD18':
            pass

        if document.document_type_id.code == 'QSC18':
            pass

        if document.document_type_id.code == 'QSF18':
            pass

        if document.document_type_id.code == 'QSI18':
            pass

        if document.document_type_id.code == 'TAN18':
            self._do_document_updt_TAN18()

        if document.document_type_id.code == 'TCR18':
            self._do_document_updt_TCR18()

        if document.document_type_id.code == 'TDH18':
            # self._do_document_updt_TDH18()
            pass

        if document.document_type_id.code == 'TID18':
            # self._do_document_updt_TID18()
            pass

        if document.document_type_id.code == 'TPR18':
            # self._do_document_updt_TPR8()
            pass

        if document.document_type_id.code == 'TUR18':
            # self._do_document_updt_TUR8()
            pass

        return True
