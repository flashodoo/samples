
from odoo import api, exceptions, fields, models, _


class FlashFicherosProductos(models.Model):
    _name = 'flash.productos'
    _description = 'Productos'

    name = fields.Char('Articulo')

    precio = fields.Char('Precio', required=True, default="0",translate=False)

    active = fields.Boolean(
        string='Active', default=True,
        help="This field...")
