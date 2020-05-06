# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Export External Sync (for CLVhealth-JCAFB Solution)',
    'summary': 'Export External Sync Module used in CLVhealth-JCAFB Solution.',
    'version': '12.0.4.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_export_jcafb',
        'clv_external_sync',
    ],
    'data': [
        'data/ir_model_sync.xml',
        'data/ir_model_fields_sync.xml',
        'data/model_export_template_sync.xml',
        'data/model_export_template_field_sync.xml',
        'data/model_export_template_document_item_sync.xml',
        'data/model_export_template_lab_test_criterion_sync.xml',
        'data/model_export_sync.xml',
        # 'data/model_export_field_sync.xml',
        # 'data/model_export_document_item_sync.xml',
        # 'data/model_export_lab_test_criterion_sync.xml',
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
