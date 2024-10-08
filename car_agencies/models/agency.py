from odoo import models, fields, _, api


class CarAgency(models.Model):
    _name = 'car.agency'
    _inherit = 'mail.thread'
    _description = 'Car Agency'

    name = fields.Char(required=True)
    responsible_id = fields.Many2one('res.partner', string="Responsible", required=True, tracking=True)
    car_ids = fields.One2many('car.reference.lines', 'car_agency', string="Cars", tracking=True)

    def action_view_brands(self):
        """
        Opens a window to view car brands associated with the current agency.

        This method returns an action dictionary that opens a view to display car brands
        (`car.brand` model) in a tree and form view. The brands shown are filtered to only
        include those associated with the current agency. The current agency ID is also passed
        in the context to pre-fill the agency field when creating new brands.
        """
        return {
            'name': _('Car Brands'),
            'res_model': 'car.brand',
            'view_mode': 'tree,form',
            'context': {'default_agency_id': self.id},
            'domain': [('agency_id', '=', self.id)],
            'target': 'current',
            'type': 'ir.actions.act_window',
        }


class CarReferenceLines(models.Model):
    _name = "car.reference.lines"
    _description = "Car Reference Lines"

    car_id = fields.Many2one("car.car", required=True)
    car_number = fields.Char(related="car_id.registration_number")
    car_agency = fields.Many2one("car.agency", string="Car Agency")

