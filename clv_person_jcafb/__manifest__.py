# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Person (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Person Module customizations for CLVhealth-JCAFB Solution.',
    'version': '12.0.4.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_person',
        # 'clv_person_history',
        'clv_document',
        'clv_community',
        'clv_set',
        'clv_event',
        'clv_lab_test',
        'clv_employee',
        'clv_base_jcafb',
        'clv_address_jcafb',
        'clv_family_jcafb',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/person_seq.xml',
        'data/document.xml',
        'data/community_member.xml',
        'data/event_attendee.xml',
        'data/lab_test.xml',
        'data/set_element.xml',
        'views/person_view.xml',
        'views/person_code_view.xml',
        'views/document_view.xml',
        'views/community_member_view.xml',
        'views/set_element_view.xml',
        'views/event_attendee_view.xml',
        'views/lab_test_view.xml',
        # 'views/person_history_view.xml',
        'views/person_reg_state_view.xml',
        'views/person_state_view.xml',
        'views/address_view.xml',
        'views/family_view.xml',
        'wizard/person_mass_edit_view.xml',
        'wizard/person_associate_to_set_view.xml',
        'wizard/person_document_setup_view.xml',
        'wizard/person_lab_test_request_setup_view.xml',
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
