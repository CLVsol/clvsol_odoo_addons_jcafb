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


class PersonUpdate(models.TransientModel):
    _inherit = 'clv.person.updt'

    reg_state = fields.Selection(
        [('draft', 'Draft'),
         ('revised', 'Revised'),
         ('done', 'Done'),
         ('canceled', 'Canceled')
         ], string='Register State', default=False, readonly=False, required=False
    )
    reg_state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='Register State', default=False, readonly=False, required=False
    )

    state = fields.Selection(
        [('new', 'New'),
         ('available', 'Available'),
         ('waiting', 'Waiting'),
         ('selected', 'Selected'),
         ('unselected', 'Unselected'),
         ('unavailable', 'Unavailable'),
         ('unknown', 'Unknown')
         ], string='State', default=False, readonly=False, required=False
    )
    state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='State', default=False, readonly=False, required=False
    )

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Responsible Empĺoyee'
    )
    employee_id_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Responsible Empĺoyee', default=False, readonly=False, required=False
    )

    random_field = fields.Char(
        string='Random ID'
    )
    random_field_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Random ID', default=False, readonly=False, required=False
    )

    community_ids = fields.Many2many(
        comodel_name='clv.community',
        relation='clv_person_updt_community_rel',
        column1='person_id',
        column2='community_id',
        string='Communities'
    )
    community_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Communities', default=False, readonly=False, required=False
    )

    event_ids = fields.Many2many(
        comodel_name='clv.event',
        relation='clv_person_updt_event_rel',
        column1='person_id',
        column2='event_id',
        string='Events'
    )
    event_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Events', default=False, readonly=False, required=False
    )

    @api.multi
    def do_person_updt(self):
        self.ensure_one()

        super(PersonUpdate, self).do_person_updt()

        for person in self.person_ids:

            _logger.info(u'%s %s', '>>>>>', person.name)

            if self.reg_state_selection == 'set':
                person.reg_state = self.reg_state
            if self.reg_state_selection == 'remove':
                person.reg_state = False

            if self.state_selection == 'set':
                person.state = self.state
            if self.state_selection == 'remove':
                person.state = False

            if self.employee_id_selection == 'set':
                person.employee_id = self.employee_id
            if self.employee_id_selection == 'remove':
                person.employee_id = False

            if self.random_field_selection == 'set':
                person.random_field = self.random_field
            if self.random_field_selection == 'remove':
                person.random_field = False

            if self.community_ids_selection == 'add':
                m2m_list = []
                for community_id in self.community_ids:
                    m2m_list.append((4, community_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.community_ids = m2m_list
            if self.community_ids_selection == 'remove_m2m':
                m2m_list = []
                for community_id in self.community_ids:
                    m2m_list.append((3, community_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.community_ids = m2m_list
            if self.community_ids_selection == 'set':
                m2m_list = []
                for community_id in person.community_ids:
                    m2m_list.append((3, community_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.community_ids = m2m_list
                m2m_list = []
                for community_id in self.community_ids:
                    m2m_list.append((4, community_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.community_ids = m2m_list

            if self.event_ids_selection == 'add':
                m2m_list = []
                for event_id in self.event_ids:
                    m2m_list.append((4, event_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.event_ids = m2m_list
            if self.event_ids_selection == 'remove_m2m':
                m2m_list = []
                for event_id in self.event_ids:
                    m2m_list.append((3, event_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.event_ids = m2m_list
            if self.event_ids_selection == 'set':
                m2m_list = []
                for event_id in person.event_ids:
                    m2m_list.append((3, event_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.event_ids = m2m_list
                m2m_list = []
                for event_id in self.event_ids:
                    m2m_list.append((4, event_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.event_ids = m2m_list

        return True
