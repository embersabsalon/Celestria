# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from authorizing_body import AuthorizingBody
from main.models.base_logged_model import BaseLoggedModel


class AccountProfile(BaseLoggedModel):
    CUSTOMER = 0
    STAFF = 1
    ADMIN = 2
    USER_TYPE_CHOICES = (
        (CUSTOMER, 'Customer'),
        (STAFF, 'Staff'),
        (ADMIN, 'Admin'),)

    user = models.OneToOneField(User, related_name='account_profile')
    registered_from = models.ForeignKey(
        AuthorizingBody, related_name='registered_accounts')
    current_body = models.ForeignKey(
        AuthorizingBody, related_name='current_accounts',
        null=True, blank=True)
    avatar = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=False)
    user_type = models.IntegerField(
        choices=USER_TYPE_CHOICES, default=CUSTOMER)

    password_reset_token = models.CharField(
        max_length=255, null=True, blank=True)
    password_reset_expiration = models.DateTimeField(null=True, blank=True)
