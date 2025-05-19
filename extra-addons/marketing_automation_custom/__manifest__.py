# -*- coding: utf-8 -*-
{
    'name': "Marketing Automation Custom",
    'version': "1.0",
    'summary': "Perluasan otomasi pemasaran: integrasi CRM + Email Marketing",
    'category': 'Marketing',
    'author': "Kelompok K01-G11",
    'depends': [
        'crm',
        'mass_mailing',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/cron_send_campaign.xml',
        'views/marketing_automation_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
