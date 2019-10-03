# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class Family(models.Model):
    _inherit = 'clv.family'

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

    def _family_verification(self, verification_outcome, model_object):

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

            if model_object.reg_state not in ['done', 'canceled']:

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

        if outcome_info == '':
            outcome_info = False

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_info'] = outcome_info
        verification_values['state'] = state
        verification_outcome.write(verification_values)

    def _family_verification_ref_address(self, verification_outcome, model_object):

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
