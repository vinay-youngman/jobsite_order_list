# -*- coding: utf-8 -*-
{
    'name': "jobsite_order_list",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'jobsites', 'quotations_orders'],

    'data': [
        #'security/ir.model.access.csv',
        'data/cron_jobsite_marker_color_sync.xml',
        'views/jobsite_order_list.xml',
    ],

    'demo': [
    ],
}
