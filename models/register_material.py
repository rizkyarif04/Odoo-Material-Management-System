from odoo import fields, models,api,_
from odoo.exceptions import ValidationError

class Reg_Material(models.Model):
    _name = "material.register"
    _description = "Registering Material"

    code = fields.Char(string='Material Code', required=True)
    name = fields.Char(string='Material Name', required=True)
    type = fields.Selection([
            ('fabric', 'Fabric'),
            ('jeans', 'Jeans'),
            ('cotton', 'Cotton')], string='Material Type', 
            required = True)
    buy_price = fields.Float(string='Material Buy Price', default=0.0, required = True)
    supplier = fields.Many2one('material.supplier', string='Related Supplier', required=True, ondelete="cascade")

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for material in self:
            if material.buy_price < 100:
                raise ValidationError("Material buy price must be 100 or more.")
            
