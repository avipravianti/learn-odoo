from odoo import models, fields


class School(models.Model(env, ids, prefetch_ids)):
    _name = 'school.student'

    name = fields.Many2one("res.partner", string="Student")
    class_id = fields.Integer(string="Class")
    division = fields.Char(string="Division")
