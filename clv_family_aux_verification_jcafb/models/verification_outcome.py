# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class FamilyAux(models.Model):
    _inherit = 'clv.family_aux'

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

    def _family_aux_verification(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        state = 'ok'
        outcome_info = ''

        if model_object.street is False:

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

    def _family_aux_verification_related_family(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        related_family = model_object.related_family_id

        state = 'ok'
        outcome_info = ''

        if related_family.id is not False:

            if (model_object.name != related_family.name):

                if outcome_info != '':
                    outcome_info += '\n'
                outcome_info += '"Name" has changed.'

                state = 'warned'

            if (model_object.phase_id != related_family.phase_id):

                if outcome_info != '':
                    outcome_info += '\n'
                outcome_info += '"Phase" has changed.'

                state = 'warned'

            if (model_object.reg_state != related_family.reg_state):

                if outcome_info != '':
                    outcome_info += '\n'
                outcome_info += '"Register State" has changed.'

                state = 'warned'

            if (model_object.state != related_family.state):

                if outcome_info != '':
                    outcome_info += '\n'
                outcome_info += '"State" has changed.'

                state = 'warned'

            if (model_object.zip != related_family.zip) or \
               (model_object.street != related_family.street) or \
               (model_object.street_number != related_family.street_number) or \
               (model_object.street2 != related_family.street2) or \
               (model_object.district != related_family.district) or \
               (model_object.country_id != related_family.country_id) or \
               (model_object.state_id != related_family.state_id) or \
               (model_object.city_id != related_family.city_id) or \
               (model_object.phone != related_family.phone) or \
               (model_object.mobile != related_family.mobile) or \
               (model_object.email != related_family.email):

                if outcome_info != '':
                    outcome_info += '\n'
                outcome_info += '"Contact Information" has changed.'

                state = 'warned'

        else:

            outcome_info = 'Missing "Related Family".'
            state = 'warned'

        if outcome_info == '':
            outcome_info = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_info'] = outcome_info
        verification_values['state'] = state
        verification_outcome.write(verification_values)

    def _family_aux_verification_ref_address_aux(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        ref_address_aux = model_object.ref_address_aux_id

        state = 'ok'
        outcome_info = ''

        if ref_address_aux.id is not False:

            if (model_object.zip != ref_address_aux.zip) or \
               (model_object.street != ref_address_aux.street) or \
               (model_object.street_number != ref_address_aux.street_number) or \
               (model_object.street2 != ref_address_aux.street2) or \
               (model_object.district != ref_address_aux.district) or \
               (model_object.country_id != ref_address_aux.country_id) or \
               (model_object.state_id != ref_address_aux.state_id) or \
               (model_object.city_id != ref_address_aux.city_id):

                if outcome_info != '':
                    outcome_info += '\n'
                outcome_info += 'Address (Aux) "Contact Information" mismatch.'

                state = 'warned'

        else:

            outcome_info = 'Missing "Address (Aux)".'
            state = 'warned'

        if outcome_info == '':
            outcome_info = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_info'] = outcome_info
        verification_values['state'] = state
        verification_outcome.write(verification_values)
