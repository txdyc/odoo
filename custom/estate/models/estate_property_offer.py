# -*- coding: utf-8 -*-
from odoo import models, fields


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Offers that property owner reveived"

    price = fields.Float(required=True, string="出价")
    status = fields.Selection([('accepted', '接受'), ('refused', '拒绝')])
    partner_id = fields.Many2one("res.partner", string="买家", required=True)
    property_id = fields.Many2one("estate.property", string="物业", required=True)
