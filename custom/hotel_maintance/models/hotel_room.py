# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Room'

    name = fields.Char(string='Room No.', required=True, copy=False)
    capacity = fields.Integer(string='Capacity', required=True, default=1)
    floor_id = fields.Many2one('hotel.floor', string='Floor', required=True)

    _sql_constraints = [
        ('name_floor_uniq', 'unique(name,floor_id)', 'Room number must be unique!'),
    ]

    @api.constrains('capacity')
    def check_room_capacity(self):
        for room in self:
            if room.capacity <= 0:
                raise ValidationError(_('Room capacity must be greater than zero.'))
