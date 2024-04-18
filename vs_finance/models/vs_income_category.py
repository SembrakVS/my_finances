from odoo import fields, models


class IncomeCategory(models.Model):
    """
    Income Category Class.

    This class represents income categories in the system.

    Attributes:
        _name (str): The technical name of the model.
        _description (str): The description of the model.
        _inherit (str): The technical name of the model that this model inherits from.
    """

    _name = 'vs.income.category'
    _description = 'Income Category'
    _inherit = 'vs.unique.name.mixin'

    name = fields.Char(string='Name', required=True)

