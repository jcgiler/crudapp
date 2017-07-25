# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Proveedor


class ProveedorList(ListView):
    model = Proveedor


class ProveedorDetail(DetailView):
    model = Proveedor

FIELDS = ['nombre','razon_social','identificacion',
				'cedula', 'genero', 'correo', 'telefono']

class ProveedorCreation(CreateView):
    model = Proveedor
    success_url = reverse_lazy('proveedores:list')
    fields = FIELDS

class ProveedorUpdate(UpdateView):
    model = Proveedor
    success_url = reverse_lazy('proveedores:list')
    fields = FIELDS

class ProveedorDelete(DeleteView):
    model = Proveedor
    template_name = 'proveedor/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedores:list')
