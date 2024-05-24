# -*- coding: utf-8 -*-
from odoo import http


class InmobiliariaNachete(http.Controller):
    @http.route('/inmobiliaria_nachete/inmobiliaria_nachete', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/inmobiliaria_nachete/inmobiliaria_nachete/objects', auth='public')
    def list(self, **kw):
        return http.request.render('inmobiliaria_nachete.listing', {
            'root': '/inmobiliaria_nachete/inmobiliaria_nachete',
            'objects': http.request.env['inmobiliaria_nachete.inmobiliaria_nachete'].search([]),
        })

    @http.route('/inmobiliaria_nachete/inmobiliaria_nachete/objects/<model("inmobiliaria_nachete.inmobiliaria_nachete"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('inmobiliaria_nachete.object', {
            'object': obj
        })