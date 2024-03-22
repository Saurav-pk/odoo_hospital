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
    'depends': ['base', 'sale', 'sale_stock'],
    'data': [
        'views/sale_order_view.xml',
        'views/employee_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
