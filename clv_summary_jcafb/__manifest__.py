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
    'name': 'Summary (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Summary Module customizations for CLVhealth-JCAFB Solution.',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_summary',
        'clv_address_jcafb',
        'clv_person_jcafb',
        'clv_document_jcafb',
        'clv_lab_test_jcafb',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/summary_view.xml',
        'views/summary_address_person_view.xml',
        'views/summary_address_document_view.xml',
        'views/summary_person_document_view.xml',
        'views/summary_person_lab_test_request_view.xml',
        'views/summary_person_event_view.xml',
        'views/summary_person_off_document_view.xml',
        'views/summary_person_off_lab_test_request_view.xml',
        'views/summary_person_off_event_view.xml',
        'wizard/address_summary_setup_view.xml',
        'wizard/person_summary_setup_view.xml',
        'wizard/person_off_summary_setup_view.xml',
        'wizard/summary_refresh_view.xml',
        'wizard/summary_export_xls_view.xml',
        'views/summary_menu_view.xml',
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
