# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Media File (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Media File Module customizations for CLVhealth-JCAFB Solution.',
    'version': '4.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_mfile',
        # 'clv_survey',
        # 'clv_address_jcafb',
        # 'clv_person_jcafb',
        'clv_document_jcafb',
        # 'clv_lab_test_jcafb',
        'clv_file_system',
    ],
    'data': [
        'data/file_system.xml',
        'views/mfile_view.xml',
        'views/mfile_state_view.xml',
        'views/document_view.xml',
        'views/file_system_view.xml',
        # 'wizard/mfile_updt_view.xml',
        # 'wizard/mfile_setup_view.xml',
        # 'wizard/document_mfile_setup_view.xml',
        # 'wizard/mfile_refresh_view.xml',
        # 'wizard/mfile_validate_view.xml',
        # 'wizard/mfile_import_view.xml',
        # 'wizard/mfile_archive_view.xml',
        # 'wizard/mfile_unarchive_view.xml',
        # 'wizard/mfile_directory_refresh_view.xml',
        # 'wizard/mfile_verify_view.xml',
        'views/mfile_menu_view.xml',
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
