# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class HotelFloor(models.Model):
    _name = 'hotel.floor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Floor'

    name = fields.Char(string='Floor', required=True)
