# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from odoo import api, fields, models, _

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

        if model_object.contact_info_is_unavailable:

            # if model_object.street is not False:

            #     outcome_info = _('"Contact Information" should not be set.\n')
            #     state = 'error'

            outcome_info = _('"Contact Information is Unavailable" should not be set.\n')
            state = 'error'

        else:

            if model_object.street is False:

                if outcome_info != '':
                    outcome_info += '\n'
                outcome_info += _('"Contact Information" is missing.\n')

                state = 'error'

            if model_object.reg_state not in ['ready', 'done', 'canceled']:

                if (model_object.zip is False) or \
                   (model_object.street is False) or \
                   (model_object.street_number is False) or \
                   (model_object.street2 is False) or \
                   (model_object.district is False) or \
                   (model_object.country_id is False) or \
                   (model_object.state_id is False) or \
                   (model_object.city_id is False):

                    outcome_info += _('Please, verify "Contact Information" data.\n')

                    if state != 'error':
                        state = 'warning'

        if model_object.phase_id.id is False:

            outcome_info += _('"Phase" is missing.\n')

            state = 'error'

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

        if model_object.related_family_is_unavailable:

            # if related_family.id is not False:

            #     outcome_info = _('"Related Family" should not be set\n.')
            #     state = 'error'

            outcome_info = _('"Related Family is Unavailable" should not be set.\n')
            state = 'error'

        else:

            if related_family.id is not False:

                if (model_object.name != related_family.name):

                    outcome_info += _('"Name" has changed.\n')

                    if state != 'error':
                        state = 'warning'

                if (model_object.phase_id != related_family.phase_id):

                    outcome_info += _('"Phase" has changed.\n')

                    if state != 'error':
                        state = 'warning'

                # if (model_object.reg_state != related_family.reg_state):

                #     outcome_info += _('"Register State" has changed.\n')

                #     if state != 'error':
                #         state = 'warning'

                if (model_object.state != related_family.state):

                    outcome_info += _('"State" has changed.\n')

                    if state != 'error':
                        state = 'warning'

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

                    outcome_info += _('"Contact Information" has changed.\n')

                    if state != 'error':
                        state = 'warning'

            else:

                outcome_info = _('Missing "Related Family".\n')

                state = 'error'

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

        if model_object.ref_address_aux_is_unavailable:

            if ref_address_aux.id is not False:

                outcome_info = _('"Address (Aux)" should not be set\n.')
                state = 'error'

            # outcome_info = _('"Address (Aux) is Unavailable" should not be set.\n')
            # state = 'error'

        else:

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
                    outcome_info += _('Address (Aux) "Contact Information" mismatch.')

                    if state != 'error':
                        state = 'warning'

            else:

                outcome_info = _('Missing "Address (Aux)".')
                if state != 'error':
                    state = 'warning'

        if outcome_info == '':
            outcome_info = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_info'] = outcome_info
        verification_values['state'] = state
        verification_outcome.write(verification_values)

    def _family_aux_verification_ref_address(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        ref_address = model_object.ref_address_id

        state = 'ok'
        outcome_info = ''

        if model_object.ref_address_is_unavailable:

            if ref_address.id is not False:

                outcome_info = _('"Address" should not be set\n.')
                state = 'error'

            # outcome_info = _('"Address is Unavailable" should not be set.\n')
            # state = 'error'

        else:

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
                    outcome_info += _('Address "Contact Information" mismatch.')

                    if state != 'error':
                        state = 'warning'

            else:

                outcome_info = _('Missing "Address".')
                if state != 'error':
                    state = 'warning'

        if outcome_info == '':
            outcome_info = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_info'] = outcome_info
        verification_values['state'] = state
        verification_outcome.write(verification_values)
