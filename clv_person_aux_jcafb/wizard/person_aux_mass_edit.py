# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PersonAuxMassEdit(models.TransientModel):
    _inherit = 'clv.person_aux.mass_edit'

    reg_state = fields.Selection(
        [('draft', 'Draft'),
         ('revised', 'Revised'),
         ('verified', 'Verified'),
         ('ready', 'Ready'),
         ('done', 'Done'),
         ('canceled', 'Canceled')
         ], string='Register State', readonly=False, required=False
    )
    reg_state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='Register State:', readonly=False, required=False
    )

    state = fields.Selection(
        [('new', 'New'),
         ('available', 'Available'),
         ('waiting', 'Waiting'),
         ('selected', 'Selected'),
         ('unselected', 'Unselected'),
         ('unavailable', 'Unavailable'),
         ('unknown', 'Unknown')
         ], string='State', readonly=False, required=False
    )
    state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='State:', readonly=False, required=False
    )

    @api.model
    def default_get(self, field_names):

        defaults = super().default_get(field_names)

        reg_state = self.env['clv.default_value'].search([
            ('model', '=', 'clv.person_aux'),
            ('parameter', '=', 'mass_edit_reg_state'),
            ('enabled', '=', True),
        ]).value

        reg_state_selection = self.env['clv.default_value'].search([
            ('model', '=', 'clv.person_aux'),
            ('parameter', '=', 'mass_edit_reg_state_selection'),
            ('enabled', '=', True),
        ]).value

        defaults['reg_state'] = reg_state
        defaults['reg_state_selection'] = reg_state_selection

        state = self.env['clv.default_value'].search([
            ('model', '=', 'clv.person_aux'),
            ('parameter', '=', 'mass_edit_state'),
            ('enabled', '=', True),
        ]).value

        state_selection = self.env['clv.default_value'].search([
            ('model', '=', 'clv.person_aux'),
            ('parameter', '=', 'mass_edit_state_selection'),
            ('enabled', '=', True),
        ]).value

        defaults['state'] = state
        defaults['state_selection'] = state_selection

        return defaults

    def do_person_aux_mass_edit(self):
        self.ensure_one()

        super().do_person_aux_mass_edit()

        for person_aux in self.person_aux_ids:

            _logger.info(u'%s %s', '>>>>>', person_aux.name)

            if self.reg_state_selection == 'set':
                person_aux.reg_state = self.reg_state
            if self.reg_state_selection == 'remove':
                person_aux.reg_state = False

            if self.state_selection == 'set':
                person_aux.state = self.state
            if self.state_selection == 'remove':
                person_aux.state = False

        return True
