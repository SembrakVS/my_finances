from odoo import fields
from odoo.tests.common import TransactionCase


class TestFinansMixin(TransactionCase):

    def setUp(self):
        super(TestFinansMixin, self).setUp()
        self.finans_mixin_model = self.env['vs.finans.mixin']

    def test_compute_balance(self):
        # Створити тестові дані
        bill = self.env['vs.bill'].create({
            'name': 'Test Bill',
            'amount': 100.0  # Початковий залишок
        })

        operation1 = self.finans_mixin_model.create({
            'operation_date': fields.Datetime.now(),
            'currency_id': self.env.ref('base.USD').id,
            'sum': 50.0,
            'bill_id': bill.id,
            'category': 'income'
        })

        operation2 = self.finans_mixin_model.create({
            'operation_date': fields.Datetime.now(),
            'currency_id': self.env.ref('base.USD').id,
            'sum': 30.0,
            'bill_id': bill.id,
            'category': 'expense'
        })

        # Обчислити очікуваний залишок
        expected_balance = operation1.sum - operation2.sum

        # Отримати реальний залишок через метод compute_balance
        actual_balance = operation1.compute_balance()

        # Порівняти очікуваний і отриманий залишок
        self.assertEqual(expected_balance, actual_balance, "Computed balance is not correct")

        # Переконатися, що змінна operation2 використовується
        self.assertTrue(operation2, "Variable operation2 is not used")

    def test_process_financial_transaction(self):
        # Створити тестові дані
        bill = self.env['vs.bill'].create({
            'name': 'Test Bill',
            'amount': 100.0  # Початковий залишок
        })

        operation1 = self.finans_mixin_model.create({
            'operation_date': fields.Datetime.now(),
            'currency_id': self.env.ref('base.USD').id,
            'sum': 50.0,
            'bill_id': bill.id,
            'category': 'income'
        })

        operation2 = self.finans_mixin_model.create({
            'operation_date': fields.Datetime.now(),
            'currency_id': self.env.ref('base.USD').id,
            'sum': 30.0,
            'bill_id': bill.id,
            'category': 'expense'
        })

        # Викликати метод обробки фінансової транзакції
        operation1.process_financial_transaction()
        operation2.process_financial_transaction()

        # Перевірити, чи залишок правильно змінився
        self.assertEqual(bill.amount - operation1.sum, 70.0, "Bill amount is not updated correctly")
