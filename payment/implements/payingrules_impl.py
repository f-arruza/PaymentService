# -*- coding: UTF-8 -*-
from payment.logic.payingrules import PayingRules


class PayingRulesImpl(PayingRules):
    def __init__(self):
        PayingRules.__init__(self)
