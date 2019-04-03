# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class MediaFile(models.Model):
    _inherit = 'clv.mfile'

    date_file = fields.Datetime(
        string='File Date'
    )

    _sql_constraints = [
        (
            'name_uniq',
            'UNIQUE (name)',
            'Error! The File Name must be unique!'
        ),
    ]
