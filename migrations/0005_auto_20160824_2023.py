# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-24 20:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangonized_api_rest', '0004_auto_20160824_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietario', to=settings.AUTH_USER_MODEL),
        ),
    ]