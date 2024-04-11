from odoo import fields, models


class IncomeCategory(models.Model):
    _name = 'vs.income.category'
    _description = 'Income Category'

    name = fields.Char(string='Name', required=True)
