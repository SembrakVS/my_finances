from odoo import fields, models


class CostsCategory(models.Model):
    _name = 'vs.expense.category'
    _description = 'Expense Category'
    _inherit = 'vs.unique.name.mixin'

    name = fields.Char(string='Name', required=True)
