# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PersonAux(models.Model):
    _inherit = 'clv.person_aux'

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

    def _person_aux_verification(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        state = 'ok'
        outcome_text = ''

        if model_object.street is False:

            if outcome_text != '':
                outcome_text += '\n'
            outcome_text += '"Contact Information" is missing.'

            state = 'warned'

        if model_object.gender is False:

            if outcome_text != '':
                outcome_text += '\n'
            outcome_text += '"Gender" is missing.'

            state = 'warned'

        if model_object.birthday is False:

            if outcome_text != '':
                outcome_text += '\n'
            outcome_text += '"Date of Birth" is missing.'

            state = 'warned'

        if outcome_text == '':
            outcome_text = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_text'] = outcome_text
        verification_values['state'] = state
        verification_outcome.write(verification_values)

    def _person_aux_verification_related_person(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        related_person = model_object.related_person_id

        state = 'ok'
        outcome_text = ''

        if related_person.id is not False:

            if (model_object.name != related_person.name):

                if outcome_text != '':
                    outcome_text += '\n'
                outcome_text += '"Name" has changed.'

                state = 'warned'

            if (model_object.zip != related_person.zip) or \
               (model_object.street != related_person.street) or \
               (model_object.street_number != related_person.street_number) or \
               (model_object.street2 != related_person.street2) or \
               (model_object.district != related_person.district) or \
               (model_object.country_id != related_person.country_id) or \
               (model_object.state_id != related_person.state_id) or \
               (model_object.city_id != related_person.city_id) or \
               (model_object.phone != related_person.phone) or \
               (model_object.mobile != related_person.mobile) or \
               (model_object.email != related_person.email):

                if outcome_text != '':
                    outcome_text += '\n'
                outcome_text += '"Contact Information" has changed.'

                state = 'warned'

            if (model_object.gender != related_person.gender):

                if outcome_text != '':
                    outcome_text += '\n'
                outcome_text += '"Gender" has changed.'

                state = 'warned'

            if (model_object.birthday != related_person.birthday):

                if outcome_text != '':
                    outcome_text += '\n'
                outcome_text += '"Date of Birth" has changed.'

                state = 'warned'

        else:

            outcome_text = 'Missing "Related Person".'
            state = 'warned'

        if outcome_text == '':
            outcome_text = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_text'] = outcome_text
        verification_values['state'] = state
        verification_outcome.write(verification_values)

    def _person_aux_verification_ref_address_aux(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        ref_address_aux = model_object.ref_address_aux_id

        state = 'ok'
        outcome_text = ''

        if ref_address_aux.id is not False:

            if (model_object.zip != ref_address_aux.zip) or \
               (model_object.street != ref_address_aux.street) or \
               (model_object.street_number != ref_address_aux.street_number) or \
               (model_object.street2 != ref_address_aux.street2) or \
               (model_object.district != ref_address_aux.district) or \
               (model_object.country_id != ref_address_aux.country_id) or \
               (model_object.state_id != ref_address_aux.state_id) or \
               (model_object.city_id != ref_address_aux.city_id):

                if outcome_text != '':
                    outcome_text += '\n'
                outcome_text += 'Address (Aux) "Contact Information" mismatch.'

                state = 'warned'

        else:

            outcome_text = 'Missing "Address (Aux)".'
            state = 'warned'

        if outcome_text == '':
            outcome_text = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_text'] = outcome_text
        verification_values['state'] = state
        verification_outcome.write(verification_values)

    def _person_aux_verification_family_aux(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        family_aux = model_object.family_aux_id

        state = 'ok'
        outcome_text = ''

        if family_aux.id is not False:

            if (model_object.zip != family_aux.zip) or \
               (model_object.street != family_aux.street) or \
               (model_object.street_number != family_aux.street_number) or \
               (model_object.street2 != family_aux.street2) or \
               (model_object.district != family_aux.district) or \
               (model_object.country_id != family_aux.country_id) or \
               (model_object.state_id != family_aux.state_id) or \
               (model_object.city_id != family_aux.city_id):

                if outcome_text != '':
                    outcome_text += '\n'
                outcome_text += 'Family (Aux) "Contact Information" mismatch.'

                state = 'warned'

        else:

            outcome_text = 'Missing "Family (Aux)".'
            state = 'warned'

        if outcome_text == '':
            outcome_text = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_text'] = outcome_text
        verification_values['state'] = state
        verification_outcome.write(verification_values)
