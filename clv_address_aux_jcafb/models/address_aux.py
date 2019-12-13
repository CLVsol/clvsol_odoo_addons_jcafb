# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class AddressAux(models.Model):
    _inherit = 'clv.address_aux'

    related_address_state = fields.Selection(
        string='Related Address State',
        related='related_address_id.state',
        store=False
    )
