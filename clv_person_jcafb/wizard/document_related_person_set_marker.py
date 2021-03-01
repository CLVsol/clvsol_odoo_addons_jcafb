# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DocumentRelatedPersonSetMarker(models.TransientModel):
    _description = 'Document Related Person Set Marker'
    _name = 'clv.document.related_person_set_marker'

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        comodel_name='clv.document',
        relation='clv_document_related_person_set_marker_rel',
        string='Documents',
        default=_default_document_ids
    )

    marker_ids = fields.Many2many(
        comodel_name='clv.person.marker',
        relation='clv_document_related_person_set_marker_marker_rel',
        column1='person_id',
        column2='marker_id',
        string='Markers'
    )
    marker_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Markers:', default=False, readonly=False, required=False
    )

    def do_document_related_person_set_marker(self):
        self.ensure_one()

        document_count = 0
        for document in self.document_ids:

            document_count += 1

            _logger.info(u'%s %s %s', '>>>>>', document_count, document.display_name)

            if document.ref_id.id is not False and document.ref_model == 'clv.person':

                related_person = document.ref_id

                if self.marker_ids_selection == 'add':
                    m2m_list = []
                    for marker_id in self.marker_ids:
                        m2m_list.append((4, marker_id.id))
                    _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                    related_person.marker_ids = m2m_list
                if self.marker_ids_selection == 'remove_m2m':
                    m2m_list = []
                    for marker_id in self.marker_ids:
                        m2m_list.append((3, marker_id.id))
                    _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                    related_person.marker_ids = m2m_list
                if self.marker_ids_selection == 'set':
                    m2m_list = []
                    for marker_id in related_person.marker_ids:
                        m2m_list.append((3, marker_id.id))
                    _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                    related_person.marker_ids = m2m_list
                    m2m_list = []
                    for marker_id in self.marker_ids:
                        m2m_list.append((4, marker_id.id))
                    _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                    related_person.marker_ids = m2m_list

                _logger.info(u'%s %s', '>>>>>>>>>>', document.ref_id.name)

        return True
