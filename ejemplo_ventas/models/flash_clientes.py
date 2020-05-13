
from odoo import api, exceptions, fields, models, _


class FlashFicherosProductos(models.Model):
    _name = 'flash.clientes'
    _description = 'Clientes'
    _order = 'active'

    name   = fields.Char('Name', required=True, translate=True)
    cPhone = fields.Char('Phone', required=False, translate=True)
    cEmail = fields.Char('Email', required=False, translate=True)

    active = fields.Boolean(
        string='Active', default=True,
        help="This field allows you to hide the customer without removing it.")
