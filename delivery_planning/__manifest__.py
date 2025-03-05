{
    'name': 'Delivery Planning',
    "version": "17.0.1.0.1",
    'summary': 'Schedule automatic validation of deliveries',
    'description': """
        This module allows you to schedule the automatic validation of deliveries.
    """,
    'category': 'Inventory',
    "author": "OUASMI Anas",
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
        'wizard/delivery_planning_wizard_views.xml',
        'data/cron.xml',
    ],
    'images': [
        "static/description/banner.png",

    ],
    'installable': True,
    'application': False,
    'auto_install': False,

}
