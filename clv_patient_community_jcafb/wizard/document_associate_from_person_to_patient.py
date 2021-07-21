# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DocumentAssociateFromPersonToPatient(models.TransientModel):
    _description = 'Document Associate from Person to Patient'
    _name = 'clv.document.associate_from_person_to_patient'

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        comodel_name='clv.document',
        relation='clv_document_associate_from_person_to_patient_rel',
        string='Documents',
        default=_default_document_ids
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

    def do_document_associate_from_person_to_patient(self):
        self.ensure_one()

        document_count = 0
        for document in self.document_ids:

            document_count += 1

            _logger.info(u'%s %s %s', '>>>>>', document_count, document.display_name)

            if (document.ref_model == 'clv.person') and (document.ref_id.is_patient is True):

                related_patient = document.ref_id.patient_ids
                ref_id = related_patient._name + ',' + str(related_patient.id)
                document.ref_id = ref_id

                _logger.info(u'%s %s', '>>>>>>>>>>', document.ref_id.name)

        return True
