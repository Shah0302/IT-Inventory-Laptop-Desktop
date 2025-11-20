from odoo import models, fields, api
from datetime import datetime


class Desktop(models.Model):

    _name = "desktop"
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
            ('desktop', 'Desktop'),
        ],
        string='Category'
    )
    brand_model = fields.Selection([
            ('b1', 'HP'),
            ('b2', 'Dell'),
            ('b3', 'Asus'),
            ('b4', 'Lenovo'),
            ('b5', 'Fujitsu'),
            ('b6', 'Acer'),
            ('b7', 'Clone'),
        ],
        string='Desktop Brand & Model')
    configuration = fields.Char(string='Configuration')
    desktop_serial= fields.Char(string='CPU Serial')
    desktop_asset = fields.Char(string='CPU Asset ID')
    hostname = fields.Char(string='Host Name')
    desktop_purchase_date = fields.Char(string='CPU Purchase Date')
    # cpu_dt = fields.Char(string='Today DT')
    desktop_age = fields.Char(string='CPU Age', compute='_compute_device_age', store=True, readonly=True)
    desktop_purchase_value = fields.Char(string='CPU Purchase Value')
    monitor_brand = fields.Selection( [
            ('b1', 'HP'),
            ('b2', 'Dell'),
            ('b3', 'Acer'),
            ('b4', 'Lenovo'),
            ('b5', 'Gigasonic'),
            ('b6', 'Rylasis'),
            ('b7', 'Value Top'),
        ],
        string='Monitor Brand & Model')
    m_serial = fields.Char(string='Monitor Serial')
    m_asset = fields.Char(string='Monitor Asset ID')
    moni_purchase_date = fields.Char(string='Monitor Purchase Date')
    # m_dt = fields.Char(string='Today DT')
    m_age = fields.Char(string='Monitor Age', compute='_compute_device_age', store=True, readonly=True)
    m_purchase_value = fields.Char(string='Monitor Purchase Value')
    ups_brand = fields.Selection([
            ('b1', 'Apollo'),
            ('b2', 'Power Guard'),
            ('b3', 'Prolink'),
            ('b4', 'PC Power'),
            ('b5', 'Max Green'),
            ('b6', 'KStar'),
            ('b7', 'Marsriva'),
        ],
        string='UPS Brand & Model')
    ups_serial = fields.Char(string='UPS Serial')
    ups_asset = fields.Char(string='UPS Asset ID')
    u_purchase_date = fields.Char(string='UPS Purchase Date')
    ups_dt = fields.Char(string='UPS DT')
    ups_age = fields.Char(string='UPS Age', compute='_compute_device_age', store=True, readonly=True)
    u_purchase_value = fields.Char(string='UPS Purchase Value')
    remarks = fields.Selection([
            ('r1', 'User has been Resigned'),
        ],
        string='Remarks')
    remarks2 = fields.Char(string='Remarks2')
    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('confirmed', "Confirmed"), ],


         tracking=True,
         default='draft')


    @api.depends('desktop_purchase_date','moni_purchase_date')
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