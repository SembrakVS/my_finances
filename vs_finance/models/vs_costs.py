from odoo import fields, models


class Costs(models.Model):
    _name = 'vs.costs'
    _description = 'Costs'
    _inherit = ['product.product', 'vs.finans.mixin']

    costs = fields.Char()
