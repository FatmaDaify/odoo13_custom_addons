# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    display_type = fields.Selection(selection_add=[('rare_list', 'Rare List')])

    @api.onchange('display_type')
    def change_product_domain(self):
        if self.display_type == 'rare_list':
            return {'domain': {
                'product_id': [('purchase_ok', '=', True), ('rare_list', '=', True), '|', ('company_id', '=', False),
                               ('company_id', '=', self.order_id.company_id)]}}
