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

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class AddressDocumentSetup(models.TransientModel):
    _inherit = 'clv.person.document_setup'

    # def _default_survey_ids(self):
    #     Survey = self.env['survey.survey']
    #     survey = Survey.search([
    #         ('title', '=', '[QSF18]'),
    #     ])
    #     survey_id = False
    #     if survey.id is not False:
    #         survey_id = survey.id
    #     return [survey_id]
    # survey_ids = fields.Many2many(
    #     comodel_name='survey.survey',
    #     relation='clv_person_document_setup_survey_rel',
    #     string='Survey Types',
    #     default=_default_survey_ids
    # )

    # def _default_category_id(self):
    #     DocumentCategory = self.env['clv.document.category']
    #     document_category = DocumentCategory.search([
    #         ('name', '=', 'Questionário'),
    #     ])
    #     category_id = False
    #     if document_category.id is not False:
    #         category_id = document_category.id
    #     return category_id
    # category_id = fields.Many2one(
    #     comodel_name='clv.document.category',
    #     string='Document Category',
    #     ondelete='restrict',
    #     default=_default_category_id
    # )

    def _default_history_marker_id(self):
        HistoryMarker = self.env['clv.history_marker']
        history_marker = HistoryMarker.search([
            ('name', '=', 'JCAFB-2018'),
        ])
        history_marker_id = False
        if history_marker.id is not False:
            history_marker_id = history_marker.id
        return history_marker_id
    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict',
        default=_default_history_marker_id
    )

    def get_category_id(self, survey_title):

        DocumentCategory = self.env['clv.document.category']

        document_category = DocumentCategory.search([
            ('name', '=', 'Questionário'),
        ])
        category_id_questionario = False
        if document_category.id is not False:
            category_id_questionario = document_category.id

        document_category = DocumentCategory.search([
            ('name', '=', 'Termo de Consentimento'),
        ])
        category_id_termo = False
        if document_category.id is not False:
            category_id_termo = document_category.id

        category_id = False

        if (survey_title == '[QAN18]') or \
           (survey_title == '[QDH18]') or \
           (survey_title == '[QMD18]') or \
           (survey_title == '[QSF18]') or \
           (survey_title == '[QSC18]') or \
           (survey_title == '[QSI18]'):
            category_id = category_id_questionario

        if (survey_title == '[TAN18]') or \
           (survey_title == '[TDH18]') or \
           (survey_title == '[TCR18]') or \
           (survey_title == '[TID18]') or \
           (survey_title == '[TPR18]') or \
           (survey_title == '[TUR18]'):
            category_id = category_id_termo

        return category_id
