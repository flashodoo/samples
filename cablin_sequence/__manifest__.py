{
    "name": "Test control",
    "version": "12.0.1.2.0",
    "category": "Test Form",
    "license": "AGPL-3",
    "summary": "A generic Test Form.",
    "author": "Test team, "
              "Community Team",
    "website": "www.odoo.com",
    "depends": [
        "base",
    ],
    "data": [
        "data/quality_control_data.xml",
        "security/ir.model.access.csv",
        "views/qc_menus.xml",
		"views/flash_productos_view.xml",
		"views/flash_ventas_facturas_view.xml",
    ],
    "installable": True,
}
