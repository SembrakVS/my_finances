from odoo import fields, models


class CustomCurrency(models.Model):
    """
    Custom Currency Model.

    This model extends the standard Odoo res.currency model
    by adding a Many2many relationship with vs.bill to store
    information about bills associated with each currency.

    Attributes:
        _inherit (str): The name of the model to inherit from.
        _name (str): The technical name of the model.
        bill_ids (Many2many): Relationship field to store the associated bills.
    """

    _inherit = 'res.currency'

    bill_ids = fields.Many2many('vs.bill', string='Bills')
