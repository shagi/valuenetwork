# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-27 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valueaccounting', '0015_auto_20200202_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='economicagent',
            name='address_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='address_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='description_es',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='email_en',
            field=models.EmailField(blank=True, max_length=96, null=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='email_es',
            field=models.EmailField(blank=True, max_length=96, null=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='name_es',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='nick_en',
            field=models.CharField(help_text='Must be unique, and no more than 32 characters', max_length=32, null=True, unique=True, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='nick_es',
            field=models.CharField(help_text='Must be unique, and no more than 32 characters', max_length=32, null=True, unique=True, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='phone_primary_en',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='primary phone'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='phone_primary_es',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='primary phone'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='photo_url_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='photo url'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='photo_url_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='photo url'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='url_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='economicagent',
            name='url_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url'),
        ),
    ]