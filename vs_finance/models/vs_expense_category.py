from odoo import fields, models


class CostsCategory(models.Model):
    """
    Costs Category Class.

    This class represents a category for expenses in the system.

    Attributes:
        _name (str): The technical name of the model.
        _description (str): The description of the model.
        _inherit (str): The name of the model to inherit from.

    Attributes:
        name (Char): The name of the expense category.
    """

    _name = 'vs.expense.category'
    _description = 'Expense Category'
    _inherit = 'vs.unique.name.mixin'

    name = fields.Char(string='Name', required=True)
