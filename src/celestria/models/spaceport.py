# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from authorizing_body import AuthorizingBody


class SpacePort(models.Model):
    DOMESTIC = 0
    INTERPLANETARY = 1
    INTERSTELLAR = 2
    INTERGALACTIC = 3

    TYPE_CHOICES = (
        (DOMESTIC, 'Domestic'),
        (INTERPLANETARY, 'Interplanetary'),
        (INTERSTELLAR, 'Interstellar'),
        (INTERGALACTIC, 'Intergalactic'),
    )

    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    authorizing_body = models.ForeignKey(AuthorizingBody)
    type = models.IntegerField(choices=TYPE_CHOICES, default=INTERPLANETARY)
