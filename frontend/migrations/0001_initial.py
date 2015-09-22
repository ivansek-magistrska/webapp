# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilityZone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abbreviation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AWSRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(max_length=20)),
                ('abbreviation', models.CharField(max_length=20)),
                ('availability_zones', models.ForeignKey(to='frontend.AvailabilityZone')),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('db_name', models.CharField(max_length=20)),
                ('db_username', models.CharField(max_length=20)),
                ('db_password', models.CharField(max_length=32)),
                ('db_dump_url', models.CharField(max_length=1000)),
                ('db_num_instances', models.IntegerField()),
                ('app_distribution_url', models.CharField(max_length=1000)),
                ('app_num_instances', models.IntegerField()),
                ('app_ami_id', models.CharField(max_length=10)),
                ('app_connection_pool_size', models.IntegerField()),
                ('as_is_enabled', models.BooleanField(default=False)),
                ('as_cooldown', models.IntegerField()),
                ('aws_access_key_id', models.CharField(max_length=50)),
                ('aws_secret_key_id', models.CharField(max_length=50)),
                ('aws_availability_zone', models.CharField(max_length=20)),
                ('rds_num_replicas', models.IntegerField()),
                ('rds_master_identifier', models.CharField(max_length=20)),
                ('rds_slave_identifier', models.CharField(max_length=20)),
                ('ec2_ami_id', models.CharField(max_length=20)),
                ('ec2_key_name', models.CharField(max_length=20)),
                ('ec2_remote_user', models.CharField(max_length=20)),
                ('ec2_instance_identifier', models.CharField(max_length=20)),
                ('ec2_availability_zone', models.CharField(max_length=20)),
                ('jmeter_aws_secret_key', models.CharField(max_length=32)),
                ('jmeter_aws_access_key', models.CharField(max_length=32)),
                ('jmeter_num_threads', models.IntegerField()),
                ('jmeter_duration_in_minutes', models.IntegerField()),
                ('jmeter_ami_id', models.CharField(max_length=20)),
                ('jmeter_key_name', models.CharField(max_length=20)),
                ('jmeter_url', models.CharField(max_length=1000)),
                ('aws_region', models.ForeignKey(related_name='aws_region', to='frontend.AWSRegion')),
            ],
        ),
        migrations.CreateModel(
            name='EC2InstanceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instance_type', models.CharField(max_length=20)),
                ('vcpu_number', models.IntegerField(verbose_name=b'# VCPU')),
                ('ram_size', models.FloatField(verbose_name=b'RAM size')),
            ],
            options={
                'verbose_name': 'EC2 instance type',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('graphs_file_path', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='RDSInstanceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instance_type', models.CharField(max_length=20)),
                ('max_connections', models.IntegerField()),
            ],
            options={
                'verbose_name': 'RDS instance type',
            },
        ),
        migrations.AddField(
            model_name='configuration',
            name='ec2_instance_type',
            field=models.ForeignKey(related_name='ec2_instance_type', to='frontend.EC2InstanceType'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='ec2_region',
            field=models.ForeignKey(to='frontend.AWSRegion'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='jmeter_instance_type',
            field=models.ForeignKey(to='frontend.EC2InstanceType'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='rds_instance_type',
            field=models.ForeignKey(to='frontend.RDSInstanceType'),
        ),
    ]
