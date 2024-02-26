from odoo import api, fields, models, _

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = 'mail.thread'
    _description = "Doctor Records"
    _rec_name = 'name'

    name = fields.Char(String='Name', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender', tracking=True)

    ref = fields.Char(String="Reference", required=True)
    active = fields.Boolean(default=True)

    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.ref} - {rec.name}'
            res.append((rec.id, name))
        return res
