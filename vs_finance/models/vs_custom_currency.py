from odoo import fields, models


class CustomCurrency(models.Model):
    _inherit = 'res.currency'

    bill_ids = fields.Many2many('vs.bill', string='Bills')
