# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PersonAux(models.Model):
    _inherit = 'clv.person_aux'

    verification_ids = fields.One2many(
        string='Verifications',
        comodel_name='clv.verification',
        compute='_compute_verification_ids_and_count',
    )
    count_verifications = fields.Integer(
        string='Verifications (count)',
        compute='_compute_verification_ids_and_count',
    )
    count_verifications_2 = fields.Integer(
        string='Verifications 2 (count)',
        compute='_compute_verification_ids_and_count',
    )

    @api.multi
    def _compute_verification_ids_and_count(self):
        for record in self:

            search_domain = [
                ('model', '=', self._name),
                ('res_id', '=', record.id),
            ]

            verifications = self.env['clv.verification'].search(search_domain)

            record.count_verifications = len(verifications)
            record.count_verifications_2 = len(verifications)
            record.verification_ids = [(6, 0, verifications.ids)]
