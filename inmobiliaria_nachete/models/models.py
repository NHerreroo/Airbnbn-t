# -*- coding: utf-8 -*-

from odoo import models, fields, api
class inmobiliaria_nachete(models.Model):
   _name = 'inmobiliaria_nachete.inmobiliaria_nachete'
   _description = 'inmobiliaria_nachete.inmobiliaria_nachete'
   name = fields.Char()
   value = fields.Integer()
   value2 = fields.Float(compute="_value_pc", store=True)
   description = fields.Text()


   name = fields.Char()
   descripcion = fields.Text()
   ubicacio = fields.Char()
   dia_de_entrada = fields.Date()
   dia_de_sortida = fields.Date()
   imagen = fields.Binary(string="image")
   habitacions = fields.Integer()
   mascotes = fields.Boolean()
   piscina = fields.Boolean()
   preu = fields.Float()
   internet = fields.Boolean()
   telefon = fields.Integer()
   accesible = fields.Boolean()
   rating = fields.Integer()


   propietari = fields.Many2one('inmobiliaria_nachete.personas','Propietari')


class personas(models.Model):
   _name = 'inmobiliaria_nachete.personas'
   _description = 'personas,clientes,vendores'


   name = fields.Char()
   cognom = fields.Char()
   dni = fields.Char()
   email = fields.Char()
   telefon = fields.Integer()


