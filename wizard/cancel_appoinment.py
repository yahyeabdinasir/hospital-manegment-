from odoo import models, fields, api, _
import datetime
from odoo.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class cancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'cancel Appointment Wizard'

    @api.model
    def default_get(self, fields_list):


        res = super(cancelAppointmentWizard, self).default_get(fields_list)
        res["cancellTime"] = datetime.date.today()
        res["cancel_appointment"] = self.env.context.get("active_id")



        return res
        print("this are the all values from there",fields_list)

        # change_note= super(cancelAppointmentWizard, self).default_get(fields_list)
        # change_note["reason"]=date.today()+relativedelta(weekday=1)
        #
        # return   change_note

    cancel_appointment = fields.Many2one('hospital.appointment', string="appointment ",

                                         )
    # domain = "[('state','=','done') ,('priority', 'in' ,('0','1'))]"
    reason = fields.Text(string="type the  reason ")
    cancellTime = fields.Date(string="cancellation date")

    def action_launch(self):
        # the logic that happinig here its that what the user have strored from the ir.confg. _system_parameter
        # and substract the from the day that user input as a booked day from the appointment day so that day substract from
        # the cancellation variable from the conf system  and if that substract less than the curent day throw the validation error

        cancell_Days = self.env['ir.config_parameter'].get_param('om_hospital.cancellation_Days')
        allowad_date = self.cancel_appointment.booked_Day - relativedelta(days=int(cancell_Days))
        #
        # query = """ select id,patient_id from hospital_appointment where id = %s   """ % self.cancel_appointment.id
        # yyyy = self.env.cr.execute(query)
        # # mmmm = self.env.cr.fetchall()
        # print("thi ", yyyy)
        #
        # query = """select id , name  , partner_id , date_order    from sale_order """
        # mmmm = self.env.cr.execute(query)
        # print(mmmm)
        # mmmm = self.env.cr.fetchall()
        # print("thi ", mmmm)

        #
        #
        #
        #
        # query = """ select *  from hospital_patient  """
        # self.env.cr.execute(query)
        # mmmm = self.env.cr.fetchall()
        # print("thi ", mmmm)
        #
        #
        query = """ select id,name from hospital_patient"""
        self.env.cr.execute(query)
        patient = self.env.cr.dictfetchall()
        print("this is the record patient ", patient)

        print(self.cancel_appointment.booked_Day)
        if allowad_date > date.today():
            today = date.today()
            print( "  cancell days",cancell_Days)
            print("allow date ", allowad_date)
            print(" today ", today)
            raise ValidationError(_("sorry cancellation is not allowed "))
        # return allowad_date
        self.cancel_appointment.state = "cancell"

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'cancel.appointment.wizard',
            'target': 'new',
            'res_id': self.id,
        }

        # this only access the record from the hospital_patient
        # query = """ select name from hospital_patient"""

        # 11 / 11/ 2025
        # 11/3/2025






        # return {
        #     'type': 'ir.actions.client',
        #     'tag': 'reload',
        # }

# if self.cancel_appointment.booked_Day == datetime.date.today():
#     raise ValidationError(_("sorry cancellation is not allowed "))
# return
