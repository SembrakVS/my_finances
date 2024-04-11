from odoo import fields, models


class Expense(models.Model):
    _name = 'vs.expense'
    _description = 'Expense'
    _inherit = 'vs.finans.mixin'

    category = fields.Many2one('vs.expense.category', string='Expense Category')
