# -*- coding: UTF-8 -*-
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Código Dinámico
from .models import (EmpresaEmpleadora, Pensionado, Empleado, Novedad,
                     PagoAporte, Banco)
from .serializers import (EmpresaEmpleadoraSerializer, PensionadoSerializer,
                          PensionadoCreateUpdateSerializer)
from .payingrules import PayingRules


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'pag_list.html'


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class EmpresaEmpleadoraListView(ListView):
    model = EmpresaEmpleadora
    template_name = 'emp_list.html'
    context_object_name = 'emp_list'


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class EmpresaEmpleadoraCreateView(CreateView):
    model = EmpresaEmpleadora
    template_name = 'emp_create.html'
    context_object_name = 'emp'
    fields = [
        'nombreRazonSocial',
        'tipoDocumento',
        'numeroDocumento',
        'clasePagadorPensiones',
        'naturalezaJuridica',
        'tipoPersona',
        'direccion',
        'ciudadMunicipio',
        'departamento',
        'telefono',
        'correo',
        'tipoPagadorPensiones',
        'actividadEconomica',
    ]

    def get_success_url(self):
        return reverse('emp-list')


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class EmpresaEmpleadoraUpdateView(UpdateView):
    model = EmpresaEmpleadora
    template_name = 'emp_update.html'
    context_object_name = 'emp'
    fields = [
        'nombreRazonSocial',
        'tipoDocumento',
        'numeroDocumento',
        'clasePagadorPensiones',
        'naturalezaJuridica',
        'tipoPersona',
        'direccion',
        'ciudadMunicipio',
        'departamento',
        'telefono',
        'correo',
        'tipoPagadorPensiones',
        'actividadEconomica',
        'active',
    ]

    def get_success_url(self):
        return reverse('emp-list')


@method_decorator(login_required, name='dispatch')
class EmpleadoListView(ListView):
    template_name = 'empl_list.html'
    context_object_name = 'empl_list'

    def get_queryset(self):
        pempresa = self.request.GET.get('empresa')

        queryset = ""
        if pempresa:
            queryset = Empleado.objects.filter(
                empresa=pempresa)
        else:
            if self.request.user.is_staff:
                queryset = Empleado.objects.all()
            else:
                empl = Empleado.objects.get(user_id=self.request.user.id)
                queryset = Empleado.objects.filter(empresa=empl.empresa)
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView,
                        self).get_context_data(**kwargs)
        empl = ""
        if self.request.user.is_staff:
            context['emp_list'] = EmpresaEmpleadora.objects.filter(active=True)
        else:
            empl = Empleado.objects.filter(user_id=self.request.user.id)
            context['emp_list'] = EmpresaEmpleadora.objects.filter(
                    active=True,
                    empl_emp__in=empl
                    )
        return context


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empl_create.html'
    context_object_name = 'empl'
    fields = [
        'user_username',
        'user_first_name',
        'user_last_name',
        'user_email',
        'empresa',
    ]

    def get_success_url(self):
        return reverse('empl-list')


@csrf_exempt
def empleadoCreate(request):
    if request.user.is_authenticated():
        mensaje = ''
        if request.user.is_staff:
            empresas = EmpresaEmpleadora.objects.filter(active=True)
        else:
            empl = Empleado.objects.filter(user_id=request.user.id)
            empresas = EmpresaEmpleadora.objects.filter(
                    active=True,
                    empl_emp__in=empl
                    )

        if request.method == 'POST':
            mensaje = registrar_empleado(request)
            if mensaje == '':
                return redirect(reverse('empl-list'))
        return render(request,
                      'empl_create.html', {'mensaje': mensaje,
                                           'empresas': empresas})
    else:
        return redirect(reverse('index'))


def registrar_empleado(request):
    empresa = request.POST.get('frm_empresa')
    first_name = request.POST.get('frm_first_name')
    last_name = request.POST.get('frm_last_name')
    username = request.POST.get('frm_username')
    email = request.POST.get('frm_email')
    password1 = request.POST.get('frm_password1')
    password2 = request.POST.get('frm_password2')

    if (username is not "" and password1 is not "" and password2 is not "" and
       email is not "" and first_name is not "" and
       last_name is not "" and empresa is not ""):

        exist_user = User.objects.filter(username=username)
        if exist_user.count() > 0:
            status = 'Usuario ya existe.'
        else:
            if password1 != password2:
                status = 'Las contraseñas no coinciden.'
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name)
                user.save()
                emp = EmpresaEmpleadora.objects.get(id=empresa)

                empl = Empleado.objects.create(user=user, empresa=emp)
                status = ''
    else:
        status = 'Todos los campos son obligatorios.'
    return status


