# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Employee (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Employee Module customizations for CLVhealth-JCAFB Solution.',
    'version': '12.0.4.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_employee',
        'clv_set',
    ],
    'data': [
        'views/hr_employee_view.xml',
        'views/hr_employee_code_view.xml',
        'views/set_element_view.xml',
        'wizard/hr_employee_mass_edit_view.xml',
        'wizard/hr_employee_associate_to_set_view.xml',
        'data/hr_employee_seq.xml',
        'data/set_element.xml',
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
