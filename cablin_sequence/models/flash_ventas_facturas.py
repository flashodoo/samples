
from odoo import api, exceptions, fields, models, _

class FlashVentasFacturas(models.Model):
    """
    The main form
    """
    _name = 'flash.ventas.facturas'
    _description = 'Facturas de Venta'
    _order = "seq_no"

    seq_no = fields.Char('Factura', readonly=True,
                         default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('seq_no', _('New')) == _('New'):
            vals['seq_no'] = self.env['ir.sequence'
                                      ].next_by_code('flash.ventas.facturas'
                                                     ) or _('New')
        return super(FlashVentasFacturas, self).create(vals)
        
    type = fields.Selection(
        [('generic', 'Generico'),
        ('related', 'Relacionado')],
        string='Type', required=True, default='generic')
    active = fields.Boolean('Active', default=True)
    test_lines = fields.One2many(
        comodel_name='flash.ventas.facturas.lineas', inverse_name='test',
        string='Questions', copy=True)
			
class FlashVentasFacturasLineas(models.Model):
    """Lines form """
    _name = 'flash.ventas.facturas.lineas'
    _description = 'Lineas'
    _order = 'sequence, id'

    # Al no tener un xml expecifico salen todos los campos
    sequence = fields.Integer(
        string='Sequence', required=True, default="10")
    name = fields.Char(
        string='Producto', required=True, translate=True)
    test = fields.Many2one(comodel_name='flash.ventas.facturas', string='Test')
    cantidad = fields.Integer(
        string='Cantidad', required=True, default="1")
   
    precio = fields.Integer(
        string='Precio', required=True, default="10")
