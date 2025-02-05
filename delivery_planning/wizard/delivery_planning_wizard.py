from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class DeliveryPlanningWizard(models.TransientModel):
    _name = 'delivery.planning.wizard'
    _description = 'Delivery Planning Wizard'

    picking_id = fields.Many2one('stock.picking', string='Picking', required=True, readonly=True)
    planned_delivery_date = fields.Datetime(string='Planned Delivery Date', required=True)

    def action_confirm(self):
        self.picking_id.planned_delivery_date = self.planned_delivery_date
        message = "Delivery planned for %s" % (self.planned_delivery_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT))
        self.picking_id.message_post(body=message)
