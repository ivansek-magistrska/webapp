# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_configuration_test_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='ec2instancetype',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rdsinstancetype',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
