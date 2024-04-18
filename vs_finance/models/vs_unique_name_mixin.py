from odoo import fields, models, api
from odoo.exceptions import ValidationError


class UniqueNameMixin(models.AbstractModel):
    """
    Unique Name Mixin Class.

    This class provides functionality to ensure that the 'name' field is unique across records.

    Attributes:
        _name (str): The technical name of the model.
    """

    _name = 'vs.unique.name.mixin'

    name = fields.Char(string='Name', required=True)

    @api.constrains('name')
    def _check_unique_name(self):
        """
        Check Unique Name Constraint.

        This method checks if the 'name' field is unique among records.

        Raises:
            ValidationError: If a record with the same 'name' already exists.
        """
        for record in self:
            if self.search([('name', '=', record.name), ('id', '!=', record.id)]):
                raise ValidationError("Name must be unique!")

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Name must be unique!'),
    ]
