# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'JCAFB Lab Tests (2020)',
    'summary': 'This module will install all the JCAFB lab tests (2020).',
    'version': '12.0.4.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_lab_test_jcafb',
    ],
    'data': [
        # 'wizard/lab_test_result_edit_EAN20_view.xml',
        # 'wizard/lab_test_result_edit_EDH20_view.xml',
        'wizard/lab_test_result_edit_ECP20_view.xml',
        'wizard/lab_test_result_edit_EEV20_view.xml',
        # 'wizard/lab_test_result_edit_EUR20_view.xml',
        # 'wizard/lab_test_report_edit_EAN20_view.xml',
        # 'wizard/lab_test_report_edit_EDH20_view.xml',
        'wizard/lab_test_report_edit_ECP20_view.xml',
        # 'wizard/lab_test_report_edit_EEV20_view.xml',
        # 'wizard/lab_test_report_edit_EUR20_view.xml',
        'wizard/lab_test_result_copy_to_report_ECP20_view.xml',
        'wizard/lab_test_result_copy_to_report_EEV20_view.xml',
        # 'wizard/lab_test_result_copy_to_report_EUR20_view.xml',
        # 'wizard/lab_test_off_report_edit_EAN20_view.xml',
        # 'wizard/lab_test_off_report_edit_EDH20_view.xml',
        'views/lab_test_result_view.xml',
        'views/lab_test_report_view.xml',
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
