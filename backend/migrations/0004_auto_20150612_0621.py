# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20150611_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='app_ami_id',
            field=models.CharField(max_length=20),
        ),
    ]
