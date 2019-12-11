# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class Document(models.Model):
    _inherit = 'clv.document'

    def get_document_category_id(self, survey):

        DocumentCategory = self.env['clv.document.category']

        document_category = DocumentCategory.search([
            ('name', '=', 'Termo de Consentimento'),
        ])
        if document_category.id is not False:
            document_category_termo = document_category.id

        document_category = DocumentCategory.search([
            ('name', '=', 'Questionário'),
        ])
        if document_category.id is not False:
            document_category_questionario = document_category.id

        document_category = DocumentCategory.search([
            ('name', '=', '(VET) Termo de Consentimento'),
        ])
        if document_category.id is not False:
            document_category_termo_vet = document_category.id

        document_category = DocumentCategory.search([
            ('name', '=', '(VET) Questionário'),
        ])
        if document_category.id is not False:
            document_category_questionario_vet = document_category.id

        document_category_id = False

        if survey.code == 'QAN19':
            document_category_id = document_category_questionario
        if survey.code == 'QDH19':
            document_category_id = document_category_questionario
        if survey.code == 'QMD19':
            document_category_id = document_category_questionario
        if survey.code == 'QSC19':
            document_category_id = document_category_questionario
        if survey.code == 'QSF19':
            document_category_id = document_category_questionario
        if survey.code == 'QSI19':
            document_category_id = document_category_questionario
        if survey.code == 'TAN19':
            document_category_id = document_category_termo
        if survey.code == 'TCR19':
            document_category_id = document_category_termo
        if survey.code == 'TDH19':
            document_category_id = document_category_termo
        if survey.code == 'TID19':
            document_category_id = document_category_termo
        if survey.code == 'TPR19':
            document_category_id = document_category_termo
        if survey.code == 'TUR19':
            document_category_id = document_category_termo

        if survey.code == 'QVG19':
            document_category_id = document_category_questionario_vet
        if survey.code == 'QVI19':
            document_category_id = document_category_questionario_vet
        if survey.code == 'TCV19':
            document_category_id = document_category_termo_vet

        return document_category_id
