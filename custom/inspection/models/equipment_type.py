# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EqeuipmentType(models.Model):
    _name = "equipment.type"
    _description = "Equipment Type"
    _parent_store = True
    _parent_name = "parent_id"

    name = fields.Char(required=True, string="类型名称")
    parent_path = fields.Char(index=True)
    parent_id = fields.Many2one('equipment.type', string='父类型', index=True)
    child_ids = fields.One2many('equipment.type', 'parent_id', string='子类型')

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise ValidationError('Error! You cannot create recursive types!')
