# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Material Management',
    'version': '1.2',
    'category': 'Storage',
    'author' : 'Rizky Arif',
    'sequence' : -100,
    'summary': 'Material management system',
    'description': """
This module contains feature to manage data material that will be sold by the company
    """,
    'data': [
        'views/menu.xml',
        'views/material_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application' : True,
    'license': 'LGPL-3',
}
