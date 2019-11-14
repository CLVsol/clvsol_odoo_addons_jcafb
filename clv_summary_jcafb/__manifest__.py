# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Summary (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Summary Module customizations for CLVhealth-JCAFB Solution.',
    'version': '12.0.4.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_summary',
        'clv_document_jcafb',
        'clv_lab_test_jcafb',
        'clv_event_jcafb',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/summary_document_view.xml',
        'views/summary_lab_test_request_view.xml',
        'views/summary_event_view.xml',
        'views/summary_menu_view.xml',
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
