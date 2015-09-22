# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20150612_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='jmeter_aws_access_key',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='jmeter_aws_secret_key',
            field=models.CharField(max_length=50),
        ),
    ]
