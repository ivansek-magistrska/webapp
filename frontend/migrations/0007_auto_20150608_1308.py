# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_configuration_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date published'),
        ),
    ]
