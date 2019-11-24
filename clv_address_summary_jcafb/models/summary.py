# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class Address(models.Model):
    _inherit = 'clv.address'

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
    def _address_summary_setup(self):

        SummaryTemplate = self.env['clv.summary.template']
        Summary = self.env['clv.summary']

        model_name = 'clv.address'

        for address in self:

            _logger.info(u'%s %s', '>>>>> (address):', address.name)

            summary_templates = SummaryTemplate.search([
                ('model', '=', model_name),
            ])

            for summary_template in summary_templates:

                _logger.info(u'%s %s', '>>>>>>>>>> (summary_template):', summary_template.name)

                summary = Summary.with_context({'active_test': False}).search([
                    ('model', '=', model_name),
                    ('res_id', '=', address.id),
                    ('action', '=', summary_template.action),
                ])

                if summary.id is False:

                    summary_values = {}
                    summary_values['model'] = model_name
                    summary_values['res_id'] = address.id
                    # summary_values['method'] = summary_template.method
                    summary_values['action'] = summary_template.action
                    _logger.info(u'>>>>>>>>>>>>>>> %s %s',
                                 '(summary_values):', summary_values)
                    summary = Summary.create(summary_values)

                _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (summary):', summary)

                address.summary_id = summary.id

                action_call = 'self.env["clv.summary"].' + \
                    summary.action + \
                    '(summary, address)'

                _logger.info(u'%s %s', '>>>>>>>>>>', action_call)

                if action_call:

                    summary.state = 'Unknown'
                    summary.outcome_text = False

                    exec(action_call)

            self.env.cr.commit()


class Summary(models.Model):
    _inherit = 'clv.summary'

    def _address_summary(self, summary, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_summary = datetime.now()

        Document = self.env['clv.document']
        SummaryDocument = self.env['clv.summary.document']
        LabTestRequest = self.env['clv.lab_test.request']
        SummaryLabTestRequest = self.env['clv.summary.lab_test.request']
        EventAttendee = self.env['clv.event.attendee']
        SummaryEvent = self.env['clv.summary.event']
        Family = self.env['clv.family']
        SummaryFamily = self.env['clv.summary.family']
        Person = self.env['clv.person']
        SummaryPerson = self.env['clv.summary.person']

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

        summary_families = SummaryFamily.search([
            ('summary_id', '=', summary.id),
        ])
        summary_families.unlink()

        summary_persons = SummaryPerson.search([
            ('summary_id', '=', summary.id),
        ])
        summary_persons.unlink()

        search_domain = [
            ('ref_id', '=', model_object._name + ',' + str(model_object.id)),
        ]
        documents = Document.search(search_domain)
        lab_test_requests = LabTestRequest.search(search_domain)
        event_attendees = EventAttendee.search(search_domain)

        search_domain = [
            ('ref_address_id', '=', model_object.id),
        ]
        families = Family.search(search_domain)

        search_domain = [
            ('ref_address_id', '=', model_object.id),
        ]
        persons = Person.search(search_domain)

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

        for family in families:

            values = {
                'summary_id': summary.id,
                'family_id': family.id,
            }
            SummaryFamily.create(values)

            search_domain = [
                ('ref_id', '=', 'clv.family' + ',' + str(family.id)),
            ]
            documents = Document.search(search_domain)
            lab_test_requests = LabTestRequest.search(search_domain)

            for document in documents:

                if document.phase_id.id == family.phase_id.id:

                    values = {
                        'summary_id': summary.id,
                        'document_id': document.id,
                    }
                    SummaryDocument.create(values)

            for lab_test_request in lab_test_requests:

                if lab_test_request.phase_id.id == family.phase_id.id:

                    values = {
                        'summary_id': summary.id,
                        'lab_test_request_id': lab_test_request.id,
                    }
                    SummaryLabTestRequest.create(values)

        for person in persons:

            values = {
                'summary_id': summary.id,
                'person_id': person.id,
            }
            SummaryPerson.create(values)

            search_domain = [
                ('ref_id', '=', 'clv.person' + ',' + str(person.id)),
            ]
            documents = Document.search(search_domain)
            lab_test_requests = LabTestRequest.search(search_domain)

            for document in documents:

                if document.phase_id.id == person.phase_id.id:

                    values = {
                        'summary_id': summary.id,
                        'document_id': document.id,
                    }
                    SummaryDocument.create(values)

            for lab_test_request in lab_test_requests:

                if lab_test_request.phase_id.id == person.phase_id.id:

                    values = {
                        'summary_id': summary.id,
                        'lab_test_request_id': lab_test_request.id,
                    }
                    SummaryLabTestRequest.create(values)

        summary_values = {}
        summary_values['date_summary'] = date_summary
        summary.write(summary_values)
