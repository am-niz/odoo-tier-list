# -*- coding: utf-8 -*-
{
    'name': "Price Tire List",

    'summary': "On pricelist every product have tires of price list",

    'description': """
By activating this module you can set different price list i mean tieres of price list for each products
    """,

    'author': "NIZAMUDHEEN MJ",
    'website': "www.linkedin.com/in/nizamudheen-m-j",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
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

