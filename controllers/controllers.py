# -*- coding: utf-8 -*-
from odoo import http

# class MethodReferenciaPicking(http.Controller):
#     @http.route('/method_referencia_picking/method_referencia_picking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_referencia_picking/method_referencia_picking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_referencia_picking.listing', {
#             'root': '/method_referencia_picking/method_referencia_picking',
#             'objects': http.request.env['method_referencia_picking.method_referencia_picking'].search([]),
#         })

#     @http.route('/method_referencia_picking/method_referencia_picking/objects/<model("method_referencia_picking.method_referencia_picking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_referencia_picking.object', {
#             'object': obj
#         })