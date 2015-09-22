# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20150615_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
