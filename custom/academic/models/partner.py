from odoo import api, fields, models, _

class Partner(models.Model):
    _inherit = 'sale.order'
    _description = 'Partner'

    confirmed_user_id = fields.Many2one('res.users', string="Confirmed User")