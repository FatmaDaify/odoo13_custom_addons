# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import ValidationError


class MaintenanceEquipmentCategory(models.Model):
    _inherit = 'maintenance.equipment.category'
    _parent_name = "parent_id"
    _parent_store = True

    parent_id = fields.Many2one('maintenance.equipment.category', string='Parent Category')
    parent_path = fields.Char(index=True)

    @api.depends('name', 'parent_id.name')
    def name_get(self):
        res = []
        for category in self:
            name = category.name
            if category.parent_id.name:
                name = '%s / %s' % (category.parent_id.name, category.name)
            res.append((category.id, name))
        return res

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))
        return True

