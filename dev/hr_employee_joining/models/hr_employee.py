from odoo import models, fields, api
from odoo.exceptions import UserError

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    invited = fields.Boolean('Invited', default=False)
    joined = fields.Boolean('Joined', default=False)
    additional_detail_ids = fields.One2many('employee.additional.detail', 'employee_id', string='Additional Details')
    def send_invitation_email(self):
        template = self.env.ref('hr_employee_joining.email_template_invite_employee', raise_if_not_found=False)
        if not template:
            raise UserError('Email template not found. Please check the configuration.')

        for employee in self:
            if not employee.work_email:
                raise UserError('Employee does not have a valid email address.')

            template.with_context(employee_id=employee.id).send_mail(employee.id, force_send=True)

            employee.invited = True


