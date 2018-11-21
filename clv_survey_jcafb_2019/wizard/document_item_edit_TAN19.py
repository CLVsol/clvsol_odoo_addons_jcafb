# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DocumentItemEdit(models.TransientModel):
    _inherit = 'clv.document.item_edit'

    #
    # TAN19
    #

    def _default_is_TAN19(self):
        active_id = self.env['clv.document'].browse(self._context.get('active_id'))
        if active_id.document_type_id.code == 'TAN19':
            is_TAN19 = True
        else:
            is_TAN19 = False
        return is_TAN19
    is_TAN19 = fields.Boolean('Is TAN19', readonly=True, default=_default_is_TAN19)

    def _default_TAN19_03_01(self):
        return self._get_default('TAN19', 'TAN19_03_01')
    TAN19_03_01 = fields.Selection([
        (u'Sim, declaro que entendi o texto acima e concordo em participar da Campanha Gratuita para Detecção de Anemia.',
         u'Sim, declaro que entendi o texto acima e concordo em participar da Campanha Gratuita para Detecção de Anemia.'),
        (u'Não concordo em participar.', u'Não concordo em participar.'),
    ], u'3.1. Consentimento', readonly=False, default=_default_TAN19_03_01)

    def _write_TAN19_03_01(self):
        self._set_value('TAN19', 'TAN19_03_01', self.TAN19_03_01)

    def _do_document_updt_TAN19(self):

        self._write_TAN19_03_01()

        return True
