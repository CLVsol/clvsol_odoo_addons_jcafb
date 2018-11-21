# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'JCAFB Surveys (2019)',
    'summary': 'This module will install all the JCAFB surveys (2019).',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_survey_jcafb',
    ],
    'data': [
        'data/document_jcafb_QAN19.xml',
        'data/document_jcafb_QDH19.xml',
        'data/document_jcafb_QMD19.xml',
        'data/document_jcafb_QSC19.xml',
        'data/document_jcafb_QSF19.xml',
        'data/document_jcafb_QSI19.xml',

        'data/document_jcafb_TAN19.xml',
        'data/document_jcafb_TCR19.xml',
        'data/document_jcafb_TDH19.xml',
        'data/document_jcafb_TID19.xml',
        'data/document_jcafb_TCV19.xml',

        'wizard/document_item_edit_TAN19_view.xml',
        'wizard/document_item_edit_TCR19_view.xml',
        'wizard/document_item_edit_TDH19_view.xml',
        'wizard/document_item_edit_TID19_view.xml',
        'wizard/document_item_edit_TCV19_view.xml',
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
