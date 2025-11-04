from odoo import models, fields


class TravelsManagement(models.Model):
    _name = "travels.management"

    booking_reference = fields.Char(string='Booking reference')
    no_of_passengers = fields.Integer("No of Passengers", default="2")
    booking_date = fields.Date("Booking Date")
    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('confirmed', "Confirmed"), ],

        string="Status",
        tracking=True,
        default='draft')
