{
    'name': 'Employee CRUD',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Nama Kamu',
    'category': 'Custom',
    'description': 'CRUD sederhana employee',
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
    ],
    'installable': True,
    'application': True,
}