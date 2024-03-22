{
    'name': 'Hospital Management System',
    'author': 'Odoo Mates',
    'website': 'www.odoo.com',
    'summary': 'Odoo 16 Development',
    'depends': ['sale', 'board'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/patients.xml',
        'views/doctor.xml',
        'views/appointment.xml',
        'views/settings.xml',
        'views/dashboard.xml',
        'views/patient_template.xml',
        'views/create_patient_template.xml',
        'views/patient_created_template.xml',
        'views/doctor_details.xml',
        'views/list_doctors.xml',
        'views/create_doctor_template.xml',
        'views/doctor_created_template.xml',
        'views/appointments_page.xml'
    ]
}