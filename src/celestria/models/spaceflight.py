# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from spaceport import SpacePort
from spacecraft import SpaceCraft
from main.models.base_logged_model import BaseLoggedModel


class SpaceFlight(BaseLoggedModel):
    ON_HOLD = 0
    BOARDING = 1
    TRAVELLING = 2
    ARRIVED = 3
    CANCELLED = 4

    STATUS_CHOICES = (
        (ON_HOLD, 'On Hold'),
        (BOARDING, 'Boarding'),
        (TRAVELLING, 'Travelling'),
        (ARRIVED, 'Arrived'),
        (CANCELLED, 'Cancelled'),
    )

    number = models.CharField(max_length=250)
    originating_port = models.ForeignKey(
        SpacePort, related_name='departing_space_flights')
    destination_port = models.ForeignKey(
        SpacePort, related_name='arriving_space_flights')
    estimated_departure_time = models.DateTimeField()
    actual_departure_time = models.DateTimeField(
        null=True, blank=True)
    estimated_arrival_time = models.DateTimeField()
    actual_arrival_time = models.DateTimeField(
        null=True, blank=True)
    estimated_duration = models.TimeField()
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=ON_HOLD)
    ticket_price = models.DecimalField(
        default=0, max_digits=32,
        decimal_places=2, null=True, blank=True)
