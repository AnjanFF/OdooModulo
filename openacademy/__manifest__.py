# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Resumen de mi modulo openacademy""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Angel",
    'website': "http://www.miweb.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/templates.xml',
    ],
}
