# from odoo import fields, api, models
#
# from odoo.tools.safe_eval import safe_eval as safe
#
# class Playground(models.Model):
#     _name = "odoo.playground"
#     _description = "odoo play ground "
#
#     DEFAULT_ENV_VARIABLES = ""
#     model_id = fields.Many2one("ir.model", string="models ")
#     code = fields.Text(default=DEFAULT_ENV_VARIABLES)
#     result = fields.Text(string="result")
#
#     def action_excute(self):
#         try:
#             if self.model_id:
#                 model = self.env[self.model_id.model]
#             else:
#                 model = self
#             self.result = safe(self.code.strip(), {"self": model})
#
#         except Exception as r:
#             self.result = str(r)
from odoo import fields, api, models
from odoo.tools.safe_eval import safe_eval as safe

class Playground(models.Model):
    _name = "odoo.playground"
    _description = "Odoo Playground"

    DEFAULT_ENV_VARIABLES = ""  # Default code or empty string
    model_id = fields.Many2one("ir.model", string="Model")
    code = fields.Text(default=DEFAULT_ENV_VARIABLES)
    result = fields.Text(string="Result")

    # code = fields.Text(string="ice_codes")

    def action_excute(self):
        try:
            if self.model_id:
                model = self.env[self.model_id.model]
            else:
                model = self
            self.result = safe(self.code.strip(), {"self": model})
        except Exception as r:
            self.result = str(r)
