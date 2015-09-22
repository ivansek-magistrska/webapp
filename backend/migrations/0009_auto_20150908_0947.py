# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_log_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='skip_deployment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='configuration',
            name='skip_test',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='configuration',
            name='test_url',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
