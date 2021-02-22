# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestResultAssociateToRelatedPatient(models.TransientModel):
    _description = 'Lab Test Result Associate to Related Patient'
    _name = 'clv.lab_test.result.associate_to_related_patient'

    def _default_lab_test_result_ids(self):
        return self._context.get('active_ids')
    lab_test_result_ids = fields.Many2many(
        comodel_name='clv.lab_test.result',
        relation='clv_lab_test_result_associate_to_related_patient_rel',
        string='Lab Test Results',
        default=_default_lab_test_result_ids
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

    def do_lab_test_result_associate_to_related_patient(self):
        self.ensure_one()

        lab_test_result_count = 0
        for lab_test_result in self.lab_test_result_ids:

            lab_test_result_count += 1

            _logger.info(u'%s %s %s', '>>>>>', lab_test_result_count, lab_test_result.display_name)

            if lab_test_result.ref_id.related_patient_id.id is not False:

                related_patient = lab_test_result.ref_id.related_patient_id
                ref_id = related_patient._name + ',' + str(related_patient.id)
                lab_test_result.ref_id = ref_id

                _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_result.ref_id.name)

        return True
