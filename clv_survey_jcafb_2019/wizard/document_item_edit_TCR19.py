# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DocumentItemEdit(models.TransientModel):
    _inherit = 'clv.document.item_edit'

    #
    # TCR19
    #

    def _default_is_TCR19(self):
        active_id = self.env['clv.document'].browse(self._context.get('active_id'))
        if active_id.document_type_id.code == 'TCR19':
            is_TCR19 = True
        else:
            is_TCR19 = False
        return is_TCR19
    is_TCR19 = fields.Boolean('Is TCR19', readonly=True, default=_default_is_TCR19)

    def _default_TCR19_03_01(self):
        return self._get_default('TCR19', 'TCR19_03_01')
    TCR19_03_01 = fields.Selection([
        (u'Concordo em participar', u'Concordo em participar'),
        (u'Não concordo em participar', u'Não concordo em participar'),
    ], u'3.1. Questionário Socioeconômico', readonly=False, default=_default_TCR19_03_01)

    def _write_TCR19_03_01(self):
        self._set_value('TCR19', 'TCR19_03_01', self.TCR19_03_01)

    def _default_TCR19_03_02(self):
        return self._get_default('TCR19', 'TCR19_03_02')
    TCR19_03_02 = fields.Selection([
        (u'Concordo em participar', u'Concordo em participar'),
        (u'Não concordo em participar', u'Não concordo em participar'),
    ], u'3.2. Exame coproparasitológico de fezes', readonly=False, default=_default_TCR19_03_02)

    def _write_TCR19_03_02(self):
        self._set_value('TCR19', 'TCR19_03_02', self.TCR19_03_02)

    def _default_TCR19_03_03(self):
        return self._get_default('TCR19', 'TCR19_03_03')
    TCR19_03_03 = fields.Selection([
        (u'Concordo em participar', u'Concordo em participar'),
        (u'Não concordo em participar', u'Não concordo em participar'),
    ], u'3.3. Swab Anal', readonly=False, default=_default_TCR19_03_03)

    def _write_TCR19_03_03(self):
        self._set_value('TCR19', 'TCR19_03_03', self.TCR19_03_03)

    def _do_document_updt_TCR19(self):

        self._write_TCR19_03_01()
        self._write_TCR19_03_02()
        self._write_TCR19_03_03()

        return True
