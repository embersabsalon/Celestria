# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-10-02 05:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('celestria', '0002_accountprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountprofile',
            name='current_body',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_accounts', to='celestria.AuthorizingBody'),
        ),
        migrations.AlterField(
            model_name='accountprofile',
            name='registered_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registered_accounts', to='celestria.AuthorizingBody'),
        ),
        migrations.AlterField(
            model_name='accountprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountprofile',
            name='user_type',
            field=models.IntegerField(choices=[(0, 'Customer'), (1, 'Staff'), (2, 'Admin')], default=0),
        ),
        migrations.AlterField(
            model_name='spaceport',
            name='authorizing_body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='space_ports', to='celestria.AuthorizingBody'),
        ),
    ]
