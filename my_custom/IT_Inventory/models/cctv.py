from odoo import models, fields, api
from datetime import datetime


class cctv(models.Model):

    _name = "cctv"
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
            ('cctv', 'Record'),
        ],
        string='Category'
    )
    brand = fields.Selection([
            ('b1', 'Dahua'),
            ('b2', 'Hikvision'),
        ],
        string='Brand')
    model = fields.Selection([
            ('b1', '4832-4KS2'),
            ('b2', 'XVR1A0A'),
            ('b3', '5864 -64-4KS2'),
            ('b4', 'XVR1308H1'),
        ],
        string='Model')
    configuration = fields.Char(string='Configuration')
    xvr_nvr_serial= fields.Char(string='XVR_NVR Serial')
    xvr_nvr_asset = fields.Char(string='XVR_NVR Asset ID')
    xvr_nvr_IP = fields.Char(string='XVR_NVR IP Address')
    hostname = fields.Char(string='Host Name')
    xvr_nvr_purchase_date = fields.Char(string='XVR_NVR Purchase Date')
    xvr_nvr_age = fields.Char(string='xvr_nvr Age', compute='_compute_device_age', store=True, readonly=True)
    xvr_nvr_purchase_value = fields.Char(string='XVR_NVR Purchase Value')
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


    @api.depends('xvr_nvr_purchase_date')
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