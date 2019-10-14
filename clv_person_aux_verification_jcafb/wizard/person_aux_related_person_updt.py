# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PersonAuxRelatePersonUpdt(models.TransientModel):
    _description = 'Person (Aux) Related Person Update'
    _name = 'clv.person_aux.related_person_updt'

    person_aux_ids = fields.Many2many(
        comodel_name='clv.person_aux',
        relation='clv_person_aux_related_person_updt_rel',
        string='Persons (Aux)'
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

    @api.model
    def default_get(self, field_names):

        defaults = super().default_get(field_names)

        defaults['person_aux_ids'] = self.env.context['active_ids']

        return defaults

    @api.multi
    def do_person_aux_related_person_updt(self):
        self.ensure_one()

        for person_aux in self.person_aux_ids:

            _logger.info(u'%s %s', '>>>>>', person_aux.name)

            if not person_aux.related_person_is_unavailable:

                related_person = person_aux.related_person_id
                vals = {}

                if (person_aux.phase_id != related_person.phase_id):

                    vals['phase_id'] = person_aux.phase_id.id

                if (person_aux.state != related_person.state):

                    vals['state'] = person_aux.state

                if (person_aux.zip != related_person.zip):

                    vals['zip'] = person_aux.zip

                if (person_aux.street != related_person.street):

                    vals['street'] = person_aux.street

                if (person_aux.street_number != related_person.street_number):

                    vals['street_number'] = person_aux.street_number

                if (person_aux.street2 != related_person.street2):

                    vals['street2'] = person_aux.street2

                if (person_aux.district != related_person.district):

                    vals['district'] = person_aux.district

                if (person_aux.country_id != related_person.country_id):

                    vals['country_id'] = person_aux.country_id.id

                if (person_aux.state_id != related_person.state_id):

                    vals['state_id'] = person_aux.state_id.id

                if (person_aux.city_id != related_person.city_id):

                    vals['city_id'] = person_aux.city_id.id

                if (person_aux.phone is not False) and (person_aux.phone != related_person.phone):

                    vals['phone'] = person_aux.phone

                if (person_aux.mobile is not False) and (person_aux.mobile != related_person.mobile):

                    vals['mobile'] = person_aux.mobile

                if (person_aux.global_tag_ids.id is not False):

                    m2m_list = []
                    count = 0
                    for global_tag_id in person_aux.global_tag_ids:
                        m2m_list.append((4, global_tag_id.id))
                        count += 1

                    if count > 0:
                        vals['global_tag_ids'] = m2m_list

                if (person_aux.category_ids.id is not False):

                    m2m_list = []
                    count = 0
                    for global_tag_id in person_aux.category_ids:
                        m2m_list.append((4, global_tag_id.id))
                        count += 1

                    if count > 0:
                        vals['category_ids'] = m2m_list

                if (person_aux.marker_ids.id is not False):

                    m2m_list = []
                    count = 0
                    for global_tag_id in person_aux.marker_ids:
                        m2m_list.append((4, global_tag_id.id))
                        count += 1

                    if count > 0:
                        vals['marker_ids'] = m2m_list

                if vals != {}:

                    vals['reg_state'] = 'revised'

                _logger.info(u'%s %s', '>>>>>>>>>>', vals)
                related_person.write(vals)

        return True
