# -*- coding: utf-8 -*-


from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    cancellation_Days = fields.Integer(string=' cancellation date' ,config_parameter="om_hospital.cancellation_Days" )
