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


class PersonOffAddressConfirm(models.TransientModel):
    _inherit = 'clv.person.off.address_confirm'

    def _default_history_marker_id(self):
        HistoryMarker = self.env['clv.history_marker']
        history_marker = HistoryMarker.search([
            ('name', '=', 'JCAFB-2018'),
        ])
        history_marker_id = False
        if history_marker.id is not False:
            history_marker_id = history_marker.id
        return history_marker_id
    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict',
        default=_default_history_marker_id
    )

    @api.multi
    def do_person_off_address_confirm(self):
        self.ensure_one()

        if self.history_marker_id.id is False:
            raise exceptions.ValidationError('The "History Marker" has not been defined!')
            return self._reopen_form()

        for person_off in self.person_off_ids:

            _logger.info(u'>>>>> %s', person_off.name)

            if (person_off.action_address == 'confirm') and \
               (person_off.address_name is False) and \
               (person_off.action_person in ['update', 'confirm', 'none']) and \
               (person_off.address_id.id == person_off.person_id.address_id.id) and \
               (person_off.state == 'verified'):

                person_off.address_id.history_marker_id = self.history_marker_id.id

                _logger.info(u'>>>>>>>>>> %s: %s', 'action_address', person_off.action_address)

                person_off.action_address = 'none'

            elif (person_off.action_address == 'confirm') and \
                 (person_off.address_name is not False) and \
                 (person_off.address_id.street == person_off.street) and \
                 (person_off.address_id.number == person_off.number) and \
                 (person_off.address_id.street2 == person_off.street2) and \
                 (person_off.address_id.district == person_off.district) and \
                 (person_off.address_id.l10n_br_city_id.id == person_off.l10n_br_city_id.id) and \
                 (person_off.address_id.state_id.id == person_off.state_id.id) and \
                 (person_off.address_id.country_id.id == person_off.country_id.id) and \
                 (person_off.state == 'verified'):

                person_off.address_id.history_marker_id = self.history_marker_id.id

                _logger.info(u'>>>>>>>>>> %s: %s', 'action_address', person_off.action_address)

                person_off.action_address = 'none'

        return True
