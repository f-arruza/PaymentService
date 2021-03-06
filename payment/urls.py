# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import IndexView
# Código Dinámico
from payment.implements.views_impl import *

urlpatterns = [
    url(
        r'^login/$',
        auth_views.login,
        {
            'template_name': 'login.html'
        },
        name='login',
    ),
    url(
        '^logout/',
        auth_views.logout,
        {'template_name': 'login.html'},
        name='logout',
    ),
    url(r'^$', IndexView.as_view(), name='index'),
    # Código Dinámico - API REST
    url(r'^api/emp-list/$', EmpresaEmpleadoraListAPIViewImpl.as_view(),
        name='emp-api-list'),
    url(r'^api/emp-create/$', EmpresaEmpleadoraCreateAPIViewImpl.as_view(),
        name='emp-api-create'),
    url(r'^api/emp-update/$', EmpresaEmpleadoraUpdateAPIViewImpl.as_view(),
        name='emp-api-update'),
    url(r'^api/pen-list/$', PensionadoListAPIViewImpl.as_view(),
        name='pen-api-list'),
    url(r'^api/pen-create/$', PensionadoCreateAPIViewImpl.as_view(),
        name='pen-api-create'),
    url(r'^api/pen-update/(?P<pk>\d+)/$',
        PensionadoUpdateAPIViewImpl.as_view(),
        name='pen-api-update'),
    # Código Dinámico - DJANGO VIEWS
    url(r'^emp-list/$', EmpresaEmpleadoraListViewImpl.as_view(),
        name='emp-list'),
    url(r'^emp-create/$', EmpresaEmpleadoraCreateViewImpl.as_view(),
        name='emp-create'),
    url(r'^emp-update/(?P<pk>\d+)/$',
        EmpresaEmpleadoraUpdateViewImpl.as_view(),
        name='emp-update'),
    url(r'^empl-list/$', EmpleadoListViewImpl.as_view(),
        name='empl-list'),
    url(r'^empl-create/$', empleadoCreateImpl, name='empl-create'),
    url(r'^empl-update/(?P<pk>\d+)/$', empleadoUpdateImpl, name='empl-update'),
    url(r'^pen-list/$', PensionadoListViewImpl.as_view(),
        name='pen-list'),
    url(r'^pen-create/$', PensionadoCreateViewImpl.as_view(),
        name='pen-create'),
    url(r'^pen-update/(?P<pk>\d+)/$', PensionadoUpdateViewImpl.as_view(),
        name='pen-update'),
    url(r'^nov-list/$', NovedadListViewImpl.as_view(),
        name='nov-list'),
    url(r'^nov-create/$', NovedadCreateViewImpl.as_view(),
        name='nov-create'),
    url(r'^nov-update/(?P<pk>\d+)/$', NovedadUpdateViewImpl.as_view(),
        name='nov-update'),
    url(r'^pag-list/$', PagosListViewImpl.as_view(),
        name='pag-list'),
    url(r'^pag-create/$', PagosCreateViewImpl.as_view(),
        name='pag-create'),
    url(r'^pag-calculate/$', paymentCalculateImpl,
        name='pag-calculate'),
]
