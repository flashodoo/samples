
from odoo import api, exceptions, fields, models, _
from datetime import datetime, date
import odoo.addons.decimal_precision as dp

class FlashVentasFacturas(models.Model):
    """
    Invoicesmain form
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

    cliente = fields.Many2one('flash.clientes', required=True, string='Cliente')
    serie = fields.Selection(
        [('a', 'A'),
        ('b', 'B')],
        string='Serie', size=5, required=True, default='a')
    active = fields.Boolean('Active', default=True)
    date = fields.Date(
        string='Fecha', required=True, default=fields.Date.today())
    #default=fields.Date.now
    factura_lineas = fields.One2many(
        comodel_name='flash.ventas.facturas.lineas', inverse_name='test',
        string='Questions', copy=True)
			
class FlashVentasFacturasLineas(models.Model):
    """Lines form """
    _name = 'flash.ventas.facturas.lineas'
    _description = 'Lineas'
    _order = 'sequence, id'

    sequence = fields.Integer(
        string='Sequence', required=True, default="10")

    articulo = fields.Many2one('flash.productos', required=True, string='Articulo')

    precio = fields.Float(string='Precio', required=True, digits=dp.get_precision('Productos Precio'))
		
    @api.onchange('articulo')
    def onchange_articulo(self):
        precio = self.articulo.precio
        self.precio = precio

    test = fields.Many2one(comodel_name='flash.ventas.facturas', string='Test')
    cantidad = fields.Integer(
        string='Cantidad', required=True, default="1")
   
    
