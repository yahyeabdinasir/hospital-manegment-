

from odoo import fields, models, api, _
from dateutil import relativedelta
from datetime import date
from odoo.exceptions import ValidationError




class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin', ]
    _description = " Hospital patient"

    name = fields.Char(string="Name", tracking=True)
    age = fields.Integer(string="Age", compute="compute_age", inverse='_inverse_compute_age', search="_search_age",
                         )

    prescription = fields.Html(string="prescriptiom")

    ref = fields.Char(string="reference")
    # ref_number=fields.Integer("the reference number" , compute="ref_num_compute")
    active = fields.Boolean(string="active", default=True)
    data_of_birth = fields.Date(string="date of birth")
    is_it_birthday = fields.Boolean(string="is birthday", compute="_compute_is_it_birthday")

    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="gender", tracking=True)

    appointment_id = fields.Many2one('hospital.appointment', string=' appointment Patient')
    # appointment_id = fields.One2many('hospital.appointment', "product_id", string='Patient')
    booking_Time = fields.Datetime(string='booked day', default=fields.Datetime.now, )
    image = fields.Image(string="image")
    tag_ids = fields.Many2many("hospital.patient_tag", string="tag id")
    appoitment_count = fields.Integer(string="appo"
                                             "intment count ", compute="_compute_appointment_count"
                                                                      , stored=True)
    appoitment_ids = fields.One2many("hospital.appointment", "patient_id", string="appoitnments")
    operation_fields = fields.Many2one("odoo.operations" , string="operation")

    parent_name = fields.Char(string="parent name ")
    material_status = fields.Selection([('maried', 'maried'), ('single', 'single')])
    partner_name = fields.Char(string="partner name ")

    phone = fields.Char(string="phone ")
    email = fields.Char(string="email")
    websites = fields.Char(string="website")

    #
    # # this is the how to access how many appointment each patient  has it by using python method
    @api.depends("appoitment_ids")
    def _compute_appointment_count(self):
        for rec in self:
            rec.appoitment_count = len(rec.appoitment_ids)
            # we can get the counting of the patient who has the appointment inside of the patiend form view
            # self.env['hospital.appointment'].search_count([('patient_id', "=", rec.id)])

    # this is the how to access how many appointment each patient  has it by using orm in odoo
    # @api.depends("appoitment_ids")
    # def _compute_appointment_count(self):
    #     # print("self ", self)
    #     for rec in self:
    #         appointment_group= self.env['hospital.appointment'].read_group(
    #             domain=[], fields=['patient_id'], groupby=['patient_id'])
    #         # print(appointment_group)
    #         for appointments in  appointment_group:
    #             # print('.................',appointments) # and this will loop through the each record and this stuffs
    #             # print("appointment", appointments.get('patient_id')[0]) # nad here we extract then the record that we have iterated so far the id
    #            # so here there s eror that arises the record that are the flase means they don't have the appointment
    #
    #         # if pick_them :
    #         #    print(pick_them[0])
    #         # else:
    #         #     print("the record is false", )
    #
    #
    #
    #
    #             patient_id = appointments.get('patient_id')[0]
    #             # print(patient_id)
    #             patietn_rec=self.browse(patient_id)
    #             patietn_rec.appoitment_count=appointments["patient_id_count"]
    #             self-=patietn_rec
    #
    #             # if pick_them :
    #             #    print(pick_them[0])
    #             # else:
    #             #     print("the record is false", )




            self.appoitment_count=10





    @api.model
    def create(self, vals):
        # print("hello odoo mate",vals)
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        if not self.ref:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
            return super(HospitalPatient, self).write(vals)

    # @api.depends('ref_number')
    #
    # def ref_num_compute(self):
    #     for rec in self:
    #         if rec.ref:
    #            rec.ref_number = rec.ref * 10
    #         else:
    #             rec.ref_number=0
    #

    @api.depends('data_of_birth')
    def compute_age(self):
        for rec in self:
            today = date.today()
            if rec.data_of_birth:
                rec.age = today.year - rec.data_of_birth.year
            else:

                rec.age = 0

    # nameget is the prebuilt fuctions that concerns about the  creating the identifier  of the model and that identifier will refenrnce each reacord
    # like selcting the reciord through the many2one record

    def name_get(self):
        result = []
        for rec in self:
            display_name = (f"{rec.name or ''} - {rec.ref or ''}")
            result.append((rec.id, display_name))
        return result


    # this is the what that can we referance the patient name and reference both when we are on the appointment

    @api.constrains("data_of_birth")
    def _check_data_of_birth(self):
        for rec in self:
            print("the current day ", fields.Date.today())
            if rec.data_of_birth and rec.data_of_birth > fields.Date.today():
                raise ValidationError(_("that is the fucking validation error"))

    @api.ondelete(at_uninstall=False)
    def appointment_checking(self):
        for rec in self:
            if rec.appoitment_ids:
                raise ValidationError(_("you canot delete the patient who has a appointment "))

    # that means we are just refering out here for sameple the logic that happens out there i mean retreiving the age with the filter
    # it means get the curent date and substract the what user type from the ui  we meant the age filtering
    @api.onchange("age")
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            if rec.age:
                rec.data_of_birth = today - relativedelta.relativedelta(years=rec.age)

    # def _search_age(self, operator, value):
    #     print("hello there ", value)
    #     return [('id', '=', 47)]

    # this is the used to filter the afe of the user based on the user input

    def _search_age(self, operator, value):
        data_of_birth = date.today() - relativedelta.relativedelta(years=value)
        print("hello there ", data_of_birth)
        start_DAte = data_of_birth.replace(day=1, month=1)
        end_Data = data_of_birth.replace(day=30, month=12)
        print("start date ", start_DAte)
        print("end date ", end_Data)
        return [('data_of_birth', '>=', start_DAte), ('data_of_birth', '<=', end_Data)]

    # def _search_age(self, operator, value):
    #     print("are u out there first")
    #     data_of_birth = date.today() - relativedelta.relativedelta(years=value)
    #     return [('data_of_birth', '=', data_of_birth)]

    # this will check if  current day and current month is equal the curent day and month same as the user day and month
    # and if it's that true it will make the condition true else it stays false
    @api.depends("data_of_birth")
    def _compute_is_it_birthday(self):
        for rec in self:

            is_birthday = False

            if rec.data_of_birth:

                today = date.today()
                # print("today day" , today.day)
                # print("rec.data_of_birth.day "  , rec.data_of_birth , rec.data_of_birth.day)
                #
                # print("today.month " ,  today.month)
                # print("rec.data_of_birth.month" , rec.data_of_birth , rec.data_of_birth.month)

                if today.day == rec.data_of_birth.day and today.month == rec.data_of_birth.month:
                    is_birthday = True
            rec.is_it_birthday = is_birthday
            # return  is_birthday

    def button_action_lunch(self):
        return {
            'name': _('appointments'),
            'view_mode': 'list,form,calendar,activity',
            'res_model': 'hospital.appointment',
            'context':{'default_patient_id':self.id},
            'domain':[('patient_id', '=',self.id)],
            'target': "current",
            'type': 'ir.actions.act_window',
        }
