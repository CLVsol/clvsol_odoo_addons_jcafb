# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class EventAttendeeAssociateFromPersonToPatient(models.TransientModel):
    _description = 'Event Attendee Associate from Person to Patient'
    _name = 'clv.event.attendee.associate_from_person_to_patient'

    def _default_event_attendee_ids(self):
        return self._context.get('active_ids')
    event_attendee_ids = fields.Many2many(
        comodel_name='clv.event.attendee',
        relation='clv_event_attendee_associate_from_person_to_patient_rel',
        string='Event Attendees',
        default=_default_event_attendee_ids
    )

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

    def do_event_attendee_associate_from_person_to_patient(self):
        self.ensure_one()

        event_attendee_count = 0
        for event_attendee in self.event_attendee_ids:

            event_attendee_count += 1

            _logger.info(u'%s %s %s', '>>>>>', event_attendee_count, event_attendee.display_name)

            if (event_attendee.ref_model == 'clv.person') and (event_attendee.ref_id.is_patient is True):

                related_patient = event_attendee.ref_id.patient_ids
                ref_id = related_patient._name + ',' + str(related_patient.id)
                event_attendee.ref_id = ref_id

                _logger.info(u'%s %s', '>>>>>>>>>>', event_attendee.ref_id.name)

        return True
