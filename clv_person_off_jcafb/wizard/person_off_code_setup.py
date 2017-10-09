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


class PersonOffCodeSetUp(models.TransientModel):
    _name = 'clv.person.off.code.setup'

    off_instance_id = fields.Many2one(
        comodel_name='clv.off.instance',
        string='Off Instance',
        required=True,
    )

    quantity = fields.Integer(
        'Quantity',
        help="Quantity of Codes",
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
    def do_person_off_code_setup(self):
        self.ensure_one()

        _logger.info(u'%s %s (%s)', '>>>>>', self.off_instance_id.name, self.quantity)

        PersonOffCode = self.env['clv.person.off.code']

        count = 0
        while count < self.quantity:
            count += 1

            values = {
                'off_instance_id': self.off_instance_id.id,
            }
            person_off_code = PersonOffCode.create(values)
            person_off_code.code = '/'

            _logger.info(u'%s %s', '>>>>>>>>>>', person_off_code.code)

        return True
