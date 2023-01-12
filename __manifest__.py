# -*- coding: utf-8 -*-
{
    'name': "BTW boeking MIS Report",

    'summary': """
        Create the yearly booking to close the Dutch BTW (VAT)""",

    'description': """
        Create the yearly booking to close the Dutch BTW (VAT)
    """,

    'author': "Bert Driehuis",
    'website': "https://github.com/driehuis/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'mis_builder'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'data/mis.report.btw-booking.xml',
    ],
}
