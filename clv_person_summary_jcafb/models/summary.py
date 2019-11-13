# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class Person(models.Model):
    _inherit = 'clv.person'

    @api.multi
    @api.multi
    def _person_summary_setup(self):

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

                action_call = 'self.env["clv.summary"].' + \
                    summary.action + \
                    '(summary, person)'

                _logger.info(u'%s %s', '>>>>>>>>>>', action_call)

                if action_call:

                    summary.state = 'Unknown'
                    summary.outcome_text = False

                    exec(action_call)

            self.env.cr.commit()


class Summary(models.Model):
    _inherit = 'clv.summary'

    def _person_summary(self, summary, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_summary = datetime.now()

        # self._object_summary_updt(
        #     summary, state, outcome_info, date_summary, model_object
        # )

        summary_values = {}
        summary_values['date_summary'] = date_summary
        summary.write(summary_values)
