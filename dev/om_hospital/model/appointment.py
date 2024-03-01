from odoo import api, models, fields, _


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = 'mail.thread'
    _description = "Appointments"

    name = fields.Many2one("hospital.patient", string="Patient", required=True)
    doctor = fields.Many2one("hospital.doctor", string="Doctor", required=True)
    appointment_date = fields.Date(string="Appointment Date", required=True)
    appointment_time = fields.Selection([('09:00', '9:00 AM'), ('09:30', '9:30 AM'), ('10:00', '10:00 AM')],
                                        string="Appointment Time", tracking=True)
    active = fields.Boolean(default=True)
