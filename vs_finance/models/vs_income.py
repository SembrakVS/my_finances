from odoo import fields, models


class Income(models.Model):
    """
    Income Class.

    This class represents income records in the system.

    Attributes:
        _name (str): The technical name of the model.
        _description (str): The description of the model.
    """

    _name = 'vs.income'
    _description = 'Income'
    _inherit = 'vs.finans.mixin'

    category_income = fields.Many2one(
        'vs.income.category',
        string='Income Category')
    source_income = fields.Selection(
        selection=[
            ('salary', 'Salary'),
            ('deposits', 'Deposits'),
            ('savings', 'Savings')],
        default='salary'
    )
