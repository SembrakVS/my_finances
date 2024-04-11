from odoo import fields, models


class Bill(models.Model):
    _name = 'vs.bill'
    _description = 'Bill'

    name = fields.Char(string='Name', required=True)
    amount = fields.Float(string='Amount', digits=(10, 2), default=0.0)

    expense_ids = fields.One2many('vs.expense', 'bill', string='Expenses')
    income_ids = fields.One2many('vs.income', 'bill', string='Incomes')
