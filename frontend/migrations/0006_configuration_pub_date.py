# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_remove_configuration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 8, 12, 59, 31, 4975, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
