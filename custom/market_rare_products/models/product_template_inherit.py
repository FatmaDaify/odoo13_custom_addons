# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    rare_list = fields.Boolean(string='Rare List', default=False)
    max_allowed_order_qty = fields.Float(string='Max Allowed Order Qty')

    @api.onchange('rare_list')
    def clear_max_allowed_order_qty(self):
        for product in self:
            if not product.rare_list:
                product.max_allowed_order_qty = 0

    @api.constrains('max_allowed_order_qty')
    def check_max_allowed_order_qty(self):
        for product in self:
            if product.max_allowed_order_qty < 0:
                raise ValidationError(_('Max allowed order qty must be positive value'))
