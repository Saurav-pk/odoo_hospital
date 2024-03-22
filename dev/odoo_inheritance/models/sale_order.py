from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    java = fields.Char(String='Name', required=True, tracking=True)
    python = fields.Char(String='Name', required=True, tracking=True)

    # @api.model
    # def create(self, vals):
    #     # Set partner_id to a valid partner ID
    #     vals['partner_id'] = 1  # Replace 1 with the actual partner ID
    #     return super(SaleOrder, self).create(vals)


class Project(models.Model):
    _inherit = 'hr.employee'

    description = fields.Char(String='Name', required=True, tracking=True)

