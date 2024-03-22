{
    'name': 'HR Employee Joining',
    'version': '1.0',
    'depends': ['base', 'mail', 'hr'],
    'author': 'Your Name',
    'category': 'Human Resources',
    'description': 'Manage employee joining and details',
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/employee_joining_views.xml',
        'views/employee_invitation_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
