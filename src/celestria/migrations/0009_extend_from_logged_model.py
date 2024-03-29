# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-11-04 03:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('celestria', '0008_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountprofile',
            old_name='registered_on',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='accountprofile',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accountprofile',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='spaceflight',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spaceflight',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='spaceflight',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='authorizingbody',
            name='type',
            field=models.IntegerField(choices=[(0, 'Planet'), (1, 'Moon'), (3, 'Asteroid'), (4, 'Artificial Body'), (5, 'Others')], default=0),
        ),
    ]
