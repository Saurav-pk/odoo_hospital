{
    'name': 'Odoo Inheritence',
    'version': '1.0',
    'category': 'Category',
    'summary': 'Module Summary',
    'description': """
    Module Description
    """,
    'author': 'saurav',
    'website': 'www.hospital.com',
    'depends': ['base'],
    'data': [
        'views/view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
