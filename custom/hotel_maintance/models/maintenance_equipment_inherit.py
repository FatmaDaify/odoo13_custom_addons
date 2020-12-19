# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import ValidationError


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    next_action_date = fields.Date(string='Date Of Next Preventive Maintenance', compute=False, store=True)
    # equipment card
    partner_location = fields.Char(string='Vendor Location')
    production = fields.Char(string='Production')
    equipment_no = fields.Char(string='Equipment No.')
    type_of_cable = fields.Char(string='Type Of M/C')
    discharge = fields.Char(string='Discharge')

    electric_volt = fields.Float(string='Volt')
    electric_current = fields.Float(string='Current')
    electric_phase = fields.Float(string='Phase')
    electric_power = fields.Float(string='Power In KW')
