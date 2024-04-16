{
    'name': 'My_FINANCE',
    'summary': 'Keeping records of personal finances',

    'author': 'Vasyl Sembrak',
    'website': '',

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.0.0.1',

    'depends': [
        'base',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',
        'data/vs_bill_data.xml',
        'data/vs_expense_category_data.xml',
        'data/vs_income_category_data.xml',
        'data/vs_partner_data.xml',
        'views/vs_main_menu.xml',
        'views/vs_finans_mixin_view.xml',
        'views/vs_bill_view.xml',
        'views/vs_expense_view.xml',
        'views/vs_income_view.xml',
        'wizard/vs_financial_wizard_view.xml',
        'reports/report_template.xml',
        'reports/report.xml',
    ],

    'demo': [
        'demo/vs_finans_mixin_demo.xml',
        'demo/vs_expense_demo.xml',
        'demo/vs_income_demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    'images': [
        'static/description/icon.png',
    ],

    'price': 100,
    'currency': 'EUR',
}
