from odoo import fields, models


class Bill(models.Model):
    """
    Bill Class.

    This class represents a bill entity in the system.

    Attributes:
        _name (str): The technical name of the model.
        _description (str): The description of the model.
        _inherit (str): The name of the model to inherit from.

    Attributes:
        name (Char): The name of the bill.
        amount (Float): The amount of the bill.
        expense_ids (One2many): The expenses related to the bill.
        income_ids (One2many): The incomes related to the bill.
    """

    _name = 'vs.bill'
    _description = 'Bill'
    _inherit = 'vs.unique.name.mixin'

    name = fields.Char(required=True)
    amount = fields.Float(digits=(10, 2), default=0.0)

    expense_ids = fields.One2many('vs.expense', 'bill_id', string='Expenses')
    income_ids = fields.One2many('vs.income', 'bill_id', string='Incomes')
