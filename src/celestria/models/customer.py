# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from account_profile import AccountProfile


class Customer(models.Model):
    REGULAR = 1
    PREMIUM = 2
    TYPE_CHOICES = (
        (REGULAR, 'Regular'),
        (PREMIUM, 'Premium'))

    account_profile = models.OneToOneField(
        AccountProfile, related_name='customers')
    type = models.IntegerField(
        choices=TYPE_CHOICES, default=REGULAR)
