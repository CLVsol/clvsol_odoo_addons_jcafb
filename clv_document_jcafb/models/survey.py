# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Document(models.Model):
    _inherit = 'clv.document'

    survey_id = fields.Many2one(
        comodel_name='survey.survey',
        string='Survey Type')
    survey_user_input_id = fields.Many2one(
        comodel_name='survey.user_input',
        string='Survey User Input'
    )
    base_survey_user_input_id = fields.Many2one(
        comodel_name='survey.user_input',
        string='Base Survey User Input'
    )


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    document_code = fields.Char(
        string='Document Code',
        readonly=True
    )

    person_code = fields.Char(
        string='Person Code',
        readonly=True
    )

    family_code = fields.Char(
        string='Family Code',
        readonly=True
    )

    address_code = fields.Char(
        string='Address Code',
        readonly=True
    )

    document_id = fields.Many2one(
        comodel_name='clv.document',
        string='Related Document'
    )

    notes = fields.Text(string='Notes')
