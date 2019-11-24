# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class EmployeeSummarySetUp(models.TransientModel):
    _description = 'Employee Summary SetUp'
    _name = 'hr.employee.summary_setup'

    def _default_employee_ids(self):
        return self._context.get('active_ids')
    employee_ids = fields.Many2many(
        comodel_name='hr.employee',
        relation='hr_employee_summary_setup_rel',
        string='Employees',
        default=_default_employee_ids
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
    def do_employee_summary_setup(self):
        self.ensure_one()

        for employee in self.employee_ids:

            _logger.info(u'%s %s', '>>>>>', employee.name)

            # employee._employee_summary_setup(self.dir_path, self.file_name)
            employee._employee_summary_setup()

        return True

    @api.multi
    def do_populate_all_employees(self):
        self.ensure_one()

        Employee = self.env['hr.employee']
        employees = Employee.search([])

        self.employee_ids = employees

        return self._reopen_form()
