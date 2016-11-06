from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .models import EmpresaEmpleadora, Pensionado
from .serializers import (EmpresaEmpleadoraSerializer, PensionadoSerializer,
                          PensionadoCreateUpdateSerializer)


class EmpresaEmpleadoraListView(ListAPIView):
    queryset = EmpresaEmpleadora.objects.all()
    serializer_class = EmpresaEmpleadoraSerializer


class EmpresaEmpleadoraCreateView(CreateAPIView):
    queryset = EmpresaEmpleadora.objects.all()
    serializer_class = EmpresaEmpleadoraSerializer


class EmpresaEmpleadoraUpdateView(UpdateAPIView):
    serializer_class = EmpresaEmpleadoraSerializer

    def get_queryset(self):
        emp = EmpresaEmpleadora.objects.filter(pk=self.kwargs['pk'])
        return emp


class PensionadoListView(ListAPIView):
    queryset = Pensionado.objects.all()
    serializer_class = PensionadoSerializer


class PensionadoCreateView(CreateAPIView):
    queryset = Pensionado.objects.all()
    serializer_class = PensionadoCreateUpdateSerializer


class PensionadoUpdateView(UpdateAPIView):
    serializer_class = PensionadoCreateUpdateSerializer

    def get_queryset(self):
        pen = Pensionado.objects.filter(pk=self.kwargs['pk'])
        return pen
