from odoo import fields, models


class Income(models.Model):
    _name = 'vs.income'
    _description = 'Income'
    _inherit = 'vs.finans.mixin'

    category = fields.Many2one('vs.income.category', string='Income Category')
    source_income = fields.Selection(
        selection=[
            ('salary', 'Salary'),
            ('deposits', 'Deposits'),
            ('savings', 'Savings')],
        default='salary'
    )