@csrf_exempt
def empleadoUpdate(request, pk):
    if request.user.is_authenticated():
        mensaje = ''
        empleado = Empleado.objects.get(id=pk)
        if request.user.is_staff:
            empresas = EmpresaEmpleadora.objects.filter(active=True)
        else:
            empl = Empleado.objects.filter(user_id=request.user.id)
            empresas = EmpresaEmpleadora.objects.filter(
                    active=True,
                    empl_emp__in=empl
                    )

        if request.method == 'POST':
            mensaje = actualizar_empleado(request, pk)
            if mensaje == '':
                return redirect(reverse('empl-list'))
        return render(request,
                      'empl_update.html', {'mensaje': mensaje,
                                           'empresas': empresas,
                                           'empleado': empleado,
                                           'pk': pk})
    else:
        return redirect(reverse('index'))


def actualizar_empleado(request, id_user):
    empresa = request.POST.get('frm_empresa')
    first_name = request.POST.get('frm_first_name')
    last_name = request.POST.get('frm_last_name')
    email = request.POST.get('frm_email')
    active = request.POST.get('frm_is_active')

    if(active is None):
        active = False
    else:
        active = True

    if (email is not "" and first_name is not "" and last_name is not "" and
       empresa is not "" and active is not None):

        user = User.objects.get(id=id_user)
        if user is None:
            status = 'Usuario no existe.'
        else:
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.is_active = active
            user.save()

            emp = EmpresaEmpleadora.objects.get(id=empresa)
            empl = Empleado.objects.get(user=user)
            empl.empresa = emp
            empl.save()
            status = ''
    else:
        status = 'Todos los campos son obligatorios.'
    return status


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class PensionadoListView(ListView):
    model = Pensionado
    template_name = 'pen_list.html'
    context_object_name = 'pen_list'

    def get_queryset(self):
        pempresa = self.request.GET.get('empresa')

        queryset = ""
        if pempresa:
            queryset = Pensionado.objects.filter(
                empresaEmpleadora=pempresa)
        else:
            if self.request.user.is_staff:
                queryset = Pensionado.objects.all()
            else:
                empl = Empleado.objects.get(user_id=self.request.user.id)
                queryset = Pensionado.objects.filter(
                    empresaEmpleadora=empl.empresa)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PensionadoListView,
                        self).get_context_data(**kwargs)
        empl = ""
        if self.request.user.is_staff:
            context['emp_list'] = EmpresaEmpleadora.objects.filter(active=True)
        else:
            empl = Empleado.objects.filter(user_id=self.request.user.id)
            context['emp_list'] = EmpresaEmpleadora.objects.filter(
                    active=True,
                    empl_emp__in=empl
                    )
        return context


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class PensionadoCreateView(CreateView):
    model = Pensionado
    template_name = 'pen_create.html'
    context_object_name = 'pen'
    fields = [
        'primerApellido',
        'segundoApellido',
        'primerNombre',
        'segundoNombre',
        'tipoDocumento',
        'numeroDocumento',
        'tipoPension',
        'tipoPensionado',
        'pensionadoExterior',
        'grupoFamiliarColombia',
        'ingresoBaseCotizacion',
        'actividadEconomica',
        'tarifaEspecial',
        'empresaEmpleadora',
    ]

    def get_context_data(self, **kwargs):
        context = super(PensionadoCreateView,
                        self).get_context_data(**kwargs)
        empl = ""
        if self.request.user.is_staff:
            context['emp_list'] = EmpresaEmpleadora.objects.filter(active=True)
        else:
            empl = Empleado.objects.filter(user_id=self.request.user.id)
            context['emp_list'] = EmpresaEmpleadora.objects.filter(
                    active=True,
                    empl_emp__in=empl
                    )
        return context

    def get_success_url(self):
        return reverse('pen-list')


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class PensionadoUpdateView(UpdateView):
    model = Pensionado
    template_name = 'pen_update.html'
    context_object_name = 'pen'
    fields = [
        'primerApellido',
        'segundoApellido',
        'primerNombre',
        'segundoNombre',
        'tipoDocumento',
        'numeroDocumento',
        'tipoPension',
        'tipoPensionado',
        'pensionadoExterior',
        'grupoFamiliarColombia',
        'ingresoBaseCotizacion',
        'actividadEconomica',
        'tarifaEspecial',
        'empresaEmpleadora',
        'active',
    ]

    def get_success_url(self):
        return reverse('pen-list')

    def get_context_data(self, **kwargs):
        context = super(PensionadoUpdateView,
                        self).get_context_data(**kwargs)
        empl = ""
        if self.request.user.is_staff:
            context['emp_list'] = EmpresaEmpleadora.objects.filter(active=True)
        else:
            empl = Empleado.objects.filter(user_id=self.request.user.id)
            context['emp_list'] = EmpresaEmpleadora.objects.filter(
                    active=True,
                    empl_emp__in=empl
                    )
        return context


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class NovedadListView(ListView):
    model = Novedad
    template_name = 'nov_list.html'
    context_object_name = 'nov_list'

    def get_queryset(self):
        pempresa = self.request.GET.get('empresa')

        queryset = ""
        if pempresa:
            queryset = Novedad.objects.filter(
                    pensionado__in=Pensionado.objects.filter(
                        empresaEmpleadora_id=pempresa)
                    )
        else:
            if self.request.user.is_staff:
                queryset = Novedad.objects.all()
            else:
                empl = Empleado.objects.get(user_id=self.request.user.id)
                queryset = Novedad.objects.filter(
                        pensionado__in=Pensionado.objects.filter(
                            empresaEmpleadora__id=empl.empresa.id)
                        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(NovedadListView,
                        self).get_context_data(**kwargs)
        empl = ""
        if self.request.user.is_staff:
            context['emp_list'] = EmpresaEmpleadora.objects.filter(active=True)
        else:
            empl = Empleado.objects.filter(user_id=self.request.user.id)
            context['emp_list'] = EmpresaEmpleadora.objects.filter(
                    active=True,
                    empl_emp__in=empl
                    )
        return context


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class NovedadCreateView(CreateView):
    model = Novedad
    template_name = 'nov_create.html'
    context_object_name = 'nov'
    fields = [
        'fechaInicio',
        'fechaFin',
        'tipo',
        'procesada',
        'duracion',
        'pensionado',
    ]

    def get_context_data(self, **kwargs):
        context = super(NovedadCreateView,
                        self).get_context_data(**kwargs)
        empl = ""
        if self.request.user.is_staff:
            context['pen_list'] = Pensionado.objects.filter(active=True)
        else:
            empl = Empleado.objects.get(user_id=self.request.user.id)
            context['pen_list'] = Pensionado.objects.filter(
                active=True,
                empresaEmpleadora__id=empl.empresa.id)
        return context

    def get_success_url(self):
        return reverse('nov-list')


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class NovedadUpdateView(UpdateView):
    model = Novedad
    template_name = 'nov_update.html'
    context_object_name = 'nov'
    fields = [
        'fechaInicio',
        'fechaFin',
        'tipo',
        'procesada',
        'duracion',
        'pensionado',
        'active',
    ]

    def get_context_data(self, **kwargs):
        context = super(NovedadUpdateView,
                        self).get_context_data(**kwargs)
        empl = ""
        if self.request.user.is_staff:
            context['pen_list'] = Pensionado.objects.filter(active=True)
        else:
            empl = Empleado.objects.get(user_id=self.request.user.id)
            context['pen_list'] = Pensionado.objects.filter(
                active=True,
                empresaEmpleadora__id=empl.empresa.id)
        return context

    def get_success_url(self):
        return reverse('nov-list')


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class PagosListView(ListView):
    model = PagoAporte
    template_name = 'pag_list.html'
    context_object_name = 'pag_list'

    def get_queryset(self):
        pempresa = self.request.GET.get('empresa')
        ppensionado = self.request.GET.get('pensionado')

        queryset = ""
        if ppensionado:
            queryset = PagoAporte.objects.filter(
                    pensionado__in=Pensionado.objects.filter(
                        id=ppensionado)
                    )
        else:
            if pempresa:
                queryset = PagoAporte.objects.filter(
                        pensionado__in=Pensionado.objects.filter(
                            empresaEmpleadora_id=pempresa)
                        )
            else:
                if self.request.user.is_staff:
                    queryset = PagoAporte.objects.all()
                else:
                    empl = Empleado.objects.get(user_id=self.request.user.id)
                    queryset = PagoAporte.objects.filter(
                            pensionado__in=Pensionado.objects.filter(
                                empresaEmpleadora_id=empl.empresa.id)
                            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PagosListView,
                        self).get_context_data(**kwargs)
        empl = ""
        if self.request.user.is_staff:
            context['emp_list'] = EmpresaEmpleadora.objects.filter(active=True)
            context['pen_list'] = Pensionado.objects.filter(active=True)
        else:
            empl = Empleado.objects.get(user_id=self.request.user.id)
            context['emp_list'] = EmpresaEmpleadora.objects.filter(
                    active=True,
                    empl_emp=empl
                    )
            context['pen_list'] = Pensionado.objects.filter(
                active=True,
                empresaEmpleadora__id=empl.empresa.id)
        context['spen'] = self.request.GET.get('pensionado')
        return context


# Código Dinámico
@method_decorator(login_required, name='dispatch')
class PagosCreateView(CreateView):
    model = PagoAporte
    template_name = 'pag_create.html'
    context_object_name = 'pag'
    fields = [
        'tipo',
        'periodoPago',
        'monto',
        'banco',
        'pensionado',
    ]

    def get_context_data(self, **kwargs):
        context = super(PagosCreateView,
                        self).get_context_data(**kwargs)
        empl = ""
        if self.request.user.is_staff:
            context['pen_list'] = Pensionado.objects.filter(active=True)
        else:
            empl = Empleado.objects.get(user_id=self.request.user.id)
            context['pen_list'] = Pensionado.objects.filter(
                active=True,
                empresaEmpleadora__id=empl.empresa.id)
        context['bancos'] = Banco.objects.all()
        return context

    def get_success_url(self):
        return reverse('pag-list')


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


@csrf_exempt
def test_code(request):
    mensaje = "HOLA: "
    py = PayingRules()

    tarifa = py.calculate(1, '03')
    mensaje = mensaje + str(tarifa)

    return render(request, 'test.html', {'mensaje': mensaje})
