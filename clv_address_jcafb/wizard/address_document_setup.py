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

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class AddressDocumentSetUp(models.TransientModel):
    _name = 'clv.address.document_setup'

    def _default_address_ids(self):
        return self._context.get('active_ids')
    address_ids = fields.Many2many(
        comodel_name='clv.address',
        relation='clv_address_document_setup_rel',
        string='Addresses',
        default=_default_address_ids
    )

    survey_ids = fields.Many2many(
        comodel_name='survey.survey',
        relation='clv_address_document_setup_survey_rel',
        string='Surveys'
    )

    category_id = fields.Many2one(
        comodel_name='clv.document.category',
        string='Document Category'
    )

    date_foreseen = fields.Date(string='Foreseen Date', index=True)
    date_deadline = fields.Date(string='Deadline', index=True)

    def _default_history_marker_id(self):
        history_marker_id = int(self.env['ir.config_parameter'].get_param(
            'clv.config.settings.current_history_marker_id', '').strip())
        return history_marker_id
    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        default=_default_history_marker_id,
        ondelete='restrict'
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
    def do_address_document_setup(self):
        self.ensure_one()

        Document = self.env['clv.document']
        DocumentType = self.env['clv.document.type']

        for address in self.address_ids:

            ref_id = address._name + ',' + str(address.id)

            _logger.info(u'%s %s %s', '>>>>>', address.name, ref_id)

            for survey in self.survey_ids:

                _logger.info(u'%s %s', '>>>>>>>>>>', survey.title)

                document = Document.search([
                    ('survey_id', '=', survey.id),
                    # ('address_id', '=', address.id),
                    ('ref_id', '=', ref_id),
                    ('history_marker_id', '=', self.history_marker_id.id,),
                ])

                if document.id is False:

                    values = {
                        'name': survey.title,
                        # 'date_document': self.date_document,
                        'date_foreseen': self.date_foreseen,
                        'date_deadline': self.date_deadline,
                        'survey_id': survey.id,
                        # 'category_id': self.category_id.id,
                        # 'address_id': address.id,
                        'ref_id': ref_id,
                        'history_marker_id': self.history_marker_id.id,
                    }
                    new_document = Document.create(values)
                    new_document.code = '/'

                    if self.category_id.id is not False:

                        values = {
                            'category_ids': [(4, self.category_id.id)],
                        }
                        new_document.write(values)

                    else:

                        category_id = new_document.get_document_category_id(survey)

                        if category_id is not False:

                            values = {
                                'category_ids': [(4, category_id)],
                            }
                            new_document.write(values)

                    document_type = DocumentType.search([
                        ('code', '=', new_document.survey_id.code),
                    ])

                    document_type_id = False
                    if document_type.id is not False:
                        document_type_id = document_type.id

                    values = {
                        'document_type_id': document_type_id,
                    }
                    new_document.write(values)

                    _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', new_document.name)

        return True
