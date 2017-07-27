# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Proveedor(models.Model):

    TDI = (
        ('1','CEDULA'),
        ('2','RUC')
    )

    GENERO = (
        ('M','MASCULINO'),
        ('F','FEMENINO')
    )

    nombre = models.CharField('Nombre Completo', max_length=255)
    razon_social = models.CharField('Razón Social', max_length=255)
    identificacion = models.CharField('Tipo de Identificacion',
                                        max_length=1, choices=TDI)
    cedula = models.CharField('Cedula', max_length=20)
    genero = models.CharField('Genero', max_length=1, choices=GENERO)
    correo = models.EmailField('Correo', max_length=254)
    telefono = models.CharField('Telefono', max_length=10)
    archivado = models.BooleanField('Archivado?', default=False)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Provedores'

    def __str__(self):
        return self.nombre
