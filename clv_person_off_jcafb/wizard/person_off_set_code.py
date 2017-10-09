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


class PersonOffSetCode(models.TransientModel):
    _name = 'clv.person.off.set_code'

    def _default_person_off_ids(self):
        return self._context.get('active_ids')
    person_off_ids = fields.Many2many(
        comodel_name='clv.person.off',
        relation='clv_person_off_set_code_rel',
        string='Persons Off',
        domain=['|', ('active', '=', False), ('active', '=', True)],
        default=_default_person_off_ids
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
    def do_person_off_set_code(self):
        self.ensure_one()

        PersonOffCode = self.env['clv.person.off.code']

        for person_off in self.person_off_ids:

            if person_off.code is False:

                _logger.info(u'%s %s', '>>>>>', person_off.name)

                if person_off.person_id.id is not False:
                    person_off.code = person_off.person_id.code
                else:

                    person_off_codes = PersonOffCode.search([
                        ('off_instance_id', '=', person_off.off_instance_id.id),
                        ('person_off_id', '=', False),
                    ])
                    for person_off_code in person_off_codes:
                        _logger.info(u'%s %s', '>>>>>>>>>>', person_off_code.code)
                        person_off.code = person_off_code.code
                        person_off_code.person_off_id = person_off.id
                        break

        return True
