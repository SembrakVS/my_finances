from odoo import fields, models


class Expense(models.Model):
    _name = 'vs.expense'
    _description = 'Expense'
    _inherit = 'vs.finans.mixin'

    expense_category = fields.Many2one('vs.expense.category', string='Expense Category')
    partner_id = fields.Many2one('res.partner', string='Partner')
