# -*- coding: utf-8 -*-

from odoo import models, fields

class InmobiliariaNachete(models.Model):
   _name = 'inmobiliaria_nachete.inmobiliaria_nachete'
   _description = 'Modelo de Vivienda'

   name = fields.Char(string="Nombre")
   descripcion = fields.Text(string="Descripción")
   ubicacio = fields.Char(string="Ubicación")
   dia_de_entrada = fields.Date(string="Día de Entrada")
   dia_de_sortida = fields.Date(string="Día de Salida")
   imagen = fields.Binary(string="Imagen", widget="image")
   habitacions = fields.Integer(string="Habitaciones")
   mascotes = fields.Boolean(string="Permite Mascotas")
   piscina = fields.Boolean(string="Tiene Piscina")
   preu = fields.Float(string="Precio")
   internet = fields.Boolean(string="Tiene Internet")
   telefon = fields.Integer(string="Teléfono")
   accesible = fields.Boolean(string="Accesible")
   rating = fields.Integer(string="Rating")
   propietari = fields.One2many('inmobiliaria_nachete.personas', 'casa', string="Propietarios")
   notas = fields.Text()


class Personas(models.Model):
   _name = 'inmobiliaria_nachete.personas'
   _description = 'Modelo de Personas'

   name = fields.Char(string="Nombre")
   cognom = fields.Char(string="Apellido")
   dni = fields.Char(string="DNI", size=9)
   email = fields.Char(string="Email")
   telefon = fields.Integer(string="Teléfono")
   casa = fields.Many2one('inmobiliaria_nachete.inmobiliaria_nachete', string="Casa")
 
