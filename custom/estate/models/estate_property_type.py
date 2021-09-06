# -*- coding: utf-8 -*-
from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Type of state property"

    name = fields.Char(required=True, string="类型名称")
