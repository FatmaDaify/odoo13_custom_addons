{
    'name': 'Market Rare Products',
    'summary': 'Market Rare Products',
    'version': '1.0',
    'category': 'Warehouse',
    'depends': ['base', 'purchase_stock', 'point_of_sale'],
    'data': [
        'views/product_template_inherit_view.xml',
        'views/purchase_order_inherit_view.xml',
        'views/pos_rare_product_templates.xml',
    ],

    'qweb': [
        'static/src/xml/rare_product_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
}
