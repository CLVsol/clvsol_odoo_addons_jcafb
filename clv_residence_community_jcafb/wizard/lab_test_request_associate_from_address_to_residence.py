# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestRequestAssociateFromAddressToResidence(models.TransientModel):
    _description = 'Lab Test Request Associate from Address to Residence'
    _name = 'clv.lab_test.request.associate_from_address_to_residence'

    def _default_lab_test_request_ids(self):
        return self._context.get('active_ids')
    lab_test_request_ids = fields.Many2many(
        comodel_name='clv.lab_test.request',
        relation='clv_lab_test_request_associate_from_address_to_residence_rel',
        string='Lab Test Requests',
        default=_default_lab_test_request_ids
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

    def do_lab_test_request_associate_from_address_to_residence(self):
        self.ensure_one()

        lab_test_request_count = 0
        for lab_test_request in self.lab_test_request_ids:

            lab_test_request_count += 1

            _logger.info(u'%s %s %s', '>>>>>', lab_test_request_count, lab_test_request.display_name)

            if (lab_test_request.ref_model == 'clv.address') and (lab_test_request.ref_id.is_residence is True):

                related_residence = lab_test_request.ref_id.residence_ids
                ref_id = related_residence._name + ',' + str(related_residence.id)
                lab_test_request.ref_id = ref_id

                _logger.info(u'%s %s', '>>>>>>>>>>', lab_test_request.ref_id.name)

        return True
