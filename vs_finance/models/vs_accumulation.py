from odoo import fields, models


class PurposeAccumulation(models.Model):
    """
    Purpose Accumulation Class.

    This class represents a purpose accumulation entity in the system.

    Attributes:
        _name (str): The technical name of the model.
        _description (str): The description of the model.
        _inherit (str): The name of the model to inherit from.

    Attributes:
        name (Char): The name of the purpose accumulation.
    """

    _name = 'vs.accumulation'
    _description = 'Purpose Accumulation'
    _inherit = 'vs.finans.mixin'

    name = fields.Char()
