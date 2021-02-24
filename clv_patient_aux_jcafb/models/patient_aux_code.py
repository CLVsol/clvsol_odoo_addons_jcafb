# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PatientAux(models.Model):
    _name = "clv.patient_aux"
    _inherit = 'clv.patient_aux', 'clv.abstract.code'

    code = fields.Char(string='Patient Code', required=False, default=False)
    code_sequence = fields.Char(default='clv.person.code')

    # @api.multi
    def _patient_aux_set_code(self):

        for patient_aux in self:

            if patient_aux.code is False:

                vals = {}

                if patient_aux.related_patient_id.id is not False:
                    if patient_aux.related_patient_id.code is not False:
                        vals['code'] = patient_aux.related_patient_id.code
                    else:
                        vals['code'] = '/'

                else:
                    vals['code'] = '/'

                patient_aux.write(vals)
