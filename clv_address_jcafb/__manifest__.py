# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Address (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Address Module customizations for CLVhealth-JCAFB Solution.',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_address',
        'clv_employee',
        'clv_document',
        'clv_lab_test',
    ],
    'data': [
        'views/address_view.xml',
        'views/address_code_view.xml',
        'views/address_annotation_view.xml',
        'views/address_reg_state_view.xml',
        'views/address_state_view.xml',
        'views/summary_file_system_view.xml',
        'views/document_view.xml',
        'views/lab_test_view.xml',
        'data/address_seq.xml',
        'data/document.xml',
        'data/lab_test.xml',
        'wizard/address_updt_view.xml',
        'wizard/address_document_setup_view.xml',
        'views/address_menu_view.xml',
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
