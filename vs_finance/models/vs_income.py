from odoo import fields, models


class Income(models.Model):
    _name = 'vs.income'
    _description = 'Sources Income'
    _inherit = 'vs.finans.mixin'

    source_income = fields.Selection(
        selection=[
            ('salary', 'Salary'),
            ('deposits', 'Deposits'),
            ('savings', 'Savings')],
        default='salary'
    )
