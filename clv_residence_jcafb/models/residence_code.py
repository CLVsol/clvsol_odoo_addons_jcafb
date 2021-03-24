# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Residence(models.Model):
    _name = "clv.residence"
    _inherit = 'clv.residence', 'clv.abstract.code'

    code = fields.Char(string='Residence Code', required=False, default='/')
    code_sequence = fields.Char(default='clv.address.code')

    def _residence_set_code(self):

        for residence in self:

            if residence.code is False:

                vals = {}

                # if residence.related_address_id.id is not False:
                #     if residence.related_address_id.code is not False:
                #         vals['code'] = residence.related_address_id.code
                #     else:
                #         vals['code'] = '/'

                # else:
                #     vals['code'] = '/'
                vals['code'] = '/'

                residence.write(vals)
