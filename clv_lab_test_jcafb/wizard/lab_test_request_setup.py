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


class LabTestRequestSetup(models.TransientModel):
    _name = 'clv.lab_test.request.setup'

    def _default_person_ids(self):
        return self._context.get('active_ids')
    person_ids = fields.Many2many(
        comodel_name='clv.person',
        relation='clv_person_lab_test_request_setup_rel',
        string='Patients',
        default=_default_person_ids
    )

    lab_test_type_ids = fields.Many2many(
        comodel_name='clv.lab_test.type',
        relation='clv_lab_test_type_lab_test_request_setup_rel',
        string='Lab Test Types'
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
    def do_lab_test_request_setup(self):
        self.ensure_one()

        LabTestRequest = self.env['clv.lab_test.request']

        for person in self.person_ids:

            _logger.info(u'%s %s', '>>>>>', person.name)

            m2m_list = []
            for lab_test_type in self.lab_test_type_ids:
                m2m_list.append((4, lab_test_type.id))

            _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)

            values = {
                'code_sequence': 'clv.lab_test.request.code',
                'lab_test_type_ids': m2m_list,
                'person_id': person.id,
                'history_marker_id': self.history_marker_id.id,
            }
            lab_test_request = LabTestRequest.create(values)

            _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_request.code)

        return True
