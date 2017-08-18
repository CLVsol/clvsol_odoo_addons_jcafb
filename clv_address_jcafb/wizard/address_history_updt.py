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

from odoo import api, models
from odoo import exceptions

_logger = logging.getLogger(__name__)


class AddressHistoryUpdate(models.TransientModel):
    _inherit = 'clv.address.history_updt'

    @api.multi
    def do_address_history_updt(self):
        self.ensure_one()

        AddressHistory = self.env['clv.address.history']

        for address in self.address_ids:

            if self.sign_out_date is False:
                raise exceptions.ValidationError('The "Sign out date" has not been defined!')
                return self._reopen_form()

            if self.sign_in_date is False:
                raise exceptions.ValidationError('The "Sign in date" has not been defined!')
                return self._reopen_form()

            _logger.info(u'%s %s', '>>>>>', address.name)

            if address.history_marker_id.id is not False:

                address_history = AddressHistory.search([
                    ('address_id', '=', address.id),
                    ('history_marker_id', '=', address.history_marker_id.id),
                    ('sign_out_date', '=', False),
                ])

                if address_history.id is False:

                    address_history_2 = AddressHistory.search([
                        ('address_id', '=', address.id),
                        ('sign_out_date', '=', False),
                    ])
                    if address_history_2.id is not False:
                        address_history_2.sign_out_date = self.sign_out_date
                        _logger.info(u'%s %s %s %s %s', '>>>>>>>>>>', address_history_2.history_marker_id.name,
                                                        address_history_2.sign_in_date,
                                                        address_history_2.sign_out_date,
                                                        address_history_2.state)

                    m2m_list = []
                    for category_id in address.category_ids:
                        m2m_list.append((4, category_id.id))
                    category_ids = m2m_list
                    values = {
                        'address_id': address.id,
                        'category_ids': category_ids,
                        'reg_state': address.reg_state,
                        'state': address.state,
                        'employee_id': address.employee_id.id,
                        'sign_in_date': self.sign_in_date,
                        'history_marker_id': address.history_marker_id.id,
                    }
                    address_history = AddressHistory.create(values)
                    _logger.info(u'%s %s %s %s %s', '>>>>>>>>>>', address_history.history_marker_id.name,
                                                    address_history.sign_in_date,
                                                    address_history.sign_out_date,
                                                    address_history.state)

                else:
                    m2m_list = []
                    for category_id in address.category_ids:
                        m2m_list.append((4, category_id.id))
                    m2m_list_2 = []
                    for category_id in address_history.category_ids:
                        m2m_list_2.append((4, category_id.id))
                    if m2m_list != m2m_list_2:
                        address_history.category_ids = m2m_list
                    if address_history.reg_state != address.reg_state:
                        address_history.reg_state = address.reg_state
                    if address_history.state != address.state:
                        address_history.state = address.state
                    if address_history.employee_id.id != address.employee_id.id:
                        address_history.employee_id = address.employee_id.id
                    _logger.info(u'%s %s %s %s %s', '>>>>>>>>>>', address_history.history_marker_id.name,
                                                    address_history.sign_in_date,
                                                    address_history.sign_out_date,
                                                    address_history.state)

            else:

                address_history = AddressHistory.search([
                    ('address_id', '=', address.id),
                    ('sign_out_date', '=', False),
                ])

                if address_history.id is not False:
                    address_history.sign_out_date = self.sign_out_date
                    _logger.info(u'%s %s %s %s', '>>>>>>>>>>', address_history.history_marker_id.name,
                                                 address_history.sign_in_date,
                                                 address_history.sign_out_date)

        return True
        # return self._reopen_form()
