from odoo import fields, models


class ModelName(models.Model):
    _name = 'ProjectName.TableName'
    _description = 'Description'
    _inherit = 'res.currency'

    name = fields.Char()
