# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class DocumentRefSetUp(models.TransientModel):
    _name = 'clv.document.ref_setup'

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        comodel_name='clv.document',
        relation='clv_document_ref_setup_rel',
        string='Documents',
        default=_default_document_ids
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
    def do_document_ref_setup(self):
        self.ensure_one()

        for document in self.document_ids:

            _logger.info(u'%s %s (%s %s %s)', '>>>>>', document.code,
                         document.address_id, document.animal_id, document.person_id)

            if document.ref_id is False:

                if document.address_id.id is not False:
                    document.ref_id = document.address_id._name + ',' + str(document.address_id.id)
                    _logger.info(u'%s %s %s', '>>>>>>>>>>', document.ref_model, document.ref_name)

                if document.animal_id.id is not False:
                    document.ref_id = document.animal_id._name + ',' + str(document.animal_id.id)
                    _logger.info(u'%s %s %s', '>>>>>>>>>>', document.ref_model, document.ref_name)

                if document.person_id.id is not False:
                    document.ref_id = document.person_id._name + ',' + str(document.person_id.id)
                    _logger.info(u'%s %s %s', '>>>>>>>>>>', document.ref_model, document.ref_name)

        return True
