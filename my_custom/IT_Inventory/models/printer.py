from odoo import models, fields, api
from datetime import datetime


class printer(models.Model):

    _name = "printer"
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
        [
            ('dept1', 'Accounts'),
            ('dept2', 'Accounts & Finance'),
            ('dept3', 'Assembly(Packing)'),
            ('dept4', 'Auto Assembly'),
            ('dept5', 'Brass Cutting'),
            ('dept6', 'Business Intelligence'),
            ('dept7', 'CEO Office'),
            ('dept8', 'Civil'),
            ('dept9', 'Coil'),
            ('dept10', 'Commercial'),
            ('dept11', 'Costing'),
            ('dept12', 'Customer Support'),
            ('dept13', 'Design & Engineering'),
            ('dept14', 'Design & Marketing'),
            ('dept15', 'Design & Tool Room'),
            ('dept16', 'Die Casting'),
            ('dept17', 'Dyeing'),
            ('dept18', 'Electro Plating'),
            ('dept19', 'ETP'),
            ('dept20', 'FG Store'),
            ('dept21', 'GET'),
            ('dept22', 'HR, Admin & Compliance'),
            ('dept23', 'Maintenance'),
            ('dept24', 'Management'),
            ('dept25', 'Manufacturing'),
            ('dept26', 'Marketing'),
            ('dept27', 'Metal Chain'),
            ('dept28', 'MIS'),
            ('dept29', 'Packing'),
            ('dept30', 'Plastic Zipper'),
            ('dept31', 'PPC'),
            ('dept32', 'Process Management'),
            ('dept33', 'Process Development'),
            ('dept34', 'Production'),
            ('dept35', 'Purchase'),
            ('dept36', 'Quality Assurance'),
            ('dept37', 'RM Store'),
            ('dept38', 'Sales'),
            ('dept39', 'Sales & Marketing'),
            ('dept40', 'Sample'),
            ('dept41', 'Software Development'),
            ('dept42', 'Supply Chain'),
            ('dept43', 'System Engineering'),
        ],
        string='Section')
    category = fields.Selection(
        [
            ('printer', 'printer'),
        ],
        string='Category'
    )
    brand = fields.Selection([
            ('b1', 'HP'),
            ('b2', 'Epson'),
            ('b3', 'Canon'),
            ('b4', 'Kyocera'),
            ('b5', 'Toshiba'),
            ('b6', 'Pentum'),
            ('b7', 'Brother'),
        ],
        string='Brand')
    model = fields.Selection([
        ('b1', '107W'),
        ('b2', 'L3210'),
        ('b3', 'L3250'),
        ('b4', 'M283fdw'),
        ('b5', 'L220'),
        ('b6', 'L130'),
        ('b7', 'L455'),
    ],
        string='model')
    configuration = fields.Char(string='Configuration')
    printer_ip= fields.Char(string='IP Address')
    printer_serial= fields.Char(string='Serial')
    printer_asset = fields.Char(string='Asset ID')
    hostname = fields.Char(string='Host Name')
    printer_purchase_date = fields.Char(string='Purchase Date')
    # cpu_dt = fields.Char(string='Today DT')
    printer_age = fields.Char(string='Age', compute='_compute_device_age', store=True, readonly=True)
    printer_purchase_value = fields.Char(string='Purchase Value')
    status = fields.Selection([
        ('s1', 'In Use'),
        ('s2', 'Idle'),
        ('s3', 'Out of Order'),

    ],
        string = 'Status')
    # remarks = fields.Selection([
    #     ('r1', 'Out of Order'),
    # ],
    #      string='Remarks')
    remarks = fields.Char(string='Remarks')
    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('confirmed', "Confirmed"), ],


         tracking=True,
         default='draft')


    @api.depends('printer_purchase_date')
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