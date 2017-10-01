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


class AnimalMngAnimalCreate(models.TransientModel):
    _name = 'clv.animal.mng.animal_create'

    def _default_animal_mng_ids(self):
        return self._context.get('active_ids')
    animal_mng_ids = fields.Many2many(
        comodel_name='clv.animal.mng',
        relation='clv_animal_mng_animal_create_rel',
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
    def do_animal_mng_animal_create(self):
        self.ensure_one()

        if self.history_marker_id.id is False:
            raise exceptions.ValidationError('The "History Marker" has not been defined!')
            return self._reopen_form()

        Animal = self.env['clv.animal']

        for animal_mng in self.animal_mng_ids:

            _logger.info(u'>>>>> %s', animal_mng.name)

            if animal_mng.action_animal == 'create':

                if animal_mng.animal_id.id is False:

                    _logger.info(u'>>>>>>>>>> %s: %s', 'action_animal', animal_mng.action_animal)

                    species_id = False
                    if animal_mng.species_id is not False:
                        species_id = animal_mng.species_id.id

                    breed_id = False
                    if animal_mng.breed_id is not False:
                        breed_id = animal_mng.breed_id.id

                    tutor_id = False
                    if animal_mng.tutor_id is not False:
                        tutor_id = animal_mng.tutor_id.id

                    address_id = False
                    if animal_mng.address_id is not False:
                        address_id = animal_mng.address_id.id

                    values = {
                        'name': animal_mng.name,
                        'spayed': animal_mng.spayed,
                        'gender': animal_mng.gender,
                        'species_id': species_id,
                        'breed_id': breed_id,
                        'estimated_age': animal_mng.estimated_age,
                        'birthday': animal_mng.birthday,
                        'tutor_id': tutor_id,
                        'address_id': address_id,
                        'phone': animal_mng.phone,
                        'mobile': animal_mng.mobile,
                        'history_marker_id': self.history_marker_id.id,
                    }
                    _logger.info(u'>>>>> %s', values)
                    new_animal = Animal.create(values)

                    animal_mng.animal_id = new_animal.id

        return True
