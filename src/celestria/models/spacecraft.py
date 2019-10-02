# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from authorizing_body import AuthorizingBody


class SpaceCraftManufacturer(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    headquarters_location = models.ForeignKey(
        AuthorizingBody, related_name='spacecraft_manufacturers')


class SpaceCraftModel(models.Model):
    GAS_ROCKET = 0
    ION_THRUSTER = 1
    SOLAR_SAIL = 2
    NUCLEAR_PULSE = 3
    FUSION_ROCKET = 4
    ANTIMATTER_ROCKET = 5
    OTHERS = 6

    PROPULSION_TYPE_CHOICES = (
        (GAS_ROCKET, 'Gas Rocket'),
        (ION_THRUSTER, 'Ion Thruster'),
        (SOLAR_SAIL, 'Solar Sail'),
        (NUCLEAR_PULSE, 'Nuclear Pulse'),
        (FUSION_ROCKET, 'Fusion'),
        (ANTIMATTER_ROCKET, 'Antimatter'),
        (OTHERS, 'Others'),
    )

    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    passenger_capacity = models.PositiveIntegerField()
    first_introduced = models.DateTimeField()
    retired_on = models.DateTimeField(null=True, blank=True)
    unit_price = models.DecimalField(
        default=0, max_digits=32, decimal_places=2, null=True, blank=True)
    propulsion_type = models.IntegerField(
        choices=PROPULSION_TYPE_CHOICES, default=ION_THRUSTER)
    manufacturer = models.ForeignKey(
        SpaceCraftManufacturer, related_name='space_craft_models',
        null=True, blank=True)


class SpaceCraft(models.Model):
    name = models.CharField(max_length=250)
    unit_number = models.CharField(max_length=250)
    manufacture_date = models.DateTimeField()
    passenger_capacity = models.PositiveIntegerField(
        null=True, blank=True)
    registering_body = models.ForeignKey(
        AuthorizingBody, related_name='space_crafts',
        null=True, blank=True)
    model = models.ForeignKey(
        SpaceCraftModel, related_name='space_crafts',
        null=True, blank=True)
