from odoo import http
from odoo.http import request

class AdditionalDetailController(http.Controller):

    @http.route('/add_additional_detail', type='http', auth='user', website=True)
    def add_additional_detail(self, **kw):
        employee_id = kw.get('employee_id')
        employee = request.env['hr.employee'].browse(int(employee_id))
        return request.render('hr_employee_joining.save_additional_detail_template', {
            'employee': employee,
        })

    @http.route('/save_additional_detail', type='http', auth='user', website=True)
    def save_additional_detail(self, **post):
        employee_id = post.get('employee_id')
        certificate = post.get('certificate')
        certificate_filename = post.get('certificate_filename')

        if not employee_id or not certificate:
            return request.redirect('/my/error/page')

        employee = request.env['hr.employee'].browse(int(employee_id))
        additional_detail = request.env['employee.additional.detail'].create({
            'employee_id': employee.id,
            'certificate': certificate,
            'certificate_filename': certificate_filename,
        })

        return request.redirect('/my/success/page')
