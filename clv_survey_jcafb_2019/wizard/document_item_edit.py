# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

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

        if document.document_type_id.code == 'QAN19':
            pass

        if document.document_type_id.code == 'QDH19':
            pass

        if document.document_type_id.code == 'QMD19':
            pass

        if document.document_type_id.code == 'QSC19':
            pass

        if document.document_type_id.code == 'QSF19':
            pass

        if document.document_type_id.code == 'QSI19':
            pass

        if document.document_type_id.code == 'TAN19':
            self._do_document_updt_TAN19()

        if document.document_type_id.code == 'TCR19':
            self._do_document_updt_TCR19()

        if document.document_type_id.code == 'TDH19':
            self._do_document_updt_TDH19()

        if document.document_type_id.code == 'TID19':
            self._do_document_updt_TID19()

        if document.document_type_id.code == 'TPR19':
            pass

        if document.document_type_id.code == 'TUR19':
            pass

        if document.document_type_id.code == 'TCV19':
            self._do_document_updt_TCV19()

        return True
