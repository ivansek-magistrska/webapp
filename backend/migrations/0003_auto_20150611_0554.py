# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20150611_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='provider',
            field=models.CharField(max_length=20, choices=[(b'openstack', b'OpenStack'), (b'google', b'Google Computing Cloud'), (b'aws', b'Amazon Web Services')]),
        ),
        migrations.DeleteModel(
            name='IaasProvider',
        ),
    ]
