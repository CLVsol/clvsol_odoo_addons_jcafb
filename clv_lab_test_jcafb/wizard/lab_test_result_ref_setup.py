# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class LabTestResultRefSetUp(models.TransientModel):
    _name = 'clv.lab_test.result.ref_setup'

    def _default_lab_test_result_ids(self):
        return self._context.get('active_ids')
    lab_test_result_ids = fields.Many2many(
        comodel_name='clv.lab_test.result',
        relation='clv_lab_test_result_ref_setup_rel',
        string='Documents',
        default=_default_lab_test_result_ids
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

    @api.multi
    def do_lab_test_result_ref_setup(self):
        self.ensure_one()

        for lab_test_result in self.lab_test_result_ids:

            _logger.info(u'%s %s (%s)', '>>>>>', lab_test_result.code,
                         lab_test_result.person_id)

            if lab_test_result.ref_id is False:

                if lab_test_result.person_id.id is not False:
                    lab_test_result.ref_id = lab_test_result.person_id._name + ',' + \
                        str(lab_test_result.person_id.id)
                    _logger.info(u'%s %s %s', '>>>>>>>>>>', lab_test_result.ref_model, lab_test_result.ref_name)

        return True
