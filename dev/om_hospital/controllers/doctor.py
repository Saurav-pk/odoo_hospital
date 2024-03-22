from odoo import http
from odoo.http import request


class DoctorController(http.Controller):

    @http.route('/hospital/doctor/<int:doctor_id>', auth='public', website=True)
    def doctor_details(self, doctor_id, **kwargs):
        doctor = request.env['hospital.doctor'].browse(doctor_id)
        return request.render('om_hospital.doctor_details_page', {
            'doctor': doctor,
        })

    @http.route('/hospital/doctors', auth='public', website=True)
    def list_doctors(self, **kw):
        doctors = request.env['hospital.doctor'].sudo().search([])
        return http.request.render('om_hospital.list_doctors_page', {
            'doctors': doctors
        })

    @http.route('/hospital/doctor/new', auth='public', website=True)
    def new_doctor_form(self, **kw):
        return http.request.render('om_hospital.create_doctor_template')

    @http.route('/hospital/doctor/create', auth='public', website=True, methods=['POST'])
    def create_doctor(self, **post):
        doctor_name = post.get('name')
        doctor_gender = post.get('gender')
        doctor_ref = post.get('ref')
        doctor_specialization = post.get('specialization')

        Doctor = request.env['hospital.doctor']
        doctor = Doctor.create({
            'name': doctor_name,
            'gender': doctor_gender,
            'ref': doctor_ref,
            'specialization': doctor_specialization
        })

        return http.request.render('om_hospital.doctor_created_template', {
            'doctor': doctor,
        })
