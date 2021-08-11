# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DocumentAssociateFromFamilyToResidence(models.TransientModel):
    _description = 'Document Associate from Family to Residence'
    _name = 'clv.document.associate_from_family_to_residence'

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        comodel_name='clv.document',
        relation='clv_document_associate_from_family_to_residence_rel',
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

    def do_document_associate_from_family_to_residence(self):
        self.ensure_one()

        document_count = 0
        for document in self.document_ids:

            document_count += 1

            _logger.info(u'%s %s %s', '>>>>>', document_count, document.display_name)

            if (document.ref_model == 'clv.family') and (document.ref_id.ref_address_id.is_residence is True):

                related_residence = document.ref_id.ref_address_id.residence_ids
                ref_id = related_residence._name + ',' + str(related_residence.id)
                document.ref_id = ref_id

                _logger.info(u'%s %s', '>>>>>>>>>>', document.ref_id.name)

        return True
