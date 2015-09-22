# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iaasprovider',
            name='code_name',
        ),
        migrations.RemoveField(
            model_name='iaasprovider',
            name='display_name',
        ),
        migrations.AddField(
            model_name='iaasprovider',
            name='provider',
            field=models.CharField(default='aws', max_length=50, choices=[(b'openstack', b'OpenStack'), (b'google', b'Google Computing Cloud'), (b'aws', b'Amazon Web Services')]),
            preserve_default=False,
        ),
    ]
