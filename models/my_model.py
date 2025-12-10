from odoo import models, fields

class MyModel(models.Model):
    _name = "my.module"
    _description = "My Example Model"

    name = fields.Char(required=True)
    description = fields.Text()
