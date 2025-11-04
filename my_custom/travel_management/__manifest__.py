{
'name': 'Travels Management',
'version': '1.0.0',
'description': 'The Travels Management',
'summary': 'The Travels Management',
'category': 'All',
'depends': ['base','web', 'contacts' ],
'data': [
        'security/ir.model.access.csv',
        'views/travel_management_views.xml',
],
'images': [],

'license': 'LGPL-3',
'installable': True,
'auto_install': False,
'application': True,
}