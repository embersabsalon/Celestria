# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class AccountProfile(models.Model):
    CUSTOMER = 0
    STAFF = 1
    USER_TYPE_CHOICES = (
        (CUSTOMER, 'Customer'),
        (STAFF, 'Staff'),)

    user = models.OneToOneField(User, related_name='user_profile')
    registered_from = models.ForeignKey(AuthorizingBody)
    avatar = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=False)
    user_type = models.IntegerField(
        choices=USER_TYPE_CHOICES, default=CUSTOMER)

    password_reset_token = models.CharField(
        max_length=255, null=True, blank=True)
    password_reset_expiration = models.DateTimeField(null=True, blank=True)
