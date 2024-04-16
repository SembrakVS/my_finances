from odoo import fields, models, api
from odoo.exceptions import ValidationError


class UniqueNameMixin(models.AbstractModel):
    _name = 'vs.unique.name.mixin'

    name = fields.Char(string='Name', required=True)

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            if self.search([('name', '=', record.name), ('id', '!=', record.id)]):
                raise ValidationError("Name must be unique!")

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Name must be unique!'),
    ]
