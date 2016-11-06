from .views import (EmpresaEmpleadoraListAPIView,
                    EmpresaEmpleadoraCreateAPIView,
                    EmpresaEmpleadoraUpdateAPIView, PensionadoListAPIView,
                    PensionadoCreateAPIView, PensionadoUpdateAPIView)


class EmpresaEmpleadoraListViewImpl(EmpresaEmpleadoraListAPIView):
    def __init__(self):
        EmpresaEmpleadoraListView.__init__(self)


class EmpresaEmpleadoraCreateViewImpl(EmpresaEmpleadoraCreateAPIView):
    def __init__(self):
        EmpresaEmpleadoraCreateView.__init__(self)


class EmpresaEmpleadoraUpdateViewImpl(EmpresaEmpleadoraUpdateAPIView):
    def __init__(self):
        EmpresaEmpleadoraUpdateView.__init__(self)


class PensionadoListViewImpl(PensionadoListAPIView):
    def __init__(self):
        PensionadoListView.__init__(self)


class PensionadoCreateViewImpl(PensionadoCreateAPIView):
    def __init__(self):
        PensionadoCreateView.__init__(self)


class PensionadoUpdateViewImpl(PensionadoUpdateAPIView):
    def __init__(self):
        PensionadoUpdateView.__init__(self)
