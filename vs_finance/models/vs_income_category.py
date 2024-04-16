from odoo import api, fields, models
from odoo.exceptions import ValidationError


class IncomeCategory(models.Model):
    _name = 'vs.income.category'
    _description = 'Income Category'
    _inherit = 'vs.unique.name.mixin'

    name = fields.Char(string='Name', required=True)
