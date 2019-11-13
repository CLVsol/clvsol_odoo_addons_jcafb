# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PersonSummarySetUp(models.TransientModel):
    _description = 'Person Summary SetUp'
    _name = 'clv.person.summary_setup'

    def _default_person_ids(self):
        return self._context.get('active_ids')
    person_ids = fields.Many2many(
        comodel_name='clv.person',
        relation='clv_person_summary_setup_rel',
        string='Persons',
        default=_default_person_ids
    )

    # def _default_dir_path(self):
    #     Summary = self.env['clv.summary']
    #     return Summary.summary_export_xls_dir_path()
    # dir_path = fields.Char(
    #     string='Directory Path',
    #     required=True,
    #     help="Directory Path",
    #     default=_default_dir_path
    # )

    # def _default_file_name(self):
    #     Summary = self.env['clv.summary']
    #     return Summary.summary_export_xls_file_name()
    # file_name = fields.Char(
    #     string='File Name',
    #     required=True,
    #     help="File Name",
    #     default=_default_file_name
    # )

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
    def do_person_summary_setup(self):
        self.ensure_one()

        for person in self.person_ids:

            _logger.info(u'%s %s', '>>>>>', person.name)

            # person._person_summary_setup(self.dir_path, self.file_name)
            person._person_summary_setup()

        return True

    @api.multi
    def do_populate_all_persons(self):
        self.ensure_one()

        Person = self.env['clv.person']
        persons = Person.search([])

        self.person_ids = persons

        return self._reopen_form()
