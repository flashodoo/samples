
from odoo import api, exceptions, fields, models, _

class QcTest(models.Model):
    """
    A test is a group of questions.
    """
    _name = 'qc.test'
    _description = 'Form test'

    # @api.onchange('type')
    # def onchange_type(self):
        # if self.type == 'generic':
            # self.object_id = False

    name = fields.Char(
        string='Name', required=True, translate=True)
    type = fields.Selection(
        [('generic', 'Generic'),
         ('related', 'Related')],
        string='Type', required=True, default='generic')
    company_id = fields.Many2one(
        comodel_name='res.company', string='Company',
        default=lambda self: self.env['res.company']._company_default_get(
            'qc.test'))
