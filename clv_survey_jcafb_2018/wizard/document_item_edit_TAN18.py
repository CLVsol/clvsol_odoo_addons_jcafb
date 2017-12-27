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

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DocumentItemEdit(models.TransientModel):
    _inherit = 'clv.document.item_edit'

    #
    # TAN18
    #

    def _default_is_TAN18(self):
        active_id = self.env['clv.document'].browse(self._context.get('active_id'))
        if active_id.document_type_id.code == 'TAN18':
            is_TAN18 = True
        else:
            is_TAN18 = False
        return is_TAN18
    is_TAN18 = fields.Boolean('Is TAN18', readonly=True, default=_default_is_TAN18)

    def _default_TAN18_03_01(self):
        return self._get_default('TAN18', 'TAN18_03_01')
    TAN18_03_01 = fields.Selection([
        (u'Sim, declaro que entendi o texto acima e concordo em participar da Campanha Gratuita para Detecção de Anemia.',
         u'Sim, declaro que entendi o texto acima e concordo em participar da Campanha Gratuita para Detecção de Anemia.'),
        (u'Não concordo em participar.', u'Não concordo em participar.'),
    ], u'3.1. Consentimento', readonly=False, default=_default_TAN18_03_01)

    def _write_TAN18_03_01(self):
        self._set_value('TAN18', 'TAN18_03_01', self.TAN18_03_01)

    def _do_document_updt_TAN18(self):

        self._write_TAN18_03_01()

        return True
