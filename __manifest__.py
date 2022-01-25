# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'POS Customer Restriction',
    'version' : '1.7',
    'summary': 'This Module allows to restrict customers from loading in point of sale.',
    'sequence': 11,
    'description': """
        This Module allows to restrict customers from loading in point of sale. Customers's visibility can be controlled with a check box ' Available in POS'
    """,
    'category': 'Point of Sale',
    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "https://www.loyalitsolutions.com",
    'depends' : ['base','point_of_sale'],
    'data': [
        'views/res_partner_template.xml', #moved to assests tag
        'views/res_partner_view.xml',
    ],
    'demo': [],
    'assets': {
        'web.assets_backend': [
            'pos_customer_restriction/static/src/js/available.js'
            'pos_customer_restriction/static/src/js/list.js',
            'pos_customer_restriction/static/src/js/fileds.js',
        ],
        'web.assets_qweb': [
            'pos_customer_restriction/static/src/xml/restriction.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'support': "support@loyalitsolutions.com",
}
