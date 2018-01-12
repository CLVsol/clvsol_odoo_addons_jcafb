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
    'name': 'Lab Test (Off) (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Lab Test (Off) Module customizations for CLVhealth-JCAFB Solution.',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_lab_test_off',
        'clv_person_off_jcafb',
        'clv_document_off_jcafb',
        'clv_lab_test_jcafb',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/lab_test_off_request_view.xml',
        'views/lab_test_off_request_code_view.xml',
        'views/lab_test_off_report_view.xml',
        'views/lab_test_off_report_code_view.xml',
        'wizard/lab_test_off_request_code_setup_view.xml',
        'wizard/lab_test_off_request_set_code_view.xml',
        'wizard/lab_test_off_report_setup_view.xml',
        'wizard/lab_test_off_report_code_setup_view.xml',
        'wizard/lab_test_off_report_set_code_view.xml',
        'wizard/lab_test_off_report_edit_view.xml',
        'wizard/lab_test_off_request_setup_view.xml',
        'wizard/lab_test_off_report_approve_view.xml',
        'wizard/lab_test_off_report_export_xls_view.xml',
        'views/lab_test_off_menu_view.xml',
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
