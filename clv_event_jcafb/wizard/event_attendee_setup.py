# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class EventAttendeeSetUp(models.TransientModel):
    _name = 'clv.event.attendee_setup'

    def _default_event_attendee_ids(self):
        return self._context.get('active_ids')
    event_ids = fields.Many2many(
        comodel_name='clv.event',
        relation='clv_event_attendee_setup_rel',
        string='Events',
        default=_default_event_attendee_ids
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
    def do_event_attendee_ref_setup(self):
        self.ensure_one()

        EventAttendee = self.env['clv.event.attendee']

        for event in self.event_ids:

            _logger.info(u'%s %s (%s %s - %s)', '>>>>>', event.name,
                         event.count_persons, event.count_persons_off, event.count_event_attendees)

            if event.person_ids is not False:

                for person in event.person_ids:

                    ref_id = 'clv.person' + ',' + str(person.id)
                    _logger.info(u'%s %s (%s)', '>>>>>>>>>>', person.name, ref_id)

                    event_attendee = EventAttendee.search([
                        ('event_id', '=', event.id),
                        ('ref_id', '=', ref_id),
                    ])

                    _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', event_attendee)

                    if event_attendee.id is False:

                        _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', person.name)

                        values = {
                            'event_id': event.id,
                            'ref_id': ref_id,
                        }
                        _logger.info(u'>>>>>>>>>>>>>>> %s', values)
                        EventAttendee.create(values)

        return True
