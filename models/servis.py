from odoo import models, fields

class ServisAlatKesehatan(models.Model):
    _name = 'servis.alat.kesehatan'
    _description = 'Manajemen Servis Alat Kesehatan'
    _order = 'servis_masuk desc'
    _rec_name = 'name'

    name = fields.Char(string='Kode Servis', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    product_id = fields.Many2one('product.product', string='Alat Kesehatan', required=True)
    technician_id = fields.Many2one('res.users', string='Teknisi', required=True)
    servis_masuk = fields.Datetime(string='Kapan Servis Masuk', required=True)
    perkiraan_selesai = fields.Datetime(string='Perkiraan Servis Selesai')
    servis_selesai = fields.Datetime(string='Servis Selesai')
    servis_keluar = fields.Datetime(string='Kapan Servis Keluar')
    complaint = fields.Text(string='Keluhan Customer')
    result = fields.Text(string='Hasil Servis')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'Sedang Servis'),
        ('done', 'Selesai Servis'),
        ('cancel', 'Batal Servis')
    ], string='Status', default='draft')

    def action_progress(self):
        self.status = 'progress'

    def action_done(self):
        self.servis_selesai = fields.Datetime.now()
        self.status = 'done'

    def action_cancel(self):
        self.status = 'cancel'