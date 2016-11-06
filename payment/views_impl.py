from .views import (EmpresaEmpleadoraListView, EmpresaEmpleadoraCreateView,
                    EmpresaEmpleadoraUpdateView, PensionadoListView,
                    PensionadoCreateView, PensionadoUpdateView)


class EmpresaEmpleadoraListViewImpl(EmpresaEmpleadoraListView):
    def __init__(self):
        EmpresaEmpleadoraListView.__init__(self)


class EmpresaEmpleadoraCreateViewImpl(EmpresaEmpleadoraCreateView):
    def __init__(self):
        EmpresaEmpleadoraCreateView.__init__(self)


class EmpresaEmpleadoraUpdateViewImpl(EmpresaEmpleadoraUpdateView):
    def __init__(self):
        EmpresaEmpleadoraUpdateView.__init__(self)


class PensionadoListViewImpl(PensionadoListView):
    def __init__(self):
        PensionadoListView.__init__(self)


class PensionadoCreateViewImpl(PensionadoCreateView):
    def __init__(self):
        PensionadoCreateView.__init__(self)


class PensionadoUpdateViewImpl(PensionadoUpdateView):
    def __init__(self):
        PensionadoUpdateView.__init__(self)
