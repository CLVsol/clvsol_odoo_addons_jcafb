# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from odoo import api, fields, models, _

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

    verification_state = fields.Char(
        string='Verification State',
        default='Unknown',
        readonly=True
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

        state = 'Ok'
        outcome_info = ''

        if model_object.contact_info_is_unavailable:

            if model_object.street is not False:

                outcome_info = _('"Contact Information" should not be set.\n')
                state = self._get_verification_outcome_state(state, 'Error (L0)')

            # outcome_info = _('"Contact Information is Unavailable" should not be set.\n')
            # state = 'Error (L0)'

        else:

            if model_object.street is False:

                outcome_info += _('"Contact Information" is missing.\n')
                state = self._get_verification_outcome_state(state, 'Error (L0)')

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
                    state = self._get_verification_outcome_state(state, 'Warning (L0)')

        if model_object.reg_state not in ['ready', 'done', 'canceled']:

            if model_object.gender is False:

                outcome_info += _('"Gender" is missing.\n')
                state = self._get_verification_outcome_state(state, 'Warning (L0)')

            if model_object.birthday is False:

                outcome_info += _('"Date of Birth" is missing.\n')
                state = self._get_verification_outcome_state(state, 'Warning (L0)')

        if model_object.phase_id.id is False:

            outcome_info += _('"Phase" is missing.\n')
            state = self._get_verification_outcome_state(state, 'Error (L0)')

        if outcome_info == '':
            outcome_info = False

        self._object_verification_outcome_updt(
            verification_outcome, state, outcome_info, date_verification, model_object
        )

    def _person_aux_verification_related_person(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        related_person = model_object.related_person_id

        state = 'Ok'
        outcome_info = ''

        if model_object.related_person_is_unavailable:

            # if related_person.id is not False:

            #     outcome_info = _('"Related Person" should not be set\n.')
            #     state = 'Error (L0)'

            outcome_info = _('"Related Person is Unavailable" should not be set.\n')
            state = self._get_verification_outcome_state(state, 'Error (L1)')

        else:

            if related_person.id is not False:

                if (model_object.name != related_person.name):

                    outcome_info += _('"Name" has changed.\n')
                    state = self._get_verification_outcome_state(state, 'Warning (L1)')

                if (model_object.gender != related_person.gender):

                    outcome_info += _('"Gender" has changed.\n')
                    state = self._get_verification_outcome_state(state, 'Warning (L1)')

                if (model_object.birthday != related_person.birthday):

                    outcome_info += _('"Date of Birth" has changed.\n')
                    state = self._get_verification_outcome_state(state, 'Warning (L1)')

                if (model_object.date_death != related_person.date_death):

                    outcome_info += _('"Deceased Date" has changed.\n')
                    state = self._get_verification_outcome_state(state, 'Warning (L1)')

                if (model_object.phase_id != related_person.phase_id):

                    outcome_info += _('"Phase" has changed.\n')
                    state = self._get_verification_outcome_state(state, 'Warning (L1)')

                if (model_object.state != related_person.state):

                    outcome_info += _('"State" has changed.\n')
                    state = self._get_verification_outcome_state(state, 'Warning (L1)')

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

                    outcome_info += _('"Contact Information" has changed.\n')
                    state = self._get_verification_outcome_state(state, 'Warning (L1)')

            else:

                outcome_info = _('Missing "Related Person".\n')
                state = self._get_verification_outcome_state(state, 'Error (L1)')

        if outcome_info == '':
            outcome_info = False

        self._object_verification_outcome_updt(
            verification_outcome, state, outcome_info, date_verification, model_object
        )

    def _person_aux_verification_ref_address_aux(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        ref_address_aux = model_object.ref_address_aux_id

        state = 'Ok'
        outcome_info = ''

        if model_object.ref_address_aux_is_unavailable:

            if ref_address_aux.id is not False:

                outcome_info = _('"Address (Aux)" should not be set\n.')
                state = self._get_verification_outcome_state(state, 'Error (L0)')

            # outcome_info = _('"Address (Aux) is Unavailable" should not be set.\n')
            # state = self._get_verification_outcome_state(state, 'Error (L0)')

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

                    outcome_info += _('Address (Aux) "Contact Information" mismatch.\n')
                    state = self._get_verification_outcome_state(state, 'Warning (L0)')

            else:

                outcome_info = _('Missing "Address (Aux)".\n')
                state = self._get_verification_outcome_state(state, 'Warning (L0)')

        if outcome_info == '':
            outcome_info = False

        self._object_verification_outcome_updt(
            verification_outcome, state, outcome_info, date_verification, model_object
        )

    def _person_aux_verification_ref_address(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        ref_address = model_object.ref_address_id

        state = 'Ok'
        outcome_info = ''

        if model_object.ref_address_is_unavailable:

            if ref_address.id is not False:

                outcome_info = _('"Address" should not be set\n.')
                state = self._get_verification_outcome_state(state, 'Error (L1)')

            # outcome_info = _('"Address is Unavailable" should not be set.\n')
            # state = self._get_verification_outcome_state(state, 'Error (L1)')

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

                    outcome_info += _('Address "Contact Information" mismatch.\n')
                    state = self._get_verification_outcome_state(state, 'Warning (L1)')

            else:

                outcome_info = _('Missing "Address".\n')
                state = self._get_verification_outcome_state(state, 'Error (L1)')

        if outcome_info == '':
            outcome_info = False

        self._object_verification_outcome_updt(
            verification_outcome, state, outcome_info, date_verification, model_object
        )

    def _person_aux_verification_family_aux(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        family_aux = model_object.family_aux_id

        state = 'Ok'
        outcome_info = ''

        if model_object.family_aux_is_unavailable:

            if family_aux.id is not False:

                outcome_info = _('"Family (Aux)" should not be set\n.')
                state = self._get_verification_outcome_state(state, 'Error (L0)')

            # outcome_info = _('"Family (Aux) is Unavailable" should not be set.\n')
            # state = self._get_verification_outcome_state(state, 'Error (L0)')

        else:

            if family_aux.id is not False:

                if (model_object.zip != family_aux.zip) or \
                   (model_object.street != family_aux.street) or \
                   (model_object.street_number != family_aux.street_number) or \
                   (model_object.street2 != family_aux.street2) or \
                   (model_object.district != family_aux.district) or \
                   (model_object.country_id != family_aux.country_id) or \
                   (model_object.state_id != family_aux.state_id) or \
                   (model_object.city_id != family_aux.city_id):

                    outcome_info += _('Family (Aux) "Contact Information" mismatch.\n')
                    state = self._get_verification_outcome_state(state, 'Warning (L0)')

            else:

                outcome_info = _('Missing "Family (Aux)".\n')
                state = self._get_verification_outcome_state(state, 'Warning (L0)')

        if outcome_info == '':
            outcome_info = False

        self._object_verification_outcome_updt(
            verification_outcome, state, outcome_info, date_verification, model_object
        )

    def _person_aux_verification_family(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        family = model_object.family_id

        state = 'Ok'
        outcome_info = ''

        if model_object.family_is_unavailable:

            if family.id is not False:

                outcome_info = _('"Family" should not be set\n.')
                state = self._get_verification_outcome_state(state, 'Error (L1)')

            # outcome_info = _('"Family is Unavailable" should not be set.\n')
            # state = self._get_verification_outcome_state(state, 'Error (L1)')

        else:

            if family.id is not False:

                if (model_object.zip != family.zip) or \
                   (model_object.street != family.street) or \
                   (model_object.street_number != family.street_number) or \
                   (model_object.street2 != family.street2) or \
                   (model_object.district != family.district) or \
                   (model_object.country_id != family.country_id) or \
                   (model_object.state_id != family.state_id) or \
                   (model_object.city_id != family.city_id):

                    outcome_info += _('Family "Contact Information" mismatch.\n')
                    state = self._get_verification_outcome_state(state, 'Warning (L1)')

            else:

                outcome_info = _('Missing "Family".\n')
                state = self._get_verification_outcome_state(state, 'Warning (L1)')

        if outcome_info == '':
            outcome_info = False

        self._object_verification_outcome_updt(
            verification_outcome, state, outcome_info, date_verification, model_object
        )
