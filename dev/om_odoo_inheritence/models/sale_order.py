from odoo import models, fields, api

class SaleOrder(models.Models):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')