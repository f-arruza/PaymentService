from .views import (EmpresaEmpleadoraListAPIView,
                    EmpresaEmpleadoraCreateAPIView,
                    EmpresaEmpleadoraUpdateAPIView, PensionadoListAPIView,
                    PensionadoCreateAPIView, PensionadoUpdateAPIView)


class EmpresaEmpleadoraListViewImpl(EmpresaEmpleadoraListAPIView):
    def __init__(self):
        EmpresaEmpleadoraListAPIView.__init__(self)


class EmpresaEmpleadoraCreateViewImpl(EmpresaEmpleadoraCreateAPIView):
    def __init__(self):
        EmpresaEmpleadoraCreateAPIView.__init__(self)


class EmpresaEmpleadoraUpdateViewImpl(EmpresaEmpleadoraUpdateAPIView):
    def __init__(self):
        EmpresaEmpleadoraUpdateAPIView.__init__(self)


class PensionadoListViewImpl(PensionadoListAPIView):
    def __init__(self):
        PensionadoListAPIView.__init__(self)


class PensionadoCreateViewImpl(PensionadoCreateAPIView):
    def __init__(self):
        PensionadoCreateAPIView.__init__(self)


class PensionadoUpdateViewImpl(PensionadoUpdateAPIView):
    def __init__(self):
        PensionadoUpdateAPIView.__init__(self)
