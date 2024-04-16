from odoo import api, models


class MonthlyFinancialReport(models.AbstractModel):
    _name = 'report.finance'
    _description = 'Monthly Financial Report'

    @api.model
    def _get_report_data(self, start_date, end_date):
        # Отримати всі фінансові операції за заданий період
        financial_operations = self.env['vs.finans.mixin'].search([
            ('operation_date', '>=', start_date),
            ('operation_date', '<=', end_date)
        ])

        # Розділити фінансові операції на витрати та надходження
        income_lines = []
        expense_lines = []

        for operation in financial_operations:
            if operation.category == 'income':
                income_lines.append({
                    'date': operation.operation_date,
                    'category': operation.description,
                    'amount': operation.sum,
                })
            elif operation.category == 'expense':
                expense_lines.append({
                    'date': operation.operation_date,
                    'category': operation.description,
                    'amount': operation.sum,
                })

        return {
            'income_lines': income_lines,
            'expense_lines': expense_lines,
        }

    @api.model
    def _get_report_values(self, docids, data=None):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        report_data = self._get_report_data(start_date, end_date)

        return {
            'doc_ids': docids,
            'doc_model': self.env['vs.finans.mixin'],
            'data': data,
            'docs': report_data,
        }
