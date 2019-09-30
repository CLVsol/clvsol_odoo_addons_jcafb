# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class Person(models.Model):
    _inherit = 'clv.person'

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

    def _person_verification(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        state = 'ok'
        outcome_info = ''

        if model_object.street is False:

            if outcome_info != '':
                outcome_info += '\n'
            outcome_info += '"Contact Information" is missing.'

            state = 'warned'

        if model_object.gender is False:

            if outcome_info != '':
                outcome_info += '\n'
            outcome_info += '"Gender" is missing.'

            state = 'warned'

        if model_object.birthday is False:

            if outcome_info != '':
                outcome_info += '\n'
            outcome_info += '"Date of Birth" is missing.'

            state = 'warned'

        if outcome_info == '':
            outcome_info = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_info'] = outcome_info
        verification_values['state'] = state
        verification_outcome.write(verification_values)

    def _person_verification_ref_address(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        ref_address = model_object.ref_address_id

        state = 'ok'
        outcome_info = ''

        if ref_address.id is not False:

            if (model_object.zip != ref_address.zip) or \
               (model_object.street != ref_address.street) or \
               (model_object.street_number != ref_address.street_number) or \
               (model_object.street2 != ref_address.street2) or \
               (model_object.district != ref_address.district) or \
               (model_object.country_id != ref_address.country_id) or \
               (model_object.state_id != ref_address.state_id) or \
               (model_object.city_id != ref_address.city_id):

                if outcome_info != '':
                    outcome_info += '\n'
                outcome_info += 'Address "Contact Information" mismatch.'

                state = 'warned'

        else:

            outcome_info = 'Missing "Address".'
            state = 'warned'

        if outcome_info == '':
            outcome_info = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_info'] = outcome_info
        verification_values['state'] = state
        verification_outcome.write(verification_values)

    def _person_verification_family(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        family = model_object.family_id

        state = 'ok'
        outcome_info = ''

        if family.id is not False:

            if (model_object.zip != family.zip) or \
               (model_object.street != family.street) or \
               (model_object.street_number != family.street_number) or \
               (model_object.street2 != family.street2) or \
               (model_object.district != family.district) or \
               (model_object.country_id != family.country_id) or \
               (model_object.state_id != family.state_id) or \
               (model_object.city_id != family.city_id):

                if outcome_info != '':
                    outcome_info += '\n'
                outcome_info += 'Family "Contact Information" mismatch.'

                state = 'warned'

        else:

            outcome_info = 'Missing "Family".'
            state = 'warned'

        if outcome_info == '':
            outcome_info = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_info'] = outcome_info
        verification_values['state'] = state
        verification_outcome.write(verification_values)