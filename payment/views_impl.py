from .views import (EmpresaEmpleadoraListAPIView,
                    EmpresaEmpleadoraCreateAPIView,
                    EmpresaEmpleadoraUpdateAPIView,
                    EmpresaEmpleadoraListView,
                    EmpresaEmpleadoraCreateView,
                    EmpresaEmpleadoraUpdateView,
                    EmpleadoListView,
                    EmpleadoCreateView,
                    PensionadoListAPIView,
                    PensionadoCreateAPIView,
                    PensionadoUpdateAPIView,
                    PensionadoListView,
                    PensionadoCreateView,
                    PensionadoUpdateView,
                    empleadoCreate,
                    empleadoUpdate,
                    NovedadListView,
                    NovedadCreateView,
                    NovedadUpdateView,
                    PagosListView,
                    PagosCreateView,
                    test_code)
from django.views.decorators.csrf import csrf_exempt


class EmpresaEmpleadoraListAPIViewImpl(EmpresaEmpleadoraListAPIView):
    def __init__(self):
        EmpresaEmpleadoraListAPIView.__init__(self)


class EmpresaEmpleadoraCreateAPIViewImpl(EmpresaEmpleadoraCreateAPIView):
    def __init__(self):
        EmpresaEmpleadoraCreateAPIView.__init__(self)


class EmpresaEmpleadoraUpdateAPIViewImpl(EmpresaEmpleadoraUpdateAPIView):
    def __init__(self):
        EmpresaEmpleadoraUpdateAPIView.__init__(self)


class EmpresaEmpleadoraListViewImpl(EmpresaEmpleadoraListView):
    def __init__(self):
        EmpresaEmpleadoraListView.__init__(self)


class EmpresaEmpleadoraCreateViewImpl(EmpresaEmpleadoraCreateView):
    def __init__(self):
        EmpresaEmpleadoraCreateView.__init__(self)


class EmpresaEmpleadoraUpdateViewImpl(EmpresaEmpleadoraUpdateView):
    def __init__(self):
        EmpresaEmpleadoraUpdateView.__init__(self)


class EmpleadoListViewImpl(EmpleadoListView):
    def __init__(self):
        EmpleadoListView.__init__(self)


class EmpleadoCreateViewImpl(EmpleadoCreateView):
    def __init__(self):
        EmpleadoCreateView.__init__(self)


class PensionadoListAPIViewImpl(PensionadoListAPIView):
    def __init__(self):
        PensionadoListAPIView.__init__(self)


class PensionadoCreateAPIViewImpl(PensionadoCreateAPIView):
    def __init__(self):
        PensionadoCreateAPIView.__init__(self)


class PensionadoUpdateAPIViewImpl(PensionadoUpdateAPIView):
    def __init__(self):
        PensionadoUpdateAPIView.__init__(self)


class PensionadoListViewImpl(PensionadoListView):
    def __init__(self):
        PensionadoListView.__init__(self)


class PensionadoCreateViewImpl(PensionadoCreateView):
    def __init__(self):
        PensionadoCreateView.__init__(self)


class PensionadoUpdateViewImpl(PensionadoUpdateView):
    def __init__(self):
        PensionadoUpdateView.__init__(self)


@csrf_exempt
def empleadoCreateImpl(request):
    return empleadoCreate(request)


@csrf_exempt
def empleadoUpdateImpl(request, pk):
    return empleadoUpdate(request, pk)


class NovedadListViewImpl(NovedadListView):
    def __init__(self):
        NovedadListView.__init__(self)


class NovedadCreateViewImpl(NovedadCreateView):
    def __init__(self):
        NovedadCreateView.__init__(self)


class NovedadUpdateViewImpl(NovedadUpdateView):
    def __init__(self):
        PensionadoUpdateView.__init__(self)


class PagosListViewImpl(PagosListView):
    def __init__(self):
        PagosListView.__init__(self)


class PagosCreateViewImpl(PagosCreateView):
    def __init__(self):
        PagosCreateView.__init__(self)


@csrf_exempt
def test_codeImpl(request):
    return test_code(request)
