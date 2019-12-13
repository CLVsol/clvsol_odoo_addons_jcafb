# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PersonAux(models.Model):
    _inherit = 'clv.person_aux'

    ref_address_state = fields.Selection(
        string='Address State',
        related='ref_address_id.state',
        store=False
    )

    ref_address_aux_state = fields.Selection(
        string='Address (Aux) State',
        related='ref_address_aux_id.state',
        store=False
    )

    family_state = fields.Selection(
        string='Family State',
        related='family_id.state',
        store=False
    )

    related_person_state = fields.Selection(
        string='Related Person State',
        related='related_person_id.state',
        store=False
    )
