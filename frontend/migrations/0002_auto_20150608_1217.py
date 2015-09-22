# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='ec2_availability_zone',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='ec2_region',
        ),
    ]
