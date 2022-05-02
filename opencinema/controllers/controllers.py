# -*- coding: utf-8 -*-
# from odoo import http


# class Opencinema(http.Controller):
#     @http.route('/opencinema/opencinema/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/opencinema/opencinema/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('opencinema.listing', {
#             'root': '/opencinema/opencinema',
#             'objects': http.request.env['opencinema.opencinema'].search([]),
#         })

#     @http.route('/opencinema/opencinema/objects/<model("opencinema.opencinema"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('opencinema.object', {
#             'object': obj
#         })
