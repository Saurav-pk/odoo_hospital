from odoo import http
from odoo.http import request


class HospitalAppointmentController(http.Controller):

    @http.route('/hospital/appointments', auth='user', website=True)
    def appointments_page(self, **kw):
        appointments = request.env['hospital.appointment'].sudo().search([])
        return http.request.render('om_hospital.appointments_page', {
            'appointments': appointments,
        })
