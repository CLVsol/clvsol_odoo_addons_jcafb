# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

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

        if survey.code == 'QAN18':
            document_category_id = document_category_questionario
        if survey.code == 'QDH18':
            document_category_id = document_category_questionario
        if survey.code == 'QMD18':
            document_category_id = document_category_questionario
        if survey.code == 'QSC18':
            document_category_id = document_category_questionario
        if survey.code == 'QSF18':
            document_category_id = document_category_questionario
        if survey.code == 'QSI18':
            document_category_id = document_category_questionario
        if survey.code == 'TAN18':
            document_category_id = document_category_termo
        if survey.code == 'TCR18':
            document_category_id = document_category_termo
        if survey.code == 'TDH18':
            document_category_id = document_category_termo
        if survey.code == 'TID18':
            document_category_id = document_category_termo
        if survey.code == 'TPR18':
            document_category_id = document_category_termo
        if survey.code == 'TUR18':
            document_category_id = document_category_termo

        if survey.code == 'QVG18':
            document_category_id = document_category_questionario_vet
        if survey.code == 'QVI18':
            document_category_id = document_category_questionario_vet
        if survey.code == 'TCV18':
            document_category_id = document_category_termo_vet

        return document_category_id
