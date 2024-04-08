from odoo import fields, models


class ModelName(models.Model):
    _name = 'ProjectName.TableName'
    _description = 'Description'
    _inherit = 'product.product'

    name = fields.Char()
