from odoo import fields, models


class PurposeAccumulation(models.Model):
    _name = 'vs.accumulation'
    _description = 'Purpose Accumulation'
    _inherit = 'vs.finans.mixin'

    name = fields.Char()
