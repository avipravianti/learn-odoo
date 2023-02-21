{
    'name': 'School Management System',
    'author': 'Odoo test',
    'description': """Treating schools""",
    'summary': """School Management Software""",
    'website': 'https://www.odoo.com/app/invoicing',
    'category': 'Tools',
    'data': [
        "security/ir.model.access.csv",
        "views/school.xml"
    ],
    'depends': ['base', 'contacts', 'hr', 'account'],
    'demo': [

    ],
}
