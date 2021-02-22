# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PatientAuxDocumentSetUp(models.TransientModel):
    _description = 'Patient (Aux) Document Setup'
    _name = 'clv.patient_aux.document_setup'

    def _default_patient_aux_ids(self):
        return self._context.get('active_ids')
    patient_aux_ids = fields.Many2many(
        comodel_name='clv.patient_aux',
        relation='clv_patient_aux_document_setup_rel',
        string='Patients (Aux)',
        default=_default_patient_aux_ids
    )

    document_type_ids = fields.Many2many(
        comodel_name='clv.document.type',
        relation='clv_patient_aux_document_setup_document_type_rel',
        string='Document Types'
    )

    category_id = fields.Many2one(
        comodel_name='clv.document.category',
        string='Document Category'
    )

    def _default_phase_id(self):
        phase_id = int(self.env['ir.config_parameter'].sudo().get_param(
            'clv.global_settings.current_phase_id', '').strip())
        return phase_id
    phase_id = fields.Many2one(
        comodel_name='clv.phase',
        string='Phase',
        default=_default_phase_id,
        ondelete='restrict'
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

    def do_patient_aux_document_setup(self):
        self.ensure_one()

        Document = self.env['clv.document']
        DocumentType = self.env['clv.document.type']

        for patient_aux in self.patient_aux_ids:

            ref_id = patient_aux._name + ',' + str(patient_aux.id)

            _logger.info(u'%s %s %s', '>>>>>', patient_aux.name, ref_id)

            for document_type in self.document_type_ids:

                _logger.info(u'%s %s', '>>>>>>>>>>', document_type.name)

                document = Document.search([
                    ('document_type_id', '=', document_type.id),
                    ('ref_id', '=', ref_id),
                ])

                if document.id is False:

                    values = {
                        'code_sequence': 'clv.document.code',
                        'survey_id': document_type.survey_id.id,
                        # 'category_id': self.category_id.id,
                        'ref_id': ref_id,
                        'phase_id': self.phase_id.id,
                    }
                    new_document = Document.create(values)

                    if self.category_id.id is not False:

                        values = {
                            'category_ids': [(4, self.category_id.id)],
                        }
                        new_document.write(values)

                    else:

                        for category_id in document_type.category_ids:

                            values = {
                                'category_ids': [(4, category_id.id)],
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

                    _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', new_document.code)

        return True
