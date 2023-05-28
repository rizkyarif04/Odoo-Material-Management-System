from odoo import fields, models

class Reg_Supplier(models.Model):
    _name = 'material.supplier'
    _description = 'Registering Related Supplier'

    name = fields.Char(string='Related Supplier Name', required=True)
    description = fields.Text(string='Description')