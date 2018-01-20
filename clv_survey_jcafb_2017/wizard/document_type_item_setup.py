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


class DocumentTypeItemSetUp(models.TransientModel):
    _inherit = 'clv.document.type.item_setup'

    @api.multi
    def do_document_type_item_setup(self):
        self.ensure_one()

        super(DocumentTypeItemSetUp, self).do_document_type_item_setup()

        for document_type in self.document_type_ids:

            _logger.info(u'%s %s', '>>>>>', document_type.code)

            if document_type.code == 'QAN17':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'QDH17':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'QMD17':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'QSC17':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'QSF17':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'QSI17':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'TCP17':
                pass

            if document_type.code == 'TCR17':
                pass

            if document_type.code == 'TID17':
                pass

        return True
