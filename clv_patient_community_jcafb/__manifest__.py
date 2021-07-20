# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Patient (Community) (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Patient (Community)Module customizations for CLVhealth-JCAFB Solution.',
    'version': '14.0.5.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_patient_jcafb',
        'clv_person_jcafb',
        'clv_document',
        'clv_event',
        'clv_lab_test',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/document_associate_from_person_to_patient_view.xml',
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
