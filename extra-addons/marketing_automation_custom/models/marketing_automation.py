from odoo import models, fields, api
from datetime import datetime

class MassMailingCampaign(models.Model):
    _inherit = 'mailing.mailing'

    # menambahkan target stage dari CRM
    crm_stage_id = fields.Many2one(
        'crm.stage', string="Target CRM Stage",
        help="Kirim otomatis saat lead mencapai stage ini"
    )
    auto_send = fields.Boolean(
        string="Auto Send",
        default=False,
        help="Jika dicentang, campaign ini akan dikirim otomatis via cron."
    )

    @api.model
    def _cron_send_campaigns(self):
        """Method yang dipanggil oleh scheduled action untuk
        memproses dan mengirim campaign yang auto_send=True."""
        now = fields.Datetime.now()
        campaigns = self.search([
            ('auto_send', '=', True),
            ('state', '=', 'draft'),
            ('scheduled_date', '<=', now),
        ])
        for camp in campaigns:
            camp.with_context(no_user_input=True).action_send_mail()
            camp.write({'state': 'sent'})


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # relasi many2many ke campaign email_marketing
    campaign_ids = fields.Many2many(
        comodel_name='mailing.mailing',
        relation='crm_lead_mailing_rel',
        column1='lead_id',
        column2='mailing_id',
        string="Linked Email Campaigns",
    )
