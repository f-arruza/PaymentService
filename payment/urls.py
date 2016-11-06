from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import IndexView
from .views_impl import (EmpresaEmpleadoraListViewImpl,
                         EmpresaEmpleadoraCreateViewImpl,
                         EmpresaEmpleadoraUpdateViewImpl,
                         PensionadoListViewImpl,
                         PensionadoCreateViewImpl,
                         PensionadoUpdateViewImpl)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='manager'),
    url(
        r'^login/$',
        auth_views.login,
        {
            'template_name': 'login.html'
        },
        name='login',
    ),
    url(r'^emp-list/$', EmpresaEmpleadoraListViewImpl.as_view(),
        name='emp-list'),
    url(r'^emp-create/', EmpresaEmpleadoraCreateViewImpl.as_view(),
        name='emp-create'),
    url(r'^emp-update/', EmpresaEmpleadoraUpdateViewImpl.as_view(),
        name='emp-update'),
    url(r'^pen-list/$', PensionadoListViewImpl.as_view(),
        name='pen-list'),
    url(r'^pen-create/', PensionadoCreateViewImpl.as_view(),
        name='pen-create'),
    url(r'^pen-update/', PensionadoUpdateViewImpl.as_view(),
        name='pen-update'),
]
