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
    # TID18
    #

    def _default_is_TID18(self):
        active_id = self.env['clv.document'].browse(self._context.get('active_id'))
        if active_id.document_type_id.code == 'TID18':
            is_TID18 = True
        else:
            is_TID18 = False
        return is_TID18
    is_TID18 = fields.Boolean('Is TID18', readonly=True, default=_default_is_TID18)

    def _default_TID18_03_01(self):
        return self._get_default('TID18', 'TID18_03_01')
    TID18_03_01 = fields.Selection([
        (u'Concordo em participar', u'Concordo em participar'),
        (u'Não concordo em participar', u'Não concordo em participar'),
    ], u'3.1. Questionário Socioeconômicoo', readonly=False, default=_default_TID18_03_01)

    def _write_TID18_03_01(self):
        self._set_value('TID18', 'TID18_03_01', self.TID18_03_01)

    def _default_TID18_03_02(self):
        return self._get_default('TID18', 'TID18_03_02')
    TID18_03_02 = fields.Selection([
        (u'Concordo em participar', u'Concordo em participar'),
        (u'Não concordo em participar', u'Não concordo em participar'),
    ], u'3.2. Exame coproparasitológico de fezes', readonly=False, default=_default_TID18_03_02)

    def _write_TID18_03_02(self):
        self._set_value('TID18', 'TID18_03_02', self.TID18_03_02)

    def _default_TID18_03_03(self):
        return self._get_default('TID18', 'TID18_03_03')
    TID18_03_03 = fields.Selection([
        (u'Concordo em participar', u'Concordo em participar'),
        (u'Não concordo em participar', u'Não concordo em participar'),
    ], u'3.3. Exame de urina', readonly=False, default=_default_TID18_03_03)

    def _write_TID18_03_03(self):
        self._set_value('TID18', 'TID18_03_03', self.TID18_03_03)

    def _do_document_updt_TID18(self):

        self._write_TID18_03_01()
        self._write_TID18_03_02()
        self._write_TID18_03_03()

        return True
