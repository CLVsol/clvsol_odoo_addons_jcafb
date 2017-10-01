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
    'name': 'Animal Management (for CLVhealth-JCAFB Solution)',
    'summary': 'Animal Management Module for CLVhealth-JCAFB Solution.',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_animal_jcafb',
    ],
    'data': [
        'security/animal_mng_security.xml',
        'security/ir.model.access.csv',
        'views/animal_mng_view.xml',
        'views/global_tag_view.xml',
        'views/animal_mng_state_view.xml',
        'views/animal_mng_log_view.xml',
        'views/animal_mng_menu_view.xml',
        'wizard/animal_mng_address_confirm_view.xml',
        'wizard/animal_mng_animal_confirm_view.xml',
        'wizard/animal_mng_address_create_view.xml',
        'wizard/animal_mng_animal_create_view.xml',
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
