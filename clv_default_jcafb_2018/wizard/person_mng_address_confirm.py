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


class PersonMngAddressConfirm(models.TransientModel):
    _inherit = 'clv.person.mng.address_confirm'

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
    def do_person_mng_address_confirm(self):
        self.ensure_one()

        if self.history_marker_id.id is False:
            raise exceptions.ValidationError('The "History Marker" has not been defined!')
            return self._reopen_form()

        for person_mng in self.person_mng_ids:

            _logger.info(u'>>>>> %s', person_mng.name)

            if (person_mng.action_address == 'confirm') and \
               (person_mng.address_name is False) and \
               (person_mng.action_person in ['update', 'confirm', 'none']) and \
               (person_mng.address_id.id == person_mng.person_id.address_id.id) and \
               (person_mng.state == 'verified'):

                person_mng.address_id.history_marker_id = self.history_marker_id.id

                _logger.info(u'>>>>>>>>>> %s: %s', 'action_address', person_mng.action_address)

                person_mng.action_address = 'none'

            elif (person_mng.action_address == 'confirm') and \
                 (person_mng.address_name is not False) and \
                 (person_mng.address_id.street == person_mng.street) and \
                 (person_mng.address_id.number == person_mng.number) and \
                 (person_mng.address_id.street2 == person_mng.street2) and \
                 (person_mng.address_id.district == person_mng.district) and \
                 (person_mng.address_id.l10n_br_city_id.id == person_mng.l10n_br_city_id.id) and \
                 (person_mng.address_id.state_id.id == person_mng.state_id.id) and \
                 (person_mng.address_id.country_id.id == person_mng.country_id.id) and \
                 (person_mng.state == 'verified'):

                person_mng.address_id.history_marker_id = self.history_marker_id.id

                _logger.info(u'>>>>>>>>>> %s: %s', 'action_address', person_mng.action_address)

                person_mng.action_address = 'none'

        return True
