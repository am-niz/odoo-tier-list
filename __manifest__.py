# -*- coding: utf-8 -*-
{
    'name': "Pricelist Tiered Pricing",

    'summary': "Enable tiered pricing on products within pricelists.",

    'description': """
This module allows you to set different price tiers for each product within pricelists. 
Activate this module to manage multiple pricing tiers for your products 
based on criteria such as quantity, date, or other conditions.
    """,

    'author': "NIZAMUDHEEN MJ",
    'website': "www.linkedin.com/in/nizamudheen-m-j",

    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_pricelist_item_views.xml',
    ],
    "application": True,
    "sequence": -93,
}
