from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class Attendee(models.Model):
    _name = 'academic.attendee'
    _rec_name = 'name'
    _description = 'Academic Attendee'

    name = fields.Char("Name")
    session_id = fields.Many2one(
        comodel_name="academic.session", string="Sessions", required=False)
    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Partner", required=False)

    # _sql_constraints = [
    #     ('uniq_id', 'UNIQUE(partner_id,session_id)', 'You cannot insert the same attendee multiple times!'),
    # ]
    # I try to use _sql_constraint but the WARNING show unable to add constrains, so the _sql_constraints did'd work and Validation did't show 

    @api.constrains('partner_id','session_id')
    def _check_unique_partner_session(self):
        for rec in self:
            exist_record = self.search([('partner_id', '=', rec.partner_id.id), ('session_id', '=', rec.session_id.id), ('id', '!=', rec.id)])
            if exist_record:
                raise ValidationError('You cannot insert the same attendee multiple times!')