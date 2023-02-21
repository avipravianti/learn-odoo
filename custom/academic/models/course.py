from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class Class(models.Model):
    _name = 'academic.course'
    _rec_name = 'name'
    _description = "Academic Course"

    name = fields.Char("Name")
    description = fields.Text(string="Description", required=False)
    responsible_id = fields.Many2one(
        comodel_name="res.users", string="Responsible")
    session_ids = fields.One2many(
        comodel_name="academic.session", inverse_name="course_id", string="Sessions", required=False, ondelete="cascade")
    
    # @api.constrains('name','description')
    # def _check_name_desc(self):
    #     for rec in self:
    #         if rec.name == rec.description:
    #             raise ValidationError('Fields name and description must be different')
    
    _sql_constraints = [
        (
            'uniq_name', 
            'UNIQUE(name)', 
            'Name is already used',
        ),
        (
            'cek_nama_desc', 
            'CHECK(name <> description)', 
            'Fields name and description must be different',
        )
    ]
