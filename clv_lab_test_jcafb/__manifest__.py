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
    'name': 'Lab Test (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Lab Test Module customizations for CLVhealth-JCAFB Solution.',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_lab_test',
        'clv_survey',
        'clv_person_jcafb',
        'clv_document_jcafb',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/lab_test_type_view.xml',
        'views/lab_test_request_view.xml',
        'views/lab_test_request_code_view.xml',
        'views/lab_test_result_view.xml',
        'views/lab_test_result_code_view.xml',
        'views/lab_test_request_state_view.xml',
        'views/lab_test_result_reg_state_view.xml',
        'views/lab_test_result_state_view.xml',
        'views/lab_test_report_view.xml',
        'views/lab_test_report_code_view.xml',
        'views/lab_test_report_reg_state_view.xml',
        'views/lab_test_report_state_view.xml',
        'views/lab_test_parasite_view.xml',
        'views/lab_test_crystal_view.xml',
        'views/lab_test_menu_view.xml',
        'data/lab_test_request_seq.xml',
        'data/lab_test_result_seq.xml',
        'data/lab_test_report_seq.xml',
        'data/lab_test_unit.xml',
        'data/lab_test_parasite.xml',
        'data/lab_test_crystal.xml',
        'wizard/lab_test_request_setup_view.xml',
        'wizard/lab_test_request_receive_view.xml',
        'wizard/lab_test_result_setup_view.xml',
        'wizard/lab_test_report_setup_view.xml',
        'wizard/lab_test_request_document_setup_view.xml',
        'wizard/lab_test_result_edit_view.xml',
        'wizard/lab_test_report_edit_view.xml',
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
