# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'Media File (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Media File Module customizations for CLVhealth-JCAFB Solution.',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_mfile',
        'clv_survey',
        'clv_address_jcafb',
        'clv_person_jcafb',
        'clv_document_jcafb',
        'clv_lab_test_jcafb',
    ],
    'data': [
        'views/mfile_view.xml',
        'views/mfile_reg_state_view.xml',
        'views/mfile_state_view.xml',
        'views/summary_file_system_view.xml',
        'wizard/mfile_updt_view.xml',
        'wizard/mfile_setup_view.xml',
        'wizard/mfile_refresh_view.xml',
        'wizard/mfile_validate_view.xml',
        'wizard/mfile_import_view.xml',
        'wizard/mfile_archive_view.xml',
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
