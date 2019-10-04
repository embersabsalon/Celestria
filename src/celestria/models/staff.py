# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from account_profile import AccountProfile


class Staff(models.Model):
    REGULAR = 1
    SUPERVISOR = 2
    MANAGER = 3
    CAPTAIN = 4
    EXECUTIVE = 5
    RANK_CHOICES = (
        (REGULAR, 'Regular'),
        (SUPERVISOR, 'Supervisor'),
        (MANAGER, 'Manager'),
        (CAPTAIN, 'Captain'),
        (EXECUTIVE, 'Executive'))

    account_profile = models.OneToOneField(
        AccountProfile, related_name='staffs')
    staff_position = models.CharField(max_length=255)
    employed_on = models.DateTimeField()
    resigned_on = models.DateTimeField(
        null=True, blank=True)
    rank = models.IntegerField(
        choices=RANK_CHOICES, default=REGULAR)
