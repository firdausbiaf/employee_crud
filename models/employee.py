from odoo import models, fields

class Employee(models.Model):
    _name = 'employee.crud'
    _description = 'Employee'

    name = fields.Char(string="Nama Karyawan", required=True)
    nik = fields.Char(string="NIK")
    position = fields.Char(string="Jabatan")
    phone = fields.Char(string="No. HP")
    address = fields.Text(string="Alamat")