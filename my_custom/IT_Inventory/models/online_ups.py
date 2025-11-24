from odoo import models, fields, api
from datetime import datetime


class online_ups(models.Model):

    _name = "online_ups"
    count = fields.Char(string='Count')
    serial = fields.Char(string='Serial Number')
    emp_id = fields.Char(string='ID')
    fullname = fields.Char(string='Full Name')
    unit = fields.Selection([
            ('ho', 'Head Office'),
            ('mt', 'Metal Trims'),
            ('zip', 'Zipper'),
        ],
        string='Unit')

    section = fields.Selection(
        [   ('dept1', 'HR, Admin & Compliance'),
            ('dept2', 'Sales'),
            ('dept3', 'Sales & Marketing'),
            ('dept4', 'Software Development'),
            ('dept5', 'System Engineering'),
        ],
        string='Section')
    category = fields.Selection(
        [
            ('online_ups', 'Backup'),
        ],
        string='Category'
    )
    brand = fields.Selection([
            ('b1', 'Apollo'),
            ('b2', 'K-Star'),
            ('b3', 'Emerson(Vertiv)'),
            ('b4', 'Sako TNS-AVR'),
        ],
        string='Brand')
    model = fields.Selection([
            ('b1', 'GXT MT+LB'),
            ('b2', 'GXT MT+CX'),
            ('b3', 'HP930C'),
        ],
        string='Model')
    configuration = fields.Char(string='Configuration')
    online_ups_serial= fields.Char(string='Online_UPS Serial')
    online_ups_asset = fields.Char(string='Online_UPS Asset ID')
    online_ups_IP = fields.Char(string='Online_UPS IP Address')
    hostname = fields.Char(string='Host Name')
    online_ups_purchase_date = fields.Char(string='Online_UPS Purchase Date')
    online_ups_age = fields.Char(string='Online_UPS Age', compute='_compute_device_age', store=True, readonly=True)
    online_ups_purchase_value = fields.Char(string='Online_UPS Purchase Value')
    status = fields.Selection([
        ('s1', 'In Use'),
        ('s2', 'Idle'),
    ],
        string='Status')
    remarks = fields.Selection([
        ('r1', 'Out of Order'),
    ],
        string='Remarks')
    remarks2 = fields.Char(string='Remarks2')
    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('confirmed', "Confirmed"), ],


         tracking=True,
         default='draft')


    @api.depends('online_ups_purchase_date')
    def _compute_device_age(self):
        today = fields.Date.today()
        for record in self:
            def calc_age(date_str):
                if not date_str:
                    return "N/A"
                try:
                    purchase_date = datetime.strptime(date_str, "%d-%m-%Y").date()
                    delta = today - purchase_date
                    years = delta.days // 365
                    months = (delta.days % 365) // 30
                    days = (delta.days % 365) % 30
                    return f"{years} years {months} months {days} days"
                except Exception:
                    return "Invalid Date Format"