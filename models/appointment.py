from odoo import fields, models, api, _

from odoo.fields import Many2one
from odoo.exceptions import ValidationError
import random


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin', ]
    _description = " Hospital appointment"
    _rec_name = 'patient_id'
    _order = 'id desc'

    patient_id = fields.Many2one('hospital.patient', string='Patient', ondelete='cascade', tracking=1)

    booking_Time = fields.Datetime(string='appointment time', default=fields.Datetime.now, )
    booked_Day = fields.Date(string='booked day ', default=fields.Date.context_today, tracking=True)
    duration = fields.Float(string="duration")

    ref = fields.Char(string="reference", help="this is the reference of the appointement record ")

    gender = fields.Selection(related='patient_id.gender', tracking=10)


    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Very High')
    ], string="Priority", tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_cansulation', 'In_cansulation'),
        ('done', 'Done'),
        ('cancell', 'Cancelled'),
        ('review', 'Review')],
        string="Status", default="draft", required=True
    )
    progress = fields.Integer(string="progress", compute="_compute_progress")
    progress_Gauge = fields.Integer(string="progress", compute="_compute_progress")
    pharmacy_ref = fields.Many2one('hospital.pharmacy', string="pharmact reference ")
    prescriptions = fields.Html(string="presription ")
    doctor_id = fields.Many2one('res.users', string="Doctor", tracking=True)
    operations_holds = fields.Many2one('odoo.operations', string="opearations ", tracking=True)

    phamacy_ids = fields.One2many("hospital.pharmacy", "appointment_id", string="pharmacy id ")
    company_id = fields.Many2one('res.company', 'Company',
                                 default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', string="Currency")
    testing_ids = fields.One2many("hospital.test", 'appoinAttacch_id', string="testing ids ")
    hide_sales_price = fields.Boolean(string="hide saled price")

    Total = fields.Monetary(string="Total", compute="_pharmacy_total_compute", store=True, currency_field='currency_id')

    @api.depends('pharmacy_ref.total_amount')

    def _pharmacy_total_compute(self):
        for rec in self:
            rec.Total = rec.pharmacy_ref.total_amount

    @api.onchange('patient_id')
    def onchange_ref(self):
        self.ref = self.patient_id.ref

    def test_python_button(self):
        print("hello yahye how are you doing ")
        return {
            "type": 'ir.actions.act_url',
            # 'url': 'https://www.visit-puntland.com',
            'url': self.prescriptions,
            'target': 'new',
        }

    def action_in_cansulation(self):
        for record in self:
            record.state = 'in_cansulation'

    def action_done(self):
        for record in self:
            record.state = 'done'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'done  successfully ',
                    'type': 'rainbow_man',
                }
            }

    def action_cancell(self):
        action = self.env.ref("om_hospital.action_cancel_appointment_wizard").read()[0]
        return action

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def unlink(self):
        for rec in self:

            if rec.state == 'done':
                raise ValidationError(_("you canot delte the done state "))
            return super(HospitalAppointment, self).unlink()

    @api.depends("state")
    def _compute_progress(self):
        for rec in self:
            if rec.state == 'draft':
                progress = random.randrange(0, 25)
            elif rec.state == 'in_cansulation':
                progress = random.randrange(0, 80)
            elif rec.state == "done":
                progress = 100
            else:
                progress = 0
            rec.progress = progress



    def send_email_template(self):
        template = self.env.ref('om_hospital.appointment_email_sending')
        for rec in self:
            print(" this is the template for email")
            template.send_mail(rec.id, force_send=True)

    def notification_action(self):
        action = self.env.ref('om_hospital.action_hospital_patient')
        # messsage = "hello yahye how is everythign"
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'messgage' : ' so this message will come now under the wharapp chatter icon ',
            'params': {
                'title': _('this is the notification learning' ),
                # 'message': messsage ,
                'message': '%s',
                'links': [{
                    'label': self.patient_id.id,
                    'url': f'#action={action.id}&id={self.patient_id.id}&model=hospital.patient',
                }],
                'sticky': False,

                'next' : {
                    'type': 'ir.actions.act_window',
                    'res_model' :'hospital.patient',
                    'res_id':self.patient_id.id,
                    'views':[(False , 'form')],
                    'target': 'current',





                },

            }

        }

    def action_whatsapp_lunch(self):
        phone = 252907889655
        encode_text = "hey yahye how is your daya going on "

        whatsapp_api = f"https://api.whatsapp.com/send?phone={phone}&text={encode_text}"


        # this line used to track when the user click the whatapp icon  and that will get tracked inside of the message
        self.message_post(body=encode_text , subject="the whatsapp links is created ")

        # whatsapp_api="https://api.whatsapp.com/send?phone=252907889655&text=hello%20from%20yahye"

        return {
            'type': 'ir.actions.act_url',
            'url': whatsapp_api,
            'target': 'new'
        }


class HospitalPharmacy(models.Model):
    _name = "hospital.pharmacy"
    # _inherit = ['mail.thread', 'mail.activity.mixin', ]
    _description = " Hospital pharmacy"


    sl_no = fields.Integer(string="sl_no")
    product_id = fields.Many2one("product.product", required=True)
    price_unit = fields.Float(related='product_id.list_price', )
    qty = fields.Integer(string="quantity", default=1)
    appointment_id = Many2one("hospital.appointment", string="appointment")

    company_currency_id = fields.Many2one('res.currency', related="appointment_id.currency_id", string="Currency")
    total_amount = fields.Monetary(string="Total Amount", compute='_compute_total_amount',
                                   currency_field='company_currency_id', store=True)

    @api.depends("price_unit", "qty")
    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = rec.price_unit * rec.qty


class HospitalTest(models.Model):
    _name = "hospital.test"
    _description = "Hospital Test"

    test_id = fields.Many2one("crm.tag")
    test_number = fields.Integer(string="testing number ")
    testQty = fields.Integer(string=" test quantity", default=1)

    appoinAttacch_id = Many2one("hospital.appointment", string="appointment attach")
