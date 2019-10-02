# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class AddressAux(models.Model):
    _inherit = 'clv.address_aux'

    verification_outcome_ids = fields.One2many(
        string='Verification Outcomes',
        comodel_name='clv.verification.outcome',
        compute='_compute_verification_outcome_ids_and_count',
    )
    count_verification_outcomes = fields.Integer(
        string='Verification Outcomes (count)',
        compute='_compute_verification_outcome_ids_and_count',
    )
    count_verification_outcomes_2 = fields.Integer(
        string='Verification Outcomes 2 (count)',
        compute='_compute_verification_outcome_ids_and_count',
    )

    @api.multi
    def _compute_verification_outcome_ids_and_count(self):
        for record in self:

            search_domain = [
                ('model', '=', self._name),
                ('res_id', '=', record.id),
            ]

            verification_outcomes = self.env['clv.verification.outcome'].search(search_domain)

            record.count_verification_outcomes = len(verification_outcomes)
            record.count_verification_outcomes_2 = len(verification_outcomes)
            record.verification_outcome_ids = [(6, 0, verification_outcomes.ids)]


class VerificationOutcome(models.Model):
    _inherit = 'clv.verification.outcome'

    def _address_aux_verification(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        state = 'ok'
        outcome_info = ''

        if (model_object.contact_info_is_unavailable is False) and (model_object.street is False):

            if outcome_info != '':
                outcome_info += '\n'
            outcome_info += '"Contact Information" is missing.'

            state = 'warned'

        if model_object.phase_id.id is False:

            if outcome_info != '':
                outcome_info += '\n'
            outcome_info += '"Phase" is missing.'

            state = 'warned'

        if outcome_info == '':
            outcome_info = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_info'] = outcome_info
        verification_values['state'] = state
        verification_outcome.write(verification_values)

    def _address_aux_verification_related_address(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        related_address = model_object.related_address_id

        state = 'ok'
        outcome_info = ''

        if model_object.related_address_is_unavailable is False:

            if related_address.id is not False:

                if (model_object.name != related_address.name):

                    if outcome_info != '':
                        outcome_info += '\n'
                    outcome_info += '"Name" has changed.'

                    state = 'warned'

                if (model_object.phase_id != related_address.phase_id):

                    if outcome_info != '':
                        outcome_info += '\n'
                    outcome_info += '"Phase" has changed.'

                    state = 'warned'

                if (model_object.reg_state != related_address.reg_state):

                    if outcome_info != '':
                        outcome_info += '\n'
                    outcome_info += '"Register State" has changed.'

                    state = 'warned'

                if (model_object.state != related_address.state):

                    if outcome_info != '':
                        outcome_info += '\n'
                    outcome_info += '"State" has changed.'

                    state = 'warned'

                if (model_object.zip != related_address.zip) or \
                   (model_object.street != related_address.street) or \
                   (model_object.street_number != related_address.street_number) or \
                   (model_object.street2 != related_address.street2) or \
                   (model_object.district != related_address.district) or \
                   (model_object.country_id != related_address.country_id) or \
                   (model_object.state_id != related_address.state_id) or \
                   (model_object.city_id != related_address.city_id) or \
                   (model_object.phone != related_address.phone) or \
                   (model_object.mobile != related_address.mobile) or \
                   (model_object.email != related_address.email):

                    if outcome_info != '':
                        outcome_info += '\n'
                    outcome_info += '"Contact Information" has changed.'

                    state = 'warned'

            else:

                outcome_info = 'Missing "Related Address".'
                state = 'warned'

        if model_object.related_address_is_unavailable is True:

            if related_address.id is not False:

                outcome_info = '"Related Address" should not be set.'
                state = 'warned'

        if outcome_info == '':
            outcome_info = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_info'] = outcome_info
        verification_values['state'] = state
        verification_outcome.write(verification_values)
