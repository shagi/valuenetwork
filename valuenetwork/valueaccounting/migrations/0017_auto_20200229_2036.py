# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-29 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valueaccounting', '0016_auto_20200227_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='economicagent',
            name='address_ca',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='description_ca',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='email_ca',
            field=models.EmailField(blank=True, max_length=96, null=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='name_ca',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='nick_ca',
            field=models.CharField(help_text='Must be unique, and no more than 32 characters', max_length=32, null=True, unique=True, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='phone_primary_ca',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='primary phone'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='photo_url_ca',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='photo url'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='url_ca',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url'),
        ),
    ]
