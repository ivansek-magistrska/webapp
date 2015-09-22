# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_remove_configuration_aws_availability_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='aws_availability_zone',
            field=models.ForeignKey(default=1, to='frontend.AvailabilityZone'),
            preserve_default=False,
        ),
    ]
