# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'description': "",
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
