from odoo import api, fields, models


class EpidemicRecord(models.Model):
    _name = "epidemic.record"
    _description = "Epidemic Record"

    # 姓名、日期、省、市、区/县、性别、年龄、就业状态、具体地址、感染方式、境内/境外感染
    name = fields.Char(string='姓名')
    date = fields.Date(string='确诊日期')
    state = fields.Char(string='省')
    city = fields.Char(string='市')
    county = fields.Char(string='区/县')
    gender = fields.Selection([('female', '女'), ('male', '男')], string='性别')
    birthdate = fields.Date(string='出生日期')
    street = fields.Char(string='具体地址')
    affect_type = fields.Char(string='感染方式')
    within_or_abroad = fields.Selection([('within', '境内'), ('abroad', '境外')], string='境内/境外感染')