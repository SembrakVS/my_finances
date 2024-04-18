from odoo import fields
from odoo.tests.common import TransactionCase


class TestExpense(TransactionCase):

    def setUp(self):
        super(TestExpense, self).setUp()
        self.expense_model = self.env['vs.expense']

    def test_create_expense(self):
        # Створити тестові дані
        expense_category = self.env['vs.expense.category'].create({
            'name': 'Test Category'
        })

        partner = self.env['res.partner'].create({
            'name': 'Test Partner'
        })

        expense = self.expense_model.create({
            'operation_date': fields.Datetime.now(),
            'currency_id': self.env.ref('base.USD').id,
            'sum': 100.0,
            'category': 'expense',
            'expense_category': expense_category.id,
            'partner_id': partner.id
        })

        # Перевірити, чи створений витрату
        self.assertTrue(expense.id, "Expense record is not created")

        # Перевірити, чи встановлені значення категорії витрат та партнера
        self.assertEqual(expense.expense_category.id, expense_category.id,
                         "Expense category is not set correctly")
        self.assertEqual(expense.partner_id.id, partner.id,
                         "Partner is not set correctly")
