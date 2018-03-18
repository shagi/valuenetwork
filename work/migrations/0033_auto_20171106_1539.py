# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0032_auto_20170705_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinrequest',
            name='email_address',
            field=models.EmailField(max_length=96, verbose_name='Email address *'),
        ),
        migrations.AlterField(
            model_name='joinrequest',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name *'),
        ),
        migrations.AlterField(
            model_name='joinrequest',
            name='requested_username',
            field=models.CharField(help_text='If you have already an account in OCP, you can put the same username to have this project in the same account, or you can choose another username to have it separate.', max_length=32, verbose_name='Username *'),
        ),
        migrations.AlterField(
            model_name='joinrequest',
            name='type_of_user',
            field=models.CharField(choices=[(b'individual', 'individual'), (b'collective', 'collective')], default=b'individual', help_text='* Required fields', max_length=12, verbose_name='Type of user *'),
        ),
    ]