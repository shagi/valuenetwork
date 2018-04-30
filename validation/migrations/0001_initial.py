# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-18 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('valueaccounting', '0013_auto_20171106_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validation_date', models.DateField(auto_now_add=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='validations', to='valueaccounting.EconomicEvent')),
                ('validated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='validations', to='valueaccounting.EconomicAgent')),
            ],
            options={
                'ordering': ('validation_date',),
            },
        ),
    ]