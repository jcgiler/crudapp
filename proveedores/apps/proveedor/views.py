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

    context_object_name = 'proveedores'

    def get(self, request, *args, **kwargs):
        A = False if not self.request.GET.get('q') else True
        self.queryset = Proveedor.objects.filter(archivado=A).order_by('-pk')
        return super(ProveedorList, self).get(request, *args, **kwargs)


class ProveedorDetail(DetailView):
    model = Proveedor


FIELDS = ['nombre','razon_social','identificacion',
		  'cedula','genero','correo','telefono','archivado']


class ProveedorCreation(CreateView):
    model = Proveedor
    success_url = reverse_lazy('proveedores:list')
    fields = FIELDS

class ProveedorUpdate(UpdateView):
    model = Proveedor
    success_url = reverse_lazy('proveedores:list')
    fields = FIELDS

def ProveedorDelete(request):
    
    template = 'proveedor/proveedor_list.html'
    cid = request.GET['q']
    Proveedor.objects.get(pk=cid).delete()

    return render(request, template, {})