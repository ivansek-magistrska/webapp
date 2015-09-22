# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20150612_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='test_finished',
            field=models.BooleanField(default=False),
        ),
    ]
