from odoo import models, fields

class EmployeeAdditionalDetail(models.Model):
    _name = 'employee.additional.detail'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    certificate = fields.Binary('Certificate')
    certificate_filename = fields.Char('Certificate Filename')
