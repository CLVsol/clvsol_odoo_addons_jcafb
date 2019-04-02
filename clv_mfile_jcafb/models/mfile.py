# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class MediaFile(models.Model):
    _inherit = 'clv.mfile'

    survey_title = fields.Char(string='Survey Title')
    survey_id = fields.Many2one(
        comodel_name='survey.survey',
        string='Survey Type'
    )
    survey_description = fields.Html(
        string='Survey Type Description',
        related='survey_id.description',
        store=False,
        readonly=True
    )
    survey_user_input_id = fields.Many2one(
        comodel_name='survey.user_input',
        string='Survey User Input'
    )

    document_code = fields.Char(string='Document Code')
    document_id = fields.Many2one(
        comodel_name='clv.document',
        string='Related Document'
    )
    document_state = fields.Selection(
        string='Document State',
        related='document_id.state',
        store=False,
        readonly=True
    )

    person_code = fields.Char(string="Person Code")
    person_id = fields.Many2one(
        comodel_name='clv.person',
        string="Related Person"
    )
    # person_state = fields.Selection(
    #     string='Person State',
    #     related='person_id.state',
    #     store=False,
    #     readonly=True
    # )
    person_employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Responsible Empĺoyee (Person)',
        related='person_id.address_id.employee_id',
        store=True
    )

    address_code = fields.Char(help="Address Code")
    address_id = fields.Many2one(
        comodel_name='clv.address',
        string="Related Address"
    )
    # address_state = fields.Selection(
    #     string='Address State',
    #     related='address_id.state',
    #     store=False,
    #     readonly=True
    # )
    address_employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Responsible Empĺoyee (Address)',
        related='address_id.employee_id',
        store=True
    )

    lab_test_request_code = fields.Char(string="Lab Test Request Code")
    lab_test_request_id = fields.Many2one(
        comodel_name='clv.lab_test.request',
        string="Related Lab Test Request"
    )

    date_survey_file = fields.Datetime(
        string='Survey File Date',
        # default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    _sql_constraints = [
        (
            'name_uniq',
            'UNIQUE (name)',
            'Error! The File Name must be unique!'
        ),
    ]
