from odoo import fields, models


class FinansMixin(models.AbstractModel):
    _name = 'vs.finans.mixin'
    _description = 'Finans mixin'
    _inherit = 'res.currency'

    operation_date = fields.Datetime()
    sum = fields.Float(digits=2)
    bill = fields.Many2one('vs.bills')
