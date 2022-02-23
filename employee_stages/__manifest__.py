# -*- coding: utf-8 -*-

{
    'name': 'Employee Stages',
    'version': '15.0.1.0.0',
    'summary': """Manages Employee Stages""",
    'description': """This module is used to tracking employee's different stages.""",
    'category': "Generic Modules/Human Resources",
    'author': 'ABC',
    'company': 'abc',
    'website': "https://www.abc.com",
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_stages_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
