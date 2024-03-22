from odoo import http
from odoo.http import request


class HospitalPatientController(http.Controller):

    @http.route('/hospital/patients', auth='user', website=True)
    def patients_page(self, **kw):
        patients = request.env['hospital.patient'].sudo().search([])
        return http.request.render('om_hospital.patients_page', {
            'patients': patients,
        })

    @http.route('/hospital/create_patient', auth='public', website=True)
    def create_patient(self, **kwargs):
        return http.request.render('om_hospital.create_patient_template')

    @http.route('/hospital/save_patient', auth='public', website=True, methods=['POST'])
    def save_patient(self, **post):
        patient_name = post.get('name')
        patient_age = post.get('age')
        patient_gender = post.get('gender')

        Patient = request.env['hospital.patient']
        patient = Patient.create({
            'name': patient_name,
            'age': int(patient_age),
            'gender': patient_gender
        })

        return http.request.render('om_hospital.patient_created_template', {
            'patient': patient,
        })