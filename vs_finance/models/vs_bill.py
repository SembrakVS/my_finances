from odoo import fields, models


class Bill(models.Model):
    _name = 'vs.bill'
    _description = 'Bill'
    _inherit = 'vs.unique.name.mixin'

    name = fields.Char(string='Name', required=True)
    amount = fields.Float(string='Amount', digits=(10, 2), default=0.0)

    expense_ids = fields.One2many('vs.expense', 'bill_id', string='Expenses')
    income_ids = fields.One2many('vs.income', 'bill_id', string='Incomes')
