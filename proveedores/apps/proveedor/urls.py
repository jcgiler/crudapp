from django.conf.urls import url

from .views import (
    ProveedorList,
    ProveedorDetail,
    ProveedorCreation,
    ProveedorUpdate,
    ProveedorDelete
)

urlpatterns = [

    url(r'^$', ProveedorList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', ProveedorDetail.as_view(), name='detail'),
    url(r'^nuevo$', ProveedorCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ProveedorUpdate.as_view(), name='edit'),
    url(r'^eliminar/$', ProveedorDelete, name='delete'),

]
