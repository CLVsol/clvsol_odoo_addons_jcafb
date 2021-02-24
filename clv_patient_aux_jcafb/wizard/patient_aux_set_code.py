# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PatientAuxSetCode(models.TransientModel):
    _description = 'Patient (Aux) Set Code'
    _name = 'clv.patient_aux.set_code'

    def _default_patientaux_ids(self):
        return self._context.get('active_ids')
    patient_aux_ids = fields.Many2many(
        comodel_name='clv.patient_aux',
        relation='clv_patient_aux_set_code_rel',
        string='Patients (Aux)',
        default=_default_patientaux_ids
    )

    patient_aux_verification_exec = fields.Boolean(
        string='Patient (Aux) Verification Execute',
        default=True,
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

    def do_patient_aux_set_code(self):
        self.ensure_one()

        for patient_aux in self.patient_aux_ids:

            _logger.info(u'%s %s', '>>>>>', patient_aux.name)

            patient_aux._patient_aux_set_code()

            if self.patient_aux_verification_exec:
                patient_aux._patient_aux_verification_exec()

        return True
