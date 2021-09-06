# -*- coding: utf-8 -*-
from odoo import models, fields
import datetime


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Properties of Real Estate"

    name = fields.Char(required=True, string='物业名称')
    description = fields.Text(string='物业描述')
    postcode = fields.Char(string='邮编')
    date_availability = fields.Date(string='交易时间范围', copy=False) #, default=lambda self: fields.Datetime(fields.Date.today() + datetime.timedelta(days=30))
    expected_price = fields.Float(required=True, string='期望价格')
    selling_price = fields.Float(string='销售价格', readonly=True, copy=False)
    bedrooms = fields.Integer(string='卧室数量', default=2)
    living_area = fields.Integer(string='起居室面积')
    facades = fields.Integer(string='外立面')
    garage = fields.Boolean(string='是否有车库')
    garden = fields.Boolean(string='是否有花园')
    garden_area = fields.Integer(string='花园面积')
    garden_orientation = fields.Selection([('North', '北'), ('South', '南'), ('East', '东'), ('West', '西')], string='花园朝向')
    active = fields.Boolean(default=True)
