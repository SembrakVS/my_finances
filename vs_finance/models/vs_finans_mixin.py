from odoo import fields, models


class FinansMixin(models.Model):
    _name = 'vs.finans.mixin'
    _description = 'Finans mixin'

    operation_date = fields.Datetime(string='Operation Date', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    sum = fields.Monetary(string='Amount', currency_field='currency_id', required=True)
    bill = fields.Many2one('vs.bill', string='Bill')

    description = fields.Text(string='Description')
    category = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense'),
        ('transfer', 'Transfer')
    ], string='Category', default='expense', required=True)

    def compute_balance(self):
        # Перевірити, чи встановлено значення для рахунку
        if not self.bill:
            return 0.0

        # Отримати всі фінансові операції для поточного рахунку
        operations = self.env['vs.finans.mixin'].search([('bill', '=', self.bill.id)])

        # Перевірити, чи є операції для обробки
        if not operations:
            return 0.0

        # Обчислити суму витрат і доходів
        total_income = sum(operation.sum for operation in operations if operation.category == 'income')
        total_expense = sum(operation.sum for operation in operations if operation.category == 'expense')

        # Обчислити залишок на рахунку
        balance = total_income - total_expense

        return balance

    def process_financial_transaction(self):
        # Логіка обробки фінансової транзакції
        if self.category == 'expense':
            # Додати суму витрат на рахунок
            self.bill.amount += self.sum
        elif self.category == 'income':
            # Відняти суму доходу з рахунку
            self.bill.amount -= self.sum
