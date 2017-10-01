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
from odoo import exceptions

_logger = logging.getLogger(__name__)


class AnimalMngAddressCreate(models.TransientModel):
    _name = 'clv.animal.mng.address_create'

    def _default_animal_mng_ids(self):
        return self._context.get('active_ids')
    animal_mng_ids = fields.Many2many(
        comodel_name='clv.animal.mng',
        relation='clv_animal_mng_address_create_rel',
        string='Animals (Management)',
        default=_default_animal_mng_ids
    )

    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict'
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
    def do_animal_mng_address_create(self):
        self.ensure_one()

        if self.history_marker_id.id is False:
            raise exceptions.ValidationError('The "History Marker" has not been defined!')
            return self._reopen_form()

        Address = self.env['clv.address']

        for animal_mng in self.animal_mng_ids:

            _logger.info(u'>>>>> %s', animal_mng.name)

            if animal_mng.action_address == 'create':

                if animal_mng.address_id.id is False:

                    _logger.info(u'>>>>>>>>>> %s: %s', 'action_address', animal_mng.action_address)

                    suggested_name = False
                    if animal_mng.street:
                        suggested_name = animal_mng.street
                        if animal_mng.number:
                            suggested_name = suggested_name + ', ' + animal_mng.number
                        if animal_mng.street2:
                            suggested_name = suggested_name + ' - ' + animal_mng.street2

                    if suggested_name is not False:

                        l10n_br_city_id = False
                        if animal_mng.l10n_br_city_id is not False:
                            l10n_br_city_id = animal_mng.l10n_br_city_id.id

                        state_id = False
                        if animal_mng.state_id is not False:
                            state_id = animal_mng.state_id.id

                        country_id = False
                        if animal_mng.country_id is not False:
                            country_id = animal_mng.country_id.id

                        new_category_ids = False
                        if animal_mng.addr_category_ids is not False:

                            new_category_ids = []
                            for category_id in animal_mng.addr_category_ids:

                                new_category_ids.append((4, category_id.id))

                        values = {
                            'name': suggested_name,
                            'street': animal_mng.street,
                            'number': animal_mng.number,
                            'street2': animal_mng.street2,
                            'district': animal_mng.district,
                            'zip': animal_mng.zip,
                            'l10n_br_city_id': l10n_br_city_id,
                            'state_id': state_id,
                            'country_id': country_id,
                            'phone': animal_mng.phone,
                            'mobile': animal_mng.mobile,
                            'category_ids': new_category_ids,
                            'history_marker_id': self.history_marker_id.id,
                        }
                        _logger.info(u'>>>>> %s', values)
                        new_address = Address.create(values)

                        animal_mng.address_id = new_address.id

        return True
