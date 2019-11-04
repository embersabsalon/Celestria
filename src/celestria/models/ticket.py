# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from spacecraft import SpaceCraft
from spaceflight import SpaceFlight
from account_profile import AccountProfile
from main.models.base_logged_model import BaseLoggedModel


class Ticket(BaseLoggedModel):
    SELLING = 0
    RESERVED = 1
    BOARDED = 2
    CANCELLED = 3
    REFUNDED = 4

    STATUS_CHOICES = (
        (SELLING, 'Selling'),
        (RESERVED, 'Reserved'),
        (BOARDED, 'Boarded'),
        (CANCELLED, 'Cancelled'),
        (REFUNDED, 'Refunded'),
    )

    number = models.CharField(max_length=250, unique=True)
    flight = models.ForeignKey(
        SpaceFlight, related_name='tickets')
    sold_to = models.OneToOneField(
        AccountProfile, related_name='tickets_bought')
    seat_number = models.CharField(max_length=64)
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=SELLING)
    actual_price = models.DecimalField(
        default=0, max_digits=32,
        decimal_places=2, null=True, blank=True)
    sold_on = models.DateTimeField(
        null=True, blank=True)
    boarded_on = models.DateTimeField(
        null=True, blank=True)
    cancelled_on = models.DateTimeField(
        null=True, blank=True)
    refunded_on = models.DateTimeField(
        null=True, blank=True)
