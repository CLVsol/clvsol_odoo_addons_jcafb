# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Lab Test (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Lab Test Module customizations for CLVhealth-JCAFB Solution.',
    'version': '4.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_lab_test',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/lab_test_request_state_view.xml',
        'views/lab_test_result_reg_state_view.xml',
        'views/lab_test_result_state_view.xml',
        'views/lab_test_report_reg_state_view.xml',
        'views/lab_test_report_state_view.xml',
        'views/lab_test_menu_view.xml',
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
