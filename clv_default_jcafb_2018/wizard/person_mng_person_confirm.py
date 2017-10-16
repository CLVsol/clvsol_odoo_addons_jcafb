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


class PersonMngPersonConfirm(models.TransientModel):
    _inherit = 'clv.person.mng.person_confirm'

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
    def do_person_mng_person_confirm(self):
        self.ensure_one()

        if self.history_marker_id.id is False:
            raise exceptions.ValidationError('The "History Marker" has not been defined!')
            return self._reopen_form()

        for person_mng in self.person_mng_ids:

            _logger.info(u'>>>>> %s', person_mng.name)

            if (person_mng.action_person == 'confirm') and \
               (person_mng.person_id.name == person_mng.name) and \
               (person_mng.state == 'verified'):

                person_mng.person_id.history_marker_id = self.history_marker_id.id

                person_mng.action_person = 'none'

                _logger.info(u'>>>>>>>>>> %s: %s', 'action_person', person_mng.action_person)

        return True
