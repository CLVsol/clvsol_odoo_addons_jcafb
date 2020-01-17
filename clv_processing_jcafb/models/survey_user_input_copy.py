# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from functools import reduce

from odoo import models

_logger = logging.getLogger(__name__)


def secondsToStr(t):

    return "%d:%02d:%02d.%03d" % reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000,), 1000, 60, 60])


class AbstractProcess(models.AbstractModel):
    _inherit = 'clv.abstract.process'

    def _do_survey_user_input_copy(self, schedule):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> schedule:', schedule.name)

        # external_host = 'https://clvheatlh-jcafb-2020-aws-tst.tklapp.com'
        # external_dbname = 'clvhealth_jcafb_2020'
        # external_user = 'admin'
        external_host = schedule.external_host_id.name
        external_dbname = schedule.external_host_id.external_dbname
        external_user = schedule.external_host_id.external_user
        external_user_pw = schedule.external_host_id.external_user_pw

        uid, sock, login_msg = self.external_host_login(
            external_host,
            external_dbname,
            external_user,
            external_user_pw
        )
