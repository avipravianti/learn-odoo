# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-test(http.Controller):
#     @http.route('/odoo-test/odoo-test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-test/odoo-test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-test.listing', {
#             'root': '/odoo-test/odoo-test',
#             'objects': http.request.env['odoo-test.odoo-test'].search([]),
#         })

#     @http.route('/odoo-test/odoo-test/objects/<model("odoo-test.odoo-test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-test.object', {
#             'object': obj
#         })
