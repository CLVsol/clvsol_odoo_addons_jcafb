# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Lab Test (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Lab Test Module customizations for CLVhealth-JCAFB Solution.',
    'version': '12.0.4.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_lab_test',
        'clv_file_system',
        'clv_employee',
        'clv_set',
        'clv_base_jcafb',
        # 'clv_document_jcafb',
        'clv_survey',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/lab_test_type_view.xml',
        'views/lab_test_request_view.xml',
        'views/lab_test_request_code_view.xml',
        'wizard/lab_test_result_approve_view.xml',
        'wizard/lab_test_report_approve_view.xml',
        'views/lab_test_result_view.xml',
        'views/lab_test_result_code_view.xml',
        'wizard/lab_test_report_export_xls_view.xml',
        'views/lab_test_report_view.xml',
        'views/lab_test_report_code_view.xml',
        'views/file_system_view.xml',
        'views/lab_test_parasite_view.xml',
        'views/lab_test_crystal_view.xml',
        'views/survey_view.xml',
        'views/global_settings_view.xml',
        'data/lab_test_request_seq.xml',
        'data/lab_test_result_seq.xml',
        'data/lab_test_report_seq.xml',
        'data/lab_test_parasite.xml',
        'data/lab_test_crystal.xml',
        'data/file_system.xml',
        'data/global_settings.xml',
        'data/set_element.xml',
        'wizard/lab_test_request_receive_view.xml',
        'wizard/lab_test_request_associate_to_set_view.xml',
        'wizard/lab_test_report_associate_to_set_view.xml',
        'wizard/lab_test_result_set_survey_user_input_view.xml',
        'wizard/lab_test_result_cirteria_updt_from_survey_view.xml',
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
