# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AuthorizingBody(models.Model):
    PLANET = 0
    MOON = 1
    DWARF_PLANET = 2
    ASTEROID = 3
    ARTIFICIAL_BODY = 4
    OTHERS = 5

    TYPE_CHOICES = (
        (PLANET, 'Planet'),
        (MOON, 'Moon'),
        (ASTEROID, 'Asteroid'),
        (ARTIFICIAL_BODY, 'Artificial Body'),
        (OTHERS, 'Others'),
    )

    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    type = models.IntegerField(choices=TYPE_CHOICES, default=PLANET)
    is_active = models.BooleanField(default=True)
    docking_tax = models.DecimalField(
        default=0, max_digits=4, decimal_places=2, null=True, blank=True)
