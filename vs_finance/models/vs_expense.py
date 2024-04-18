from odoo import fields, models


class Expense(models.Model):
    """
    Expense Class.

    This class represents an expense entity in the system.

    Attributes:
        _name (str): The technical name of the model.
        _description (str): The description of the model.
        _inherit (str): The name of the model to inherit from.

    Attributes:
        expense_category (Many2one): The category of the expense.
        partner_id (Many2one): The partner associated with the expense.
    """

    _name = 'vs.expense'
    _description = 'Expense'
    _inherit = 'vs.finans.mixin'

    expense_category = fields.Many2one('vs.expense.category', string='Expense Category')
    partner_id = fields.Many2one('res.partner', string='Partner')
