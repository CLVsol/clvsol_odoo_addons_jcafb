# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DocumentSurveyUserInputValidate(models.TransientModel):
    _description = 'Survey User Input Validate'
    _name = 'clv.document.survey_user_input_validate'

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        comodel_name='clv.document',
        relation='clv_document_survey_user_input_validate_rel',
        string='Documents',
        default=_default_document_ids
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

    def do_document_survey_user_input_validate(self):
        self.ensure_one()

        for document in self.document_ids:

            document.survey_user_input_id._survey_user_input_validate()

        return True
