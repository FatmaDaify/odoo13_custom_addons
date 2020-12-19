# -*- coding: utf-8 -*-
{
    'name': 'Sale Custom Reports',
    'summary': 'Sale Custom Reports',
    'depends': ['base', 'sale_management', 'sale_stock'],
    'description': """
        This module add new reports in sale and invoices.
    """,
    'data': [
        'report/custom_layout_view.xml',
        'report/sale_order_report_inherit.xml',
        'report/account_invoice_report_inherit.xml',
        'report/order_acknowledgement_report.xml',
        'views/sale_order_inherit_view.xml',
        'views/menu_item_view.xml',
    ],

}
