from odoo import models, fields, api
from datetime import datetime


class pabx(models.Model):

    _name = "pabx"
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
            ('pabx', 'Communication'),
        ],
        string='Category'
    )
    brand = fields.Selection([
            ('b1', 'Panasonic'),
            ('b2', 'Grandstream'),
        ],
        string='Brand')
    model = fields.Selection([
            ('b1', 'KX-NS300'),
            ('b2', 'GXW4232'),
            ('b3', 'UCM6301 V1.2C'),
        ],
        string='Model')
    configuration = fields.Char(string='Configuration')
    pabx_serial= fields.Char(string='PABX Serial')
    pabx_asset = fields.Char(string='PABX Asset ID')
    pabx_IP = fields.Char(string='PABX IP Address')
    hostname = fields.Char(string='Host Name')
    pabx_purchase_date = fields.Char(string='PABX Purchase Date')
    pabx_age = fields.Char(string='PABX Age', compute='_compute_device_age', store=True, readonly=True)
    pabx_purchase_value = fields.Char(string='PABX Purchase Value')
    status = fields.Selection([
        ('s1', 'In Use'),
        ('s2', 'Idle'),
        ('s3', 'End of Life'),
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


    @api.depends('pabx_purchase_date')
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