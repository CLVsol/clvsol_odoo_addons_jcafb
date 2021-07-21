# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Residence (Community) (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Residence (Community)Module customizations for CLVhealth-JCAFB Solution.',
    'version': '14.0.5.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_residence_jcafb',
        'clv_address_jcafb',
        'clv_family_jcafb',
        'clv_document',
        'clv_event',
        'clv_lab_test',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/document_associate_from_address_to_residence_view.xml',
        # 'wizard/document_associate_from_family_to_residence_view.xml',
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
