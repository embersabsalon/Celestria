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
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)

    @property
    def fullname(self):
        if self.middle_name:
            return '{} {} {}'.format(
                self.first_name, self.middle_name, self.last_name)
        return '{} {}'.format(
            self.first_name, self.last_name)

    @property
    def age(self):
        if self.birth_date:
            return relativedelta(date.today() - self.birth_date).years
        return None
