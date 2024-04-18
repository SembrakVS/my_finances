from odoo import fields, models


class FinancialWizard(models.TransientModel):
    _name = 'vs.financial.wizard'
    _description = 'Financial Wizard'

    operation_date = fields.Datetime(string='Operation Date', required=True, default=fields.Datetime.now)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    amount = fields.Float(string='Amount', digits=(10, 2), required=True)
    bill_id = fields.Many2one('vs.bill', string='Bill')
    description = fields.Text(string='Description')
    category = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense'),
        ('transfer', 'Transfer')
    ], string='Category', default='expense', required=True)

    def action_confirm(self):
        # Виконати логіку підтвердження операції
        self.env['vs.finans.mixin'].create({
            'operation_date': self.operation_date,
            'currency_id': self.currency_id.id,
            'sum': self.amount,
            'bill_id': self.bill_id.id,
            'description': self.description,
            'category': self.category,
        })

        return {'type': 'ir.actions.act_window_close'}
