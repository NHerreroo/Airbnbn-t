# -*- coding: utf-8 -*-

from odoo import models, fields

class InmobiliariaNachete(models.Model):
   _name = 'inmobiliaria_nachete.inmobiliaria_nachete'
   _description = 'Modelo de Vivienda'

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
   propietari = fields.One2many('inmobiliaria_nachete.personas', 'casa', string="Propietarios")
   notas = fields.Text()


class Personas(models.Model):
   _name = 'inmobiliaria_nachete.personas'
   _description = 'Modelo de Personas'

   name = fields.Char()
   cognom = fields.Char()
   dni = fields.Char(size=9)
   email = fields.Char()
   telefon = fields.Integer()
   casa = fields.Many2one('inmobiliaria_nachete.inmobiliaria_nachete', string="Casa")
 
