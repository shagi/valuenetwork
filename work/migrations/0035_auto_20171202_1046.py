# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 10:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_auto_20170907_2253'),
        ('work', '0034_auto_20171202_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocp_unit_type',
            name='general_unit',
        ),
        migrations.RemoveField(
            model_name='ocp_unit_type',
            name='general_unit_type',
        ),
        migrations.RemoveField(
            model_name='ocp_unit_type',
            name='ocp_unit',
        ),
        migrations.DeleteModel(
            name='Ocp_Unit_Type',
        ),
        migrations.CreateModel(
            name='Ocp_Unit_Type',
            fields=[
            ],
            options={
                'verbose_name': 'Type of General Unit',
                'proxy': True,
                'verbose_name_plural': 'o-> Types of General Units',
                'indexes': [],
            },
            bases=('general.unit_type',),
        ),
    ]
