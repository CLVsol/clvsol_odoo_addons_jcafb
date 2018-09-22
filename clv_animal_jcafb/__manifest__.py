# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Animal (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Animal Module customizations for CLVhealth-JCAFB Solution.',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_address_jcafb',
        'clv_animal',
        'clv_document',
        'clv_lab_test',
    ],
    'data': [
        'views/animal_code_view.xml',
        'views/address_view.xml',
        'views/animal_reg_state_view.xml',
        'views/animal_state_view.xml',
        'views/document_view.xml',
        'views/lab_test_view.xml',
        'data/animal_seq.xml',
        'data/document_referenceable_model.xml',
        'data/lab_test_referenceable_model.xml',
        'wizard/animal_updt_view.xml',
        'wizard/animal_document_setup_view.xml',
        'views/animal_menu_view.xml',
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
