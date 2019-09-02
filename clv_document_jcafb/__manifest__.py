# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Document (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Document Module customizations for CLVhealth-JCAFB Solution.',
    'version': '12.0.4.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_base_jcafb',
        'clv_document',
        'clv_survey',
    ],
    'data': [
        'views/document_code_view.xml',
        'views/document_reg_state_view.xml',
        'views/document_state_view.xml',
        'views/document_view.xml',
        'views/document_type_view.xml',
        'data/document_seq.xml',
        # 'wizard/document_updt_view.xml',
        # 'wizard/document_item_edit_view.xml',
        # 'wizard/document_item_updt_from_survey_view.xml',
        # 'wizard/document_type_setup_view.xml',
        'views/document_menu_view.xml',
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
