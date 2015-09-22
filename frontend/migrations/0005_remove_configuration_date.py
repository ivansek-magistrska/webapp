# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_configuration_aws_availability_zone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='date',
        ),
    ]
