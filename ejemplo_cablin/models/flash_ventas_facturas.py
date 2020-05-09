
from odoo import api, exceptions, fields, models, _

class FlashVentasFacturas(models.Model):
    """
    The main form
    """
    _name = 'flash.ventas.facturas'
    _description = 'Facturas de Venta'

    name = fields.Char('Código', translate=True )

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
