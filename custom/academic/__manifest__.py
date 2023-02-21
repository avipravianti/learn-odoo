{
    'name': 'Academic Information',
    'author': 'Odoo test',
    'version': '1.0',
    'depends': [
        'base', 'sale'
    ],
    'category': 'Education',
    'description': '''Academic Information System Day 1''',
    'data': [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/course.xml",
        "views/session.xml",
        "views/partner.xml",
        "views/res_partner.xml",
        "views/attendee.xml"
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
