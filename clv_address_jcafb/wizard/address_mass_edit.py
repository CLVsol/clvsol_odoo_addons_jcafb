# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class AddressMassEdit(models.TransientModel):
    _inherit = 'clv.address.mass_edit'

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Responsible Empĺoyee'
    )
    employee_id_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Responsible Empĺoyee:', default=False, readonly=False, required=False
    )

    @api.multi
    def do_address_mass_edit(self):
        self.ensure_one()

        super().do_address_mass_edit()

        for address in self.address_ids:

            _logger.info(u'%s %s', '>>>>>', address.name)

            if self.employee_id_selection == 'set':
                address.employee_id = self.employee_id
            if self.employee_id_selection == 'remove':
                address.employee_id = False

        return True
