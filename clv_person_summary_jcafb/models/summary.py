# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

import xlwt
# from xlutils.copy import copy
# from xlrd import open_workbook

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class Person(models.Model):
    _inherit = 'clv.person'

    summary_id = fields.Many2one(
        comodel_name='clv.summary',
        string='Summary',
        ondelete='restrict',
        readonly='True'
    )
    date_summary = fields.Datetime(
        string='Summary Date',
        related='summary_id.date_summary',
        store=False
    )

    @api.multi
    @api.multi
    def _person_summary_setup(self, dir_path, file_name):

        SummaryTemplate = self.env['clv.summary.template']
        Summary = self.env['clv.summary']

        model_name = 'clv.person'

        for person in self:

            _logger.info(u'%s %s', '>>>>> (person):', person.name)

            summary_templates = SummaryTemplate.search([
                ('model', '=', model_name),
            ])

            for summary_template in summary_templates:

                _logger.info(u'%s %s', '>>>>>>>>>> (summary_template):', summary_template.name)

                summary = Summary.with_context({'active_test': False}).search([
                    ('model', '=', model_name),
                    ('res_id', '=', person.id),
                    ('action', '=', summary_template.action),
                ])

                if summary.id is False:

                    summary_values = {}
                    summary_values['model'] = model_name
                    summary_values['res_id'] = person.id
                    # summary_values['method'] = summary_template.method
                    summary_values['action'] = summary_template.action
                    _logger.info(u'>>>>>>>>>>>>>>> %s %s',
                                 '(summary_values):', summary_values)
                    summary = Summary.create(summary_values)

                _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (summary):', summary)

                person.summary_id = summary.id

                action_call = 'self.env["clv.summary"].' + \
                    summary.action + \
                    '(summary, person)'

                _logger.info(u'%s %s', '>>>>>>>>>>', action_call)

                if action_call:

                    summary.state = 'Unknown'
                    summary.outcome_text = False

                    exec(action_call)

            self.env.cr.commit()

            summary._person_summary_export_xls(summary, person, dir_path, file_name)


class Summary(models.Model):
    _inherit = 'clv.summary'

    def _person_summary(self, summary, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_summary = datetime.now()

        Document = self.env['clv.document']
        SummaryDocument = self.env['clv.summary.document']
        LabTestRequest = self.env['clv.lab_test.request']
        SummaryLabTestRequest = self.env['clv.summary.lab_test.request']
        EventAttendee = self.env['clv.event.attendee']
        SummaryEvent = self.env['clv.summary.event']

        summary_documents = SummaryDocument.search([
            ('summary_id', '=', summary.id),
        ])
        summary_documents.unlink()

        summary_lab_test_requests = SummaryLabTestRequest.search([
            ('summary_id', '=', summary.id),
        ])
        summary_lab_test_requests.unlink()

        summary_events = SummaryEvent.search([
            ('summary_id', '=', summary.id),
        ])
        summary_events.unlink()

        search_domain = [
            ('ref_id', '=', model_object._name + ',' + str(model_object.id)),
        ]
        documents = Document.search(search_domain)
        lab_test_requests = LabTestRequest.search(search_domain)
        event_attendees = EventAttendee.search(search_domain)

        for document in documents:

            if document.phase_id.id == model_object.phase_id.id:

                values = {
                    'summary_id': summary.id,
                    'document_id': document.id,
                }
                SummaryDocument.create(values)

        for lab_test_request in lab_test_requests:

            if lab_test_request.phase_id.id == model_object.phase_id.id:

                values = {
                    'summary_id': summary.id,
                    'lab_test_request_id': lab_test_request.id,
                }
                SummaryLabTestRequest.create(values)

        for event_attendee in event_attendees:

            if event_attendee.event_id.phase_id.id == model_object.phase_id.id:

                values = {
                    'summary_id': summary.id,
                    'event_id': event_attendee.event_id.id,
                }
                SummaryEvent.create(values)

        summary_values = {}
        summary_values['date_summary'] = date_summary
        summary.write(summary_values)

    def _person_summary_export_xls(self, summary, model_object, dir_path, file_name):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        model_object_name = model_object._name.replace('.', '_')
        model_object_code = model_object.code

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', dir_path),
        ])

        file_name = file_name.replace('<model>', model_object_name).replace('<code>', model_object_code)
        file_path = dir_path + '/' + file_name
        wbook = xlwt.Workbook()
        sheet = wbook.add_sheet(file_name[8:])

        for i in range(0, 49):
            sheet.col(i).width = 256 * 2
        sheet.show_grid = False

        row_nr = 0

        row_nr += 1

        # style_bold_str = 'font: bold on'
        # style_bold = xlwt.easyxf(style_bold_str)

        style_str = 'font: bold on; font: italic on, height 256'
        style = xlwt.easyxf(style_str)
        sheet.write(row_nr, 0, self.reference_name, style=style)
        sheet.row(row_nr).height = 256
        row_nr += 2
        wbook.save(file_path)

        self.directory_id = file_system_directory.id
        self.file_name = file_name
        self.stored_file_name = file_name
