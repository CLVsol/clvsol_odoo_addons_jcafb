# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'JCAFB Surveys (2018)',
    'summary': 'This module will install all the JCAFB surveys (2018).',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_survey',
        'clv_document_jcafb',
    ],
    'data': [
        'data/survey_jcafb_QAN18.xml',
        'data/survey_jcafb_QDH18.xml',
        'data/survey_jcafb_QMD18.xml',
        'data/survey_jcafb_QSF18.xml',
        'data/survey_jcafb_QSC18.xml',
        'data/survey_jcafb_QSI18.xml',
        'data/survey_jcafb_TAN18.xml',
        'data/survey_jcafb_TDH18.xml',
        'data/survey_jcafb_TCR18.xml',
        'data/survey_jcafb_TID18.xml',
        'data/survey_jcafb_TPR18.xml',
        'data/survey_jcafb_TUR18.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
