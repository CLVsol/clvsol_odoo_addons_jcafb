# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from werkzeug import urls

from odoo import fields, models


class LabTestResult(models.Model):
    _inherit = 'clv.lab_test.result'

    survey_id = fields.Many2one(
        comodel_name='survey.survey',
        string='Survey Type')
    survey_user_input_id = fields.Many2one(
        comodel_name='survey.user_input',
        string='Survey User Input'
    )

    survey_url = fields.Char(
        string='Survey URL',
        compute="_compute_survey_url"
    )

    def _compute_survey_url(self):

        base_url = '/' if self.env.context.get('relative_url') else \
                   self.env['ir.config_parameter'].sudo().get_param('web.base.url')

        for lab_test_result in self:
            user_input = lab_test_result.survey_user_input_id
            survey_access_token = user_input.survey_id.access_token
            if survey_access_token is not False and user_input.token is not False:
                lab_test_result.survey_url = \
                    urls.url_join(base_url, "survey/fill/%s/%s" % (survey_access_token, user_input.token))
            else:
                lab_test_result.survey_url = False


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    lab_test_result_code = fields.Char(
        string='Lab Test Result Code',
        readonly=True
    )

    lab_test_result_id = fields.Many2one(
        comodel_name='clv.lab_test.result',
        string='Related Lab Test Result'
    )
