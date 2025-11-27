from odoo import models, fields, api
from datetime import datetime


class attendance_machine(models.Model):

    _name = "attendance_machine"
    count = fields.Char(string='Count')
    serial = fields.Char(string='Serial Number')
    emp_id = fields.Char(string='ID')
    fullname = fields.Char(string='Full Name')
    email = fields.Char(string='Email IDs')
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
            ('attendance_machine', 'Attendance Machine'),
        ],
        string='Category'
    )
    brand = fields.Selection([
            ('b1', 'ZkTeco'),
        ],
        string='Machine Brand')
    model = fields.Selection([
            ('b1', 'F18'),
            ('b2', 'uFace800'),
            ('b3', 'K40'),
        ],
        string='Machine Model')
    configuration = fields.Char(string='Configuration')
    attendance_machine_serial= fields.Char(string='Machine Serial')
    attendance_machine_asset = fields.Char(string='Machine Asset ID')
    attendance_machine_IP = fields.Char(string='Machine IP Address')
    hostname = fields.Char(string='Host Name')
    attendance_machine_purchase_date = fields.Char(string='Machine Purchase Date')
    attendance_machine_age = fields.Char(string='Machine Age', compute='_compute_device_age', store=True, readonly=True)
    attendance_machine_purchase_value = fields.Char(string='Machine Purchase Value')
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

    @api.depends('attendance_machine_purchase_date')
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

            record.attendance_machine_age = calc_age(record.attendance_machine_purchase_date)

