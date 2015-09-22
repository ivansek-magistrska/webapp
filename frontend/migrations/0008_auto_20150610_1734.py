# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_auto_20150608_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awsregion',
            name='availability_zones',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='aws_availability_zone',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='aws_region',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='ec2_instance_type',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='jmeter_instance_type',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='rds_instance_type',
        ),
        migrations.DeleteModel(
            name='Measurement',
        ),
        migrations.DeleteModel(
            name='AvailabilityZone',
        ),
        migrations.DeleteModel(
            name='AWSRegion',
        ),
        migrations.DeleteModel(
            name='Configuration',
        ),
        migrations.DeleteModel(
            name='EC2InstanceType',
        ),
        migrations.DeleteModel(
            name='RDSInstanceType',
        ),
    ]
