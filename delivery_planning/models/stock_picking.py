from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    planned_delivery_date = fields.Datetime(string='Planned Delivery Date', readonly=True)

    def action_open_delivery_planning_wizard(self):
        return {
            'name': 'Plan Delivery',
            'type': 'ir.actions.act_window',
            'res_model': 'delivery.planning.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_picking_id': self.id},
        }

    def _process_planned_delivery(self):
        """
        This method is called by the cron job to process planned deliveries.
        """
        for picking in self.search([
            ('state', '!=', 'done'),
            ('planned_delivery_date', '<=', fields.Datetime.now())
        ]):
            try:
                picking.button_validate()
                message = "Delivery automatically validated by cron job."
                picking.message_post(body=message)
                self.env.cr.commit()  # Commit after each successful validation
            except Exception as e:
                # Log the error and continue with the next picking
                self.env.cr.rollback()  # Rollback in case of error
                _logger = self.env['ir.logging'].get_logger(__name__)
                _logger.error(f"Error processing picking {picking.id}: {e}")
                message = f"Error during automatic validation: {e}"
                picking.message_post(body=message)
