# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class SurveyUserInputSetSurveyUserInput(models.TransientModel):
    _description = 'SurveyUserInput Set Survey User Input'
    _name = 'clv.document.set_survey_user_input'

    @api.model
    def referenceable_models(self):
        return [(ref.model, ref.name) for ref in self.env['clv.referenceable.model'].search([
            ('base_model', '=', self._name),
        ])]

    def _default_document_id(self):
        return self._context.get('active_id')
    document_id = fields.Many2one(
        comodel_name='clv.document',
        string='SurveyUserInput',
        readonly=True,
        default=_default_document_id
    )

    def _default_document_type_id(self):
        return self.env['clv.document'].browse(self._context.get('active_id')).document_type_id
    document_type_id = fields.Many2one(
        comodel_name='clv.document.type',
        string='SurveyUserInput Type',
        readonly=True,
        default=_default_document_type_id
    )

    def _default_reference(self):
        reference = self.env['clv.document'].browse(self._context.get('active_id')).ref_id
        if reference:
            ref_name = reference.name
            ref_code = reference.code
            return ref_name + ' [' + ref_code + ']'
        else:
            return False
    reference = fields.Char(
        string='Refers to',
        readonly=True,
        default=_default_reference
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

    def do_document_set_survey_user_input(self):
        self.ensure_one()

        document = self.env['clv.document'].browse(self._context.get('active_id'))

        _logger.info(u'%s %s', '>>>>>', self.document_id.code)

        SurveyQuestion = self.env['survey.question']
        SurveyUserInput = self.env['survey.user_input']
        SurveyUserInputLine = self.env['survey.user_input.line']
        DocumentTypeParameter = self.env['clv.document.type.parameter']

        if document.survey_user_input_id.id is False:

            ref_model = document.ref_id._name

            values = {
                # 'token': document.code.replace('.', '-'),
                'survey_id': document.survey_id.id,
                'document_code': document.code,
                'document_id': document.id,
            }
            if ref_model == 'clv_person':
                values['person_code'] = document.ref_id.code
            if ref_model == 'clv_family':
                values['family_code'] = document.ref_id.code
            if ref_model == 'clv_address':
                values['address_code'] = document.ref_id.code

            new_user_input = SurveyUserInput.create(values)

            document.survey_user_input_id = new_user_input.id

            questions = SurveyQuestion.search([
                ('survey_id', '=', document.survey_id.id),
                ('is_page', '=', False),
            ])

            m2m_list = []
            for question in questions:
                m2m_list.append((4, question.id))
            new_user_input. predefined_question_ids = m2m_list

            document_type_parameters = DocumentTypeParameter.search([
                ('document_type_id', '=', document.document_type_id.id),
            ])

            for document_type_parameter in document_type_parameters:

                question = SurveyQuestion.search([
                    ('code', '=', document_type_parameter.item_code),
                ])
                values = {
                    'user_input_id': new_user_input.id,
                    'survey_id': document.survey_id.id,
                    'question_id': question.id,
                    'answer_type': document_type_parameter.item_type,
                    'value_char_box': eval('document.' + document_type_parameter.name),
                }
                SurveyUserInputLine.create(values)

            _logger.info(u'%s %s', '>>>>> ', new_user_input)

        return True
