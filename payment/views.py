from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Código Dinámico
from .models import EmpresaEmpleadora, Pensionado
from .serializers import (EmpresaEmpleadoraSerializer, PensionadoSerializer,
                          PensionadoCreateUpdateSerializer)


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'


# Código Dinámico
class EmpresaEmpleadoraListAPIView(ListAPIView):
    queryset = EmpresaEmpleadora.objects.all()
    serializer_class = EmpresaEmpleadoraSerializer

    # permission_classes = (IsAuthenticated,)

    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'id',
    )


# Código Dinámico
class EmpresaEmpleadoraCreateAPIView(CreateAPIView):
    queryset = EmpresaEmpleadora.objects.all()
    serializer_class = EmpresaEmpleadoraSerializer

    # permission_classes = (IsAuthenticated,)


# Código Dinámico
class EmpresaEmpleadoraUpdateAPIView(UpdateAPIView):
    serializer_class = EmpresaEmpleadoraSerializer

    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        emp = EmpresaEmpleadora.objects.filter(pk=self.kwargs['pk'])
        return emp


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class EmpresaEmpleadoraListView(ListView):
    login_url = '/manager/login/'
    redirect_field_name = 'redirect_to'

    model = EmpresaEmpleadora
    template_name = 'emps_list.html'
    context_object_name = 'emps'


# Código Dinámico
class PensionadoListAPIView(ListAPIView):
    queryset = Pensionado.objects.all()
    serializer_class = PensionadoSerializer

    # permission_classes = (IsAuthenticated,)

    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'id',
    )


# Código Dinámico
class PensionadoCreateAPIView(CreateAPIView):
    queryset = Pensionado.objects.all()
    serializer_class = PensionadoCreateUpdateSerializer

    # permission_classes = (IsAuthenticated,)


# Código Dinámico
class PensionadoUpdateAPIView(UpdateAPIView):
    serializer_class = PensionadoCreateUpdateSerializer

    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pen = Pensionado.objects.filter(pk=self.kwargs['pk'])
        return pen
