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

from odoo import fields, models


class AddressDocumentSetup(models.TransientModel):
    _inherit = 'clv.address.document_setup'

    def _default_survey_ids(self):
        Survey = self.env['survey.survey']
        survey = Survey.search([
            ('title', '=', '[QSF18]'),
        ])
        survey_id = False
        if survey.id is not False:
            survey_id = survey.id
        return [survey_id]
    survey_ids = fields.Many2many(
        comodel_name='survey.survey',
        relation='clv_address_document_setup_survey_rel',
        string='Survey Types',
        default=_default_survey_ids
    )

    def _default_category_id(self):
        DocumentCategory = self.env['clv.document.category']
        document_category = DocumentCategory.search([
            ('name', '=', 'Questionário'),
        ])
        category_id = False
        if document_category.id is not False:
            category_id = document_category.id
        return category_id
    category_id = fields.Many2one(
        comodel_name='clv.document.category',
        string='Document Category',
        ondelete='restrict',
        default=_default_category_id
    )

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
