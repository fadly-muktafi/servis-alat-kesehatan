{
    'name': 'Servis Alat Kesehatan',
    'version': '19.0.1.0.0',
    'summary': 'Manajemen Servis Alat Kesehatan',
    'author': 'Fadly Muktafi - Junior Odoo Programmer',
    'category': 'Healthcare',
    'depends': ['base', 'product', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/servis_views.xml',
    ],
    'installable': True,
    'application': True,
}