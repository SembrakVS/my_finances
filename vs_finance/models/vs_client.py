from odoo import fields, models


class PartnerExtension(models.Model):
    """
    Extend res.partner model to add custom fields.
    """

    _inherit = 'res.partner'

    contract = fields.Binary()
    """
    Binary field to store the contract of the partner.

    :var string: Contract
    :vartype string: str
    """

    rating = fields.Integer()
    """
    Integer field to store the rating of the partner.

    :var string: Rating
    :vartype string: str
    """
