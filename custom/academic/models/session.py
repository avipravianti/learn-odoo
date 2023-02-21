from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import timedelta, datetime, date
import time


class Session(models.Model):
    _name = 'academic.session'
    _description = 'Academic Session'

    name = fields.Char("Name", required=True)
    course_id = fields.Many2one(
        comodel_name="academic.course", string="Course", required=False)
    instructor_id = fields.Many2one(
        comodel_name="res.partner", string="Instructor", required=False)
    start_date = fields.Date(string="Start Date", required=False, default=lambda self:time.strftime("%Y-%m-%d"))
    duration = fields.Integer(string="Duration", required=False)
    seats = fields.Integer(string="Seats", required=False)
    active = fields.Boolean(string="Active", default=True)
    attendee_ids = fields.One2many(
        comodel_name="academic.attendee", inverse_name="session_id", string="Attendees", required=False, ondelete="cascade")
    taken_seats = fields.Float(compute="_calc_taken_seats", string="Taken Seat", required=False)

    @api.depends('attendee_ids','seats')
    def _calc_taken_seats(self):
        for rec in self:
            if rec.seats > 0:
                rec.taken_seats = 100.0 * len(rec.attendee_ids)/rec.seats
            else:
                rec.taken_seats = 0.0

    @api.onchange('seats')
    def onchange_seats(self):
        if self.seats > 0:
            self.taken_seats = 100.0 * len(self.attendee_ids)/self.seats
        else:
            self.taken_seats = 0.0

    @api.constrains('instructor_id','attendee_ids')
    def _check_instructor(self):
        for session in self:
            x = [att.partner_id.id for att in session.attendee_ids]
            if session.instructor_id.id in x:
                raise ValidationError('Instructor cannot be Attendee')
        return True
    
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {}, name = _('Copy of %s') % self.name)
        return super(Session,self).copy(default=default)
