from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .models import EmpresaEmpleadora
from .serializers import EmpresaEmpleadoraSerializer


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
