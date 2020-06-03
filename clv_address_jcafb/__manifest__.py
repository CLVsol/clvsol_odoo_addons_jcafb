# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Address (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Address Module customizations for CLVhealth-JCAFB Solution.',
    'version': '12.0.4.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_address',
        'clv_document',
        'clv_community',
        'clv_event',
        'clv_lab_test',
        'clv_employee',
        'clv_base_jcafb',
    ],
    'data': [
        'data/address_seq.xml',
        'data/document.xml',
        'data/community_member.xml',
        'data/event_attendee.xml',
        'data/lab_test.xml',
        'views/address_code_view.xml',
        'views/document_view.xml',
        'views/community_member_view.xml',
        'views/event_attendee_view.xml',
        'views/lab_test_view.xml',
        'views/employee_view.xml',
        'views/address_reg_state_view.xml',
        'views/address_state_view.xml',
        'views/address_menu_view.xml',
        'wizard/address_mass_edit_view.xml',
        'wizard/address_document_setup_view.xml',
        'wizard/address_lab_test_request_setup_view.xml',
        'wizard/address_street_pattern_add_view.xml',
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
