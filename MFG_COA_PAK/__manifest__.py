# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': "Pakistan Chart of Account",
    'summary': """
        Adds Parent account and ability to open chart of account list view based on the date and moves""",
    'description': """
        * Adds parent account in account
        * Adds new type 'view' in account type
        * Adds Chart of account heirachy view
        * Adds credit, debit and balance in account
        * Shows chart of account based on the date and target moves we have selected
    - Need to set the group show chart of account structure to view the chart of account heirarchy.
    
    Contact us for any need of customisation or chart of account .
    """,

    'author': 'Itech Resources',
    'website': 'http://itechresources.net/',
    'category': 'Accounting &amp; Finance',
    'version': '1.2.1',
    'depends': ['base', 'account'],
    'data': [
        'security/account_parent_security.xml',
        'views/account_view.xml',
        'views/open_chart.xml',
        #'data/account_type_data.xml',
        'data/l10n_pak_chart_data.xml',
        #'data/account_chart_template_data.yml',
        'data/account_type_data.xml',
    ],
    'demo': [
    ],
    'price': 30.00,
    'currency': 'EUR',
}
