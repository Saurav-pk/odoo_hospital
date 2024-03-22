# from odoo import http
# from odoo.http import request
#
#
# class HospitalController(http.Controller):
#
#     @http.route(['/hospital/patient/'], website=True, auth='public')
#     def hospital_patient(self, **kw):
#         # return "Hello, world"
#         patients = request.env['hospital.patient'].sudo().search([])
#         print("patients---", patients)
#         return request.render("om_hospital.patient_page", {
#             'patients': patients
#         })
