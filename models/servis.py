from odoo import models, fields

class ServisAlatKesehatan(models.Model):
    _name = 'servis.alat.kesehatan'
    _description = 'Manajemen Servis Alat Kesehatan'
    _order = 'servis_masuk desc'
    _rec_name = 'name'

    name = fields.Char(string='Kode Servis', default="Servis Baru", required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    product_id = fields.Many2one('product.product', string='Alat Kesehatan', required=True)
    technician_id = fields.Many2one('res.users', string='Teknisi', required=True)
    servis_masuk = fields.Datetime(string='Servis Masuk')
    servis_batal = fields.Datetime(string='Servis Batal')
    servis_mulai = fields.Datetime(string='Servis Mulai')
    perkiraan_selesai = fields.Datetime(string='Perkiraan Selesai', required=True)
    servis_gagal = fields.Datetime(string='Gagal Servis')
    servis_selesai = fields.Datetime(string='Servis Selesai')
    servis_keluar = fields.Datetime(string='Servis Keluar')
    problem = fields.Text(string='Keluhan Customer', required=True)
    result = fields.Text(string='Hasil Servis')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('received', 'Diterima'),
        ('cancelled', 'Batal Servis'),
        ('progress', 'Sedang Servis'),
        ('failed', 'Gagal Servis'),
        ('completed', 'Selesai Servis'),
        ('released', 'Dikembalikan'),
    ], string='Status', default='draft')

    def action_received(self):
        self.servis_masuk = fields.Datetime.now()
        self.status = 'received'

    def action_cancel(self):
        self.servis_batal = fields.Datetime.now()
        self.status = 'cancelled'

    def action_progress(self):
        self.servis_mulai = fields.Datetime.now()
        self.status = 'progress'

    def action_failed(self):
        self.servis_gagal = fields.Datetime.now()
        self.status = 'failed'

    def action_completed(self):
        self.servis_selesai = fields.Datetime.now()
        self.status = 'completed'

    def action_released(self):
        self.servis_keluar = fields.Datetime.now()
        self.status = 'released'
