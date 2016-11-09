from payment.models import Novedad, Pensionado
from decimal import *


class PayingRules():

    def calculate(self, pensionado_id, tipo_aporte):
        monto = None
        # SALUD
        if tipo_aporte == '01':
            tarifa = self.calcularSaludConNovedad3(pensionado_id)
            if tarifa is not None:
                monto = tarifa
            tarifa = self.calcularSaludConNovedad3_7(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularSaludConNovedad7(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularSaludResidenciaExterior(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularSaludPorDefecto(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
        # PENSION
        if tipo_aporte == '02':
            tarifa = self.calcularPensionPorDefecto(pensionado_id)
            if tarifa is not None:
                monto = tarifa
            tarifa = self.calcularPensionConNovedad3(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularPensionNovedad3_7(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularPensionNovedad7(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularPensionAltoRiesgo(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularPensionCongresista(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularPensionCTI(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularPensionAviador(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
        # RIESGOS LABORALES
        if tipo_aporte == '03':
            tarifa = self.calcularRiesgosLabClaseUno(pensionado_id)
            if tarifa is not None:
                monto = tarifa
            tarifa = self.calcularRiesgosLabClaseDos(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularRiesgosLabClaseTres(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularRiesgosLabClaseCuatro(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa
            tarifa = self.calcularRiesgosLabClaseCinco(pensionado_id)
            if tarifa is not None and (monto is None or tarifa == 0 or
                                       (monto > 0 and tarifa > monto)):
                monto = tarifa

        if monto is None:
            monto = 0
        return monto

    def calcularSaludConNovedad3(self, pensionado_id):
        nov = Novedad.objects.filter(pensionado_id=pensionado_id,
                                     procesada=False).order_by(
                                     '-fechaCreacion')[:1]
        if len(nov) > 0 and nov[0].duracion <= 3:
            return 0

    def calcularSaludConNovedad3_7(self, pensionado_id):
        nov = Novedad.objects.filter(pensionado_id=pensionado_id,
                                     procesada=False).order_by(
                                     '-fechaCreacion')[:1]
        pen = Pensionado.objects.get(id=pensionado_id)
        if len(nov) > 0 and nov[0].duracion > 3 and nov[0].duracion <= 7:
            return round(pen.ingresoBaseCotizacion * Decimal(0.12), 2)

    def calcularSaludConNovedad7(self, pensionado_id):
        nov = Novedad.objects.filter(pensionado_id=pensionado_id,
                                     procesada=False).order_by(
                                     '-fechaCreacion')[:1]
        pen = Pensionado.objects.get(id=pensionado_id)
        if len(nov) > 0 and nov[0].duracion > 7:
            return round(pen.ingresoBaseCotizacion * Decimal(0.16), 2)

    def calcularSaludResidenciaExterior(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        if pen.pensionadoExterior and not pen.grupoFamiliarColombia:
            return 0

    def calcularSaludPorDefecto(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        return round(pen.ingresoBaseCotizacion * Decimal(0.12), 2)

    def calcularPensionPorDefecto(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        return round(pen.ingresoBaseCotizacion * Decimal(0.16), 2)

    def calcularPensionConNovedad3(self, pensionado_id):
        nov = Novedad.objects.filter(pensionado_id=pensionado_id,
                                     procesada=False).order_by(
                                     '-fechaCreacion')[:1]
        pen = Pensionado.objects.get(id=pensionado_id)
        if len(nov) > 0 and nov[0].tipo == '03' and nov[0].duracion <= 3:
            return 0

    def calcularPensionNovedad3_7(self, pensionado_id):
        nov = Novedad.objects.filter(pensionado_id=pensionado_id,
                                     procesada=False).order_by(
                                     '-fechaCreacion')[:1]
        pen = Pensionado.objects.get(id=pensionado_id)
        if (len(nov) > 0 and nov[0].tipo == '03' and nov[0].duracion > 3 and
           nov[0].duracion <= 7):
            return round(pen.ingresoBaseCotizacion * Decimal(0.12), 2)

    def calcularPensionNovedad7(self, pensionado_id):
        nov = Novedad.objects.filter(pensionado_id=pensionado_id,
                                     procesada=False).order_by(
                                     '-fechaCreacion')[:1]
        pen = Pensionado.objects.get(id=pensionado_id)
        if len(nov) > 0 and nov[0].tipo == '03' and nov[0].duracion > 7:
            return round(pen.ingresoBaseCotizacion * Decimal(0.16), 2)

    def calcularPensionAltoRiesgo(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        if pen.tarifaEspecial == '1':
            return round(pen.ingresoBaseCotizacion * Decimal(0.26), 2)

    def calcularPensionCongresista(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        if pen.tarifaEspecial == '2':
            return round(pen.ingresoBaseCotizacion * Decimal(0.255), 2)

    def calcularPensionCTI(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        if pen.tarifaEspecial == '3':
            return round(pen.ingresoBaseCotizacion * Decimal(0.35), 2)

    def calcularPensionAviador(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        if pen.tarifaEspecial == '4':
            return round(pen.ingresoBaseCotizacion * Decimal(0.21), 2)

    def calcularRiesgosLabClaseUno(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        if (pen.actividadEconomica == '8022' or
           pen.actividadEconomica == '8513'):
            return round(pen.ingresoBaseCotizacion * Decimal(0.00522), 2)

    def calcularRiesgosLabClaseDos(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        if (pen.actividadEconomica == '0117' or
           pen.actividadEconomica == '1541'):
            return round(pen.ingresoBaseCotizacion * Decimal(0.01044), 2)

    def calcularRiesgosLabClaseTres(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        if (pen.actividadEconomica == '1592' or
           pen.actividadEconomica == '1743'):
            return round(pen.ingresoBaseCotizacion * Decimal(0.02436), 2)

    def calcularRiesgosLabClaseCuatro(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        if (pen.actividadEconomica == '2101' or
           pen.actividadEconomica == '2322'):
            return round(pen.ingresoBaseCotizacion * Decimal(0.04350), 2)

    def calcularRiesgosLabClaseCinco(self, pensionado_id):
        pen = Pensionado.objects.get(id=pensionado_id)
        if (pen.actividadEconomica == '1431' or
           pen.actividadEconomica == '2321'):
            return round(pen.ingresoBaseCotizacion * Decimal(0.06960), 2)
