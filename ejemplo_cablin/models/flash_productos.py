
from odoo import api, exceptions, fields, models, _


class FlashFicherosProductos(models.Model):
    _name = 'flash.productos'
    _description = 'Productos'

    name = fields.Char('Name', required=True, translate=True)

    active = fields.Boolean(
        string='Active', default=True,
        help="This field allows you to hide the product without removing it.")
