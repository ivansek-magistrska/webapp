# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20150608_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='aws_availability_zone',
        ),
    ]
