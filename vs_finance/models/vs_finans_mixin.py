from odoo import api, fields, models
from odoo.exceptions import AccessError


class FinansMixin(models.Model):
    """
    Finans Mixin Class.

    This class represents a mixin for financial operations in the system.

    Attributes:
        _name (str): The technical name of the model.
        _description (str): The description of the model.
    """

    _name = 'vs.finans.mixin'
    _description = 'Finans mixin'

    operation_date = fields.Datetime(
        string='Operation Date',
        required=True)
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        required=True)
    sum = fields.Monetary(
        string='Amount',
        currency_field='currency_id',
        required=True)
    bill_id = fields.Many2one(
        'vs.bill',
        string='Bill')

    description = fields.Text(string='Description')
    category = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense'),
        ('transfer', 'Transfer')
    ], string='Category', default='expense', required=True)

    def compute_balance(self):
        """
        Compute the balance of the financial operations related to the bill.

        Returns:
            float: The balance of the financial operations.
        """
        self.ensure_one()
        # Check if bill is set
        if not self.bill_id:
            return 0.0

        # Get all financial operations for the current bill
        operations = self.env['vs.finans.mixin'].search([('bill_id', '=', self.bill_id.id)])

        # Check if there are operations to process
        if not operations:
            return 0.0

        # Compute total income and expense
        total_income = sum(operation.sum for operation in operations if operation.category == 'income')
        total_expense = sum(operation.sum for operation in operations if operation.category == 'expense')

        # Compute the balance of the bill
        balance = total_income - total_expense

        return balance

    def process_financial_transaction(self):
        """
        Process the financial transaction based on the category.

        This method adjusts the amount of the bill based on the category of the financial transaction.
        """
        # Financial transaction processing logic
        if self.category == 'expense':
            # Add the expense amount to the bill
            self.bill_id.amount += self.sum
        elif self.category == 'income':
            # Deduct the income amount from the bill
            self.bill_id.amount -= self.sum

    @api.model
    def create(self, vals):
        """
        Override the create method to check user permissions.

        Args:
            vals (dict): Dictionary of values to create the record.

        Returns:
            Record: The created record.

        Raises:
            AccessError: If the user does not have permission to create records.
        """
        # Check if the user has permission to create records
        if not self.env.user.has_group('vs_finance.group_financial_user'):
            raise AccessError("You are not allowed to create records in Finans Mixin")

        return super(FinansMixin, self).create(vals)
