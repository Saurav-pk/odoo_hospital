from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

 
class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = 'mail.thread'
    _description = "Patient Records"

    name = fields.Char(String='Name', required=True, tracking=True)
    age = fields.Integer(String="Age", tracking=True)
    is_Child = fields.Boolean(String="Is Child ?", tracking=True)
    notes = fields.Text(String="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender',
                              tracking=True)
    capitalized_name = fields.Char(String='Capitalized Name', compute='_compute_capitalized_name', store=True)
    ref = fields.Char(String="Reference", default=lambda self: _('New'))
    doctor_id = fields.Many2one("hospital.doctor", string="Doctor")
    tag_ids = fields.Many2many('res.partner.category', 'hospital_patient_tag_rel', 'patient_id', 'tag_id',
                               string="Tags")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals_list)

    @api.constrains('is_child', 'age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_Child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded !"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ""

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_Child = True
        else:
            self.is_Child = False
