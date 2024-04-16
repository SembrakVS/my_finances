from odoo import fields
from odoo.tests.common import TransactionCase


class TestIncome(TransactionCase):

    def setUp(self):
        super(TestIncome, self).setUp()
        self.income_model = self.env['vs.income']

    def test_create_income(self):
        # Створити тестові дані
        income_category = self.env['vs.income.category'].create({
            'name': 'Test Income Category'
        })

        income = self.income_model.create({
            'operation_date': fields.Datetime.now(),
            'currency_id': self.env.ref('base.USD').id,
            'sum': 100.0,
            'category': 'income',
            'category_income': income_category.id,
            'source_income': 'salary'
        })

        # Перевірити, чи створений дохід
        self.assertTrue(income.id, "Income record is not created")

        # Перевірити, чи встановлені значення категорії доходу та джерела доходу
        self.assertEqual(income.category_income.id, income_category.id, "Income category is not set correctly")
        self.assertEqual(income.source_income, 'salary', "Income source is not set correctly")

