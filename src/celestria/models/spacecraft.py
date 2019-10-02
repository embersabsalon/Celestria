# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from authorizing_body import AuthorizingBody


class SpaceCraft(models.Model):
    name = models.CharField(max_length=250)
    passenger_capacity = models.PositiveIntegerField()
    registering_body = models.ForeignKey(
        AuthorizingBody, related_name='space_crafts')
