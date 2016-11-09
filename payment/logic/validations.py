# -*- coding: UTF-8 -*-
class Validations():

    def __init__(self):
        pass

    def validate(self, pensionado):
        alerts = []
        alt = self.validateTipoPensionado(pensionado)
        if alt is not None:
            alerts.append(alt)
        alt = self.validateTipoPensionVsTipoPagador(pensionado)
        if alt is not None:
            alerts.append(alt)
        alt = self.validateTipoPensionVsTipoPensionado(pensionado)
        if alt is not None:
            alerts.append(alt)

        return alerts

    def validateTipoPensionado(self, pensionado):
        alert = 'No hay concordancia entre el Tipo de Pensionado'
        alert = alert + ' y el Tipo de Pagador.'

        referIzq = pensionado.tipoPensionado
        referDer = pensionado.empresaEmpleadora.tipoPagadorPensiones

        if (referIzq == '1' and referDer != '1' and referDer != '2' and
           referDer != '3'):
            return alert
        if (referIzq == '2' and referDer != '2' and referDer != '3'):
            return alert
        if (referIzq == '3' and referDer != '2'):
            return alert
        if (referIzq == '4' and referDer != '3'):
            return alert
        if (referIzq == '5' and referDer != '1'):
            return alert
        if (referIzq == '6' and referDer != '1'):
            return alert
        if (referIzq == '7' and referDer != '4'):
            return alert
        if (referIzq == '8' and referDer != '4'):
            return alert
        if (referIzq == '9' and referDer != '1' and referDer != '2' and
           referDer != '3'):
            return alert

        return None

    def validateTipoPensionVsTipoPagador(self, pensionado):
        alert = 'No hay concordancia entre el Tipo de Pension'
        alert = alert + ' y el Tipo de Pagador.'

        referIzq = pensionado.tipoPension
        referDer = pensionado.empresaEmpleadora.tipoPagadorPensiones

        if (referIzq == '1' and referDer != '2' and referDer != '3'):
            return alert
        if (referIzq == '5' and referDer != '3'):
            return alert
        if (referIzq == '6' and referDer != '3'):
            return alert
        if (referIzq == '7' and referDer != '3'):
            return alert
        if (referIzq == '9' and referDer != '3'):
            return alert
        if (referIzq == '10' and referDer != '1' and referDer != '3' and
           referDer != '4'):
            return alert
        if (referIzq == '11' and referDer != '1' and referDer != '3'):
            return alert
        if (referIzq == '12' and referDer != '1'):
            return alert
        if (referIzq == '13' and referDer != '1' and referDer != '3'):
            return alert
        if (referIzq == '14' and referDer != '1' and referDer != '3'):
            return alert
        if (referIzq == '15' and referDer != '3'):
            return alert
        if (referIzq == '16' and referDer != '2'):
            return alert

        return None

    def validateTipoPensionVsTipoPensionado(self, pensionado):
        alert = 'No hay concordancia entre el Tipo de Pension'
        alert = alert + ' y el Tipo de Pensionado.'

        referIzq = pensionado.tipoPension
        referDer = pensionado.tipoPensionado

        if (referIzq == '1' and referDer != '1' and referDer != '2' and
           referDer != '3'):
            return alert
        if (referIzq == '2' and referDer != '1' and referDer != '2' and
           referDer != '3' and referDer != '5' and referDer != '6' and
           referDer != '7' and referDer != '8'):
            return alert
        if (referIzq == '3' and referDer != '1' and referDer != '2' and
           referDer != '3' and referDer != '5' and referDer != '6' and
           referDer != '7' and referDer != '8'):
            return alert
        if (referIzq == '4' and referDer != '1' and referDer != '2' and
           referDer != '3' and referDer != '5' and referDer != '6' and
           referDer != '7' and referDer != '8'):
            return alert
        if (referIzq == '5' and referDer != '4' and referDer != '5' and
           referDer != '6'):
            return alert
        if (referIzq == '6' and referDer != '4' and referDer != '5' and
           referDer != '6'):
            return alert
        if (referIzq == '7' and referDer != '4' and referDer != '5' and
           referDer != '6'):
            return alert
        if (referIzq == '8' and referDer != '1' and referDer != '2' and
           referDer != '3' and referDer != '5' and referDer != '6' and
           referDer != '7' and referDer != '8'):
            return alert
        if (referIzq == '9' and referDer != '4'):
            return alert
        if (referIzq == '10' and referDer != '5' and referDer != '6' and
           referDer != '7' and referDer != '8'):
            return alert
        if (referIzq == '11' and referDer != '1' and referDer != '2' and
           referDer != '5' and referDer != '6' and referDer != '7' and
           referDer != '8'):
            return alert
        if (referIzq == '12' and referDer != '5' and referDer != '6'):
            return alert
        if (referIzq == '13' and referDer != '5' and referDer != '6'):
            return alert
        if (referIzq == '14' and referDer != '1' and referDer != '2' and
           referDer != '5' and referDer != '6'):
            return alert
        if (referIzq == '15' and referDer != '1' and referDer != '2'):
            return alert
        if (referIzq == '16' and referDer != '1'):
            return alert
        if (referIzq == '20' and referDer == '9'):
            return alert
        if (referIzq == '21' and referDer != '1' and referDer != '2' and
           referDer != '5' and referDer != '6' and referDer != '7' and
           referDer != '8'):
            return alert

        return None
