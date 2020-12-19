# -*- coding: utf-8 -*-
{
    'name': 'Hotel Maintenance',
    'summary': 'Hotel Maintenance',
    'depends': ['base', 'maintenance'],
    'description': """
        This module add parent category in maintenance category and manage hotel maintenance customizations.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_floor_view.xml',
        'views/hotel_room_view.xml',
        'views/maintenance_equipment_inherit_view.xml',
        'views/maintenance_equipment_category_inherit_view.xml',
        'views/menu_item_view.xml',
    ],

}
