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

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class AddressSummarySetUp(models.TransientModel):
    _name = 'clv.address.summary_setup'

    def _default_address_ids(self):
        return self._context.get('active_ids')
    address_ids = fields.Many2many(
        comodel_name='clv.address',
        relation='clv_address_summary_setup_rel',
        string='Addresses',
        default=_default_address_ids
    )

    def _default_dir_path(self):
        Summary = self.env['clv.summary']
        return Summary.summary_export_xls_dir_path()
    dir_path = fields.Char(
        string='Directory Path',
        required=True,
        help="Directory Path",
        default=_default_dir_path
    )

    def _default_file_name(self):
        Summary = self.env['clv.summary']
        return Summary.summary_export_xls_file_name()
    file_name = fields.Char(
        string='File Name',
        required=True,
        help="File Name",
        default=_default_file_name
    )

    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
        return action

    @api.multi
    def do_address_summary_setup(self):
        self.ensure_one()

        for address in self.address_ids:

            _logger.info(u'%s %s', '>>>>>', address.name)

            address.address_summary_setup(self.dir_path, self.file_name)

        return True

    @api.multi
    def do_populate_all_addresses(self):
        self.ensure_one()

        Address = self.env['clv.address']
        addresses = Address.search([])

        self.address_ids = addresses

        return self._reopen_form()
