from django.conf.urls import url

from .views import (
    ProveedorList,
    ProveedorArchiveList,
    ProveedorDetail,
    ProveedorCreation,
    ProveedorUpdate,
    ProveedorDelete
)

urlpatterns = [

    url(r'^$', ProveedorList.as_view(), name='list'),
    url(r'^archivado$', ProveedorArchiveList.as_view(), name='archive'),
    url(r'^(?P<pk>\d+)$', ProveedorDetail.as_view(), name='detail'),
    url(r'^nuevo$', ProveedorCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ProveedorUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', ProveedorDelete.as_view(), name='delete'),

]
