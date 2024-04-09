from odoo import fields, models


class Bills(models.Model):
    _name = 'vs.bills'
    _description = 'Bills'
    _inherit = 'account.account'

    name = fields.Char()
