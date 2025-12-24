from odoo import fields, models, api


class ResConfigSettings(models.Model):
    _name = "odoo.operations"
    _descriptions = "odoo opearaions"
    _rec_name = 'operation_name'
    _log_access=False
    _order = 'sequence,id'



    operation_name = fields.Char(string="operations")
    operation = fields.Char(string="operations")
    reference_Record = fields.Reference(selection=[('hospital.patient', 'patient'),
                                                   ('hospital.appointment', 'appointment'),

                                                   ], string="record")
    sequence=fields.Integer(string="sequance" , default=10)

    # this is here we use when we need to create the appointment from the patient form by just clicking the create and list that will get crared by using that
    # and it's referencing the operation name



    # we can get this the hr departments model same as this one
    @api.model
    def name_create(self, name):
        return self.create({'operation_name': name}).name_get()[0]
