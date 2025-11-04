from odoo import models, fields, api
from datetime import datetime


class ItInventory(models.Model):

    _name = "it.inventory"

    count = fields.Char(string='Count')
    serial = fields.Char(string='Serial Number')
    emp_id = fields.Char(string='ID')
    fullname = fields.Char(string='Full Name')
    email = fields.Char(string='Email IDs')
    unit = fields.Char(string='Unit')
    section = fields.Char(string='Section')
    category = fields.Char(string='Category')
    brand_model = fields.Char(string='CPU Brand & Model')
    configuration = fields.Char(string='Configuration')
    cpu_serial= fields.Char(string='CPU Serial')
    cpu_asset = fields.Char(string='CPU Asset ID')
    hostname = fields.Char(string='Host Name')
    cpu_purchase_date = fields.Char(string='CPU Purchase Date')
    # cpu_dt = fields.Char(string='Today DT')
    cpu_age = fields.Char(string='CPU Age', compute='_compute_device_age', store=True, readonly=True)
    cpu_purchase_value = fields.Char(string='CPU Purchase Value')
    monitor_brand = fields.Char(string='Monitor Brand & Model')
    m_serial = fields.Char(string='Monitor Serial')
    m_asset = fields.Char(string='Monitor Asset ID')
    moni_purchase_date = fields.Char(string='Monitor Purchase Date')
    # m_dt = fields.Char(string='Today DT')
    m_age = fields.Char(string='Monitor Age', compute='_compute_device_age', store=True, readonly=True)
    m_purchase_value = fields.Char(string='Monitor Purchase Value')
    ups_brand = fields.Char(string='UPS Brand & Model')
    ups_serial = fields.Char(string='UPS Serial')
    ups_asset = fields.Char(string='UPS Asset ID')
    u_purchase_date = fields.Char(string='UPS Purchase Date')
    # ups_dt = fields.Char(string='UPS DT')
    ups_age = fields.Char(string='UPS Age', compute='_compute_device_age', store=True, readonly=True)
    u_purchase_value = fields.Char(string='UPS Purchase Value')
    remarks = fields.Char(string='Remarks')
    remarks2 = fields.Char(string='Remarks2')
    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('confirmed', "Confirmed"), ],


        tracking=True,
        default='draft')


    @api.depends('cpu_purchase_date','moni_purchase_date','u_purchase_date')
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

            record.cpu_age = calc_age(record.cpu_purchase_date)
            record.m_age = calc_age(record.moni_purchase_date)
            record.ups_age = calc_age(record.u_purchase_date)
