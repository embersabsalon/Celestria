# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from solarcurrency.models import SolarCurrency


class SolarCurrencyAdmin(admin.ModelAdmin):
    model = SolarCurrency
    list_display = (
        'code', 'actual_name', 'convertion_rate_trac')


admin.site.register(SolarCurrency, SolarCurrencyAdmin)
