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


class PersonMngPersonAddressMove(models.TransientModel):
    _inherit = 'clv.person.mng.person_address_move'

    def _default_person_category_id(self):
        PersonCategory = self.env['clv.person.category']
        person_category = PersonCategory.search([
            ('name', '=', 'Mudou de Endereço'),
        ])
        m2m_list = []
        if person_category.id is not False:
            m2m_list.append((4, person_category.id))
        return m2m_list
    person_category_ids = fields.Many2many(
        comodel_name='clv.person.category',
        relation='clv_person_mng_person_address_move_person_category_rel',
        column1='person_id',
        column2='category_id',
        string='Person Categories',
        default=_default_person_category_id
    )

    @api.multi
    def do_person_mng_person_address_move(self):
        self.ensure_one()

        if self.person_category_ids.id == []:
            raise exceptions.ValidationError('The "Person Catgegories" has not been defined!')
            return self._reopen_form()

        for person_mng in self.person_mng_ids:

            if (person_mng.action_person_address == 'move') and \
               (person_mng.action_person == 'none') and \
               (person_mng.action_address == 'none') and \
               (person_mng.state == 'verified'):

                _logger.info(u'>>>>> %s', person_mng.name)

                if self.destination_addr_id:
                    person_mng.person_id.address_id = self.destination_addr_id

                    m2m_list = []
                    for person_category_id in self.person_category_ids:
                        m2m_list.append((4, person_category_id.id))
                    _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                    person_mng.person_id.category_ids = m2m_list

                    _logger.info(u'>>>>>>>>>> %s', person_mng.person_id.address_id.name)

                    person_mng.action_person_address = 'none'

                    Person = self.env['clv.person']

                    address_id = self.origin_addr_id.id
                    persons = False
                    if address_id is not False:
                        persons = Person.search([('address_id', '=', address_id)])
                    _logger.info(u'>>>>>>>>>> %s', self.origin_addr_person_ids)
                    self.origin_addr_person_ids = persons
                    _logger.info(u'>>>>>>>>>> %s', self.origin_addr_person_ids)

                    address_id = person_mng.address_id.id
                    persons = False
                    if address_id is not False:
                        persons = Person.search([('address_id', '=', address_id)])
                    _logger.info(u'>>>>>>>>>> %s', self.destination_addr_person_ids)
                    self.destination_addr_person_ids = persons
                    _logger.info(u'>>>>>>>>>> %s', self.destination_addr_person_ids)

        # return True
        return self._reopen_form()
