from django.conf.urls import url
from .views import (EmpresaEmpleadoraListView, EmpresaEmpleadoraCreateView,
                    EmpresaEmpleadoraUpdateView)

urlpatterns = [
    url(r'^emp-list/$', EmpresaEmpleadoraListView.as_view(), name='emp-list'),
    url(r'^emp-create/', EmpresaEmpleadoraCreateView.as_view(),
        name='emp-create'),
    url(r'^emp-update/', EmpresaEmpleadoraUpdateView.as_view(),
        name='emp-update'),
]
