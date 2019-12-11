# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

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

            if document_type.code == 'QAN20':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'QDH20':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'QMD20':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'QSC20':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'QSF20':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'QSI20':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'TAN20':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'TCR20':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'TDH20':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'TID20':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'TPR20':
                self._do_document_type_item_setup(document_type)

            if document_type.code == 'TUR20':
                self._do_document_type_item_setup(document_type)

        return True
