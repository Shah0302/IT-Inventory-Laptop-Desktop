{
'name': 'IT_Inventory',
'version': '1.0.0',
'description': 'The IT Inventory',
'summary': 'The IT Inventory',
'category': 'All',
'depends': ['base','web', 'contacts' ],
'data': [
        'security/ir.model.access.csv',
        'views/it_inventory_views.xml',
],
'images': [],

'license': 'LGPL-3',
'installable': True,
'auto_install': False,
'application': True,
}