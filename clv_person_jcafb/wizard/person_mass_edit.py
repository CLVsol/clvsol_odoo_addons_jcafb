# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PersonMassEdit(models.TransientModel):
    _inherit = 'clv.person.mass_edit'

    random_field = fields.Char(
        string='Random ID', default=False,
        help='Use "/" to get an automatic new Random ID.'
    )
    random_field_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Random ID:', default=False, readonly=False, required=False
    )

    @api.multi
    def do_person_mass_edit(self):
        self.ensure_one()

        super().do_person_mass_edit()

        for person in self.person_ids:

            _logger.info(u'%s %s', '>>>>>', person.name)

            if self.random_field_selection == 'set':
                person.random_field = self.random_field
            if self.random_field_selection == 'remove':
                person.random_field = False

        return True
