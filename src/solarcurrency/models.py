# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

BASE_CURRENCY = ['TRAC']


class SolarCurrency(models.Model):
    """
    Solar currency model for use of multiple apps
    Fields
        code: 4 letter code of currency as per
              Solar Standardization Authority 4217
        actual name: actual currency name
        convertion_rate_trac: convertion rate
                              1 <This SolarCurrency>: x Terra Coins
    """

    code = models.CharField(max_length=4)
    actual_name = models.CharField(max_length=20)
    convertion_rate_trac = models.DecimalField(
        max_digits=32, decimal_places=4, default=1.0)

    class Meta:
        ordering = ['pk']

    def terra_coin_value(self, amount=0):
        # Convert to Terra Coin
        return amount * convertion_rate_trac

    def __str__(self):
        #  Stringify value to return code
        return self.code
