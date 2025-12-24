from odoo import models, fields, api, _


class PatientTag(models.Model):
    _name = 'hospital.patient_tag'
    _description = 'hospital patient tags'

    name = fields.Char(string="patient name" , trim=False)
    active = fields.Boolean(string=" patient active ", default=True)

    sequance = fields.Integer(string="tsequance namber")
    color = fields.Integer(string="color")
    color2 = fields.Char(string="color 2")

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}

        if not default.get("name"):
            default['name'] = self.name + "(copy)"
        return super(PatientTag, self).copy(default=default)

    _sql_constraints = [
        ('unique_tag_name', 'unique(name,active)', 'State name already exists in the system'),
        ('check_Sequance', 'check(sequance > 0)', 'sequance must be graeter the 0 ')
    ]
