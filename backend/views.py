import json
from logging import Logger
import logging
import traceback
import uuid
import boto
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
import models, tasks
from models import Log
import backend.tasks as tasks
import os
from django.views.generic import DetailView

class ResultsView(DetailView):
    model = models.Configuration
    template_name = 'frontend/results.html'


class MyLogger(Logger):

    def __init__(self, configuration):
        self.configuration = configuration

    def log(self, msg, level=logging.INFO, append_to_last=False, fin=False):

        if append_to_last:
            log = Log.objects.filter(configuration=self.configuration).order_by('id').last()
            log.message += msg
        else:
            log = Log()
            log.configuration = self.configuration
            log.message = msg

        log.finished = fin
        log.save()

class FinishView(View):
    def post(self, request):
        errors = []
        if request.is_ajax():
            try:
                data = json.loads(request.POST.get('formData')) if request.POST.get('formData', None) else json.loads(request.body)
                configuration = self.save_configuration(data, data['provider'])

                results_dir = "%s/results/%s" % (os.path.abspath(os.path.dirname(__file__)), configuration.results_id)
                config_path = self.write_config(configuration, results_dir)

                scenario_path = self.handle_uploaded_file(request.FILES['file'], results_dir)

                logger = MyLogger(configuration)
                tasks.deployment_scripts_task.delay(scenario_path, configuration, config_path, results_dir, logger)

                return HttpResponse(json.dumps({'task_id': configuration.id}), status=200, content_type='application/json')
            except Exception as e:
                errors.append(traceback.format_exc())
        else:
            errors.append('Only AJAX requests are allowed!')
        return HttpResponse(json.dumps({'errors': errors}), status=500, content_type='application/json')

    def handle_uploaded_file(self, f, results_dir):
        filename = '%s/scenario.jmx' % results_dir
        with open(filename, 'w+') as fp:
            for chunk in f.chunks():
                fp.write(chunk)
        return filename

    def write_config(self, configuration, results_dir):
        os.makedirs(results_dir)
        filename = "%s/config.ini" % results_dir
        fp = open(filename, 'w+')

        if configuration.provider == 'aws':
            cfg = self.create_aws_config(configuration, fp)
        elif configuration.provider == 'openstack':
            cfg = self.create_openstack_config(configuration)
        elif configuration.provider == 'google':
            cfg = self.create_google_config(configuration)
        else:
            raise Exception("Wrong provider")


        cfg.write(fp)
        fp.close()
        return filename

    def create_openstack_config(self, configuration):
        raise Exception('Not implemented')

    def create_google_config(self, configuration):
        raise Exception('Not implemented')

    def create_aws_config(self, configuration, fp):
        cfg = boto.Config(fp=fp)

        section = 'DATABASE'
        cfg.add_section(section)
        cfg.set(section, 'name', configuration.db_name)
        cfg.set(section, 'user', configuration.db_username)
        cfg.set(section, 'password', configuration.db_password)
        cfg.set(section, 'dump_url', configuration.db_dump_url)

        section = 'APPLICATION'
        cfg.add_section(section)
        cfg.set(section, 'distribution_url', configuration.app_distribution_url)
        cfg.set(section, 'connection_pool_size', configuration.app_connection_pool_size)
        cfg.set(section, 'num_instances', str(configuration.app_num_instances))

        section = 'AUTO_SCALABILITY'
        cfg.add_section(section)
        cfg.set(section, 'enabled', 'yes' if configuration.as_is_enabled == True else 'no')
        cfg.set(section, 'cooldown', str(configuration.as_cooldown))

        section = 'AWS'
        cfg.add_section(section)
        cfg.set(section, 'aws_access_key_id', configuration.aws_access_key_id)
        cfg.set(section, 'aws_secret_access_key', configuration.aws_secret_key_id)
        cfg.set(section, 'region', configuration.aws_region.abbreviation)
        cfg.set(section, 'availability_zone', configuration.aws_availability_zone.abbreviation)

        section = 'RDS'
        cfg.add_section(section)
        cfg.set(section, 'instance_type', configuration.rds_instance_type.instance_type)
        cfg.set(section, 'num_replicas', str(configuration.rds_num_replicas))
        cfg.set(section, 'master_identifier', configuration.rds_master_identifier)
        cfg.set(section, 'replica_identifier', configuration.rds_slave_identifier)

        section = 'EC2'
        cfg.add_section(section)

        cfg.set(section, 'instance_type', configuration.ec2_instance_type.instance_type)
        cfg.set(section, 'ami_id', configuration.ec2_ami_id)
        cfg.set(section, 'key_name', configuration.ec2_key_name)
        cfg.set(section, 'key_pair', '<auto generated>')
        cfg.set(section, 'remote_user', configuration.ec2_remote_user)
        cfg.set(section, 'instance_identifier', configuration.ec2_instance_identifier)

        return cfg

    def save_openstack_configuration(self, data):
        raise Exception("Not implemented")

    def save_google_configuration(self, data):
        raise Exception("Not implemented")

    def save_configuration(self, data, provider):
        if provider == 'aws':
            return self.save_aws_configuration(data)
        elif provider == 'openstack':
            return self.save_openstack_configuration(data)
        elif provider == 'google':
            return self.save_google_configuration(data)
        else:
            raise Exception("Wrong provider")

    def save_aws_configuration(self, data):
        configuration = models.Configuration()

        configuration.provider = data['provider']
        configuration.db_password = data['db']['password']
        configuration.db_username = data['db']['username']
        configuration.db_name = data['db']['name']
        configuration.db_dump_url = data['db']['url']
        configuration.db_num_instances = data['db']['num_instances']

        configuration.rds_master_identifier = data['db']['master_identifier']
        configuration.rds_slave_identifier = data['db']['replica_identifier']
        configuration.rds_num_replicas = data['db']['num_replicas']
        configuration.rds_instance_type = get_object_or_404(models.RDSInstanceType, pk=data['db']['instance_type']['id'])

        configuration.app_distribution_url = data['fr']['dist_url']
        configuration.app_connection_pool_size = data['fr']['connection_pool_size']
        configuration.app_num_instances = data['fr']['num_instances']
        configuration.app_ami_id = data['fr']['ami_id']

        configuration.aws_access_key_id = data['fr']['access_key']
        configuration.aws_secret_key_id = data['fr']['secret_key']
        configuration.aws_region = get_object_or_404(models.AWSRegion, pk=data['fr']['region']['id'])
        configuration.aws_availability_zone = get_object_or_404(models.AvailabilityZone, pk=data['fr']['availability_zone']['id'])

        configuration.ec2_instance_type = get_object_or_404(models.EC2InstanceType, pk=data['fr']['instance_type']['id'])
        configuration.ec2_ami_id = data['fr']['ami_id']
        configuration.ec2_key_name = data['fr']['keyname']
        configuration.ec2_remote_user = data['fr']['remote_user']
        configuration.ec2_instance_identifier = data['fr']['instance_identifier']

        configuration.jmeter_aws_access_key = data['jmeter']['aws_access_key']
        configuration.jmeter_aws_secret_key = data['jmeter']['aws_secret_key']
        configuration.jmeter_ami_id = data['jmeter']['ami_id']
        configuration.jmeter_url = data['jmeter']['url']
        configuration.jmeter_duration_in_minutes = data['jmeter']['scenario_duration']
        configuration.jmeter_instance_type = get_object_or_404(models.EC2InstanceType, pk=data['jmeter']['instance_type']['id'])
        configuration.jmeter_num_threads = data['jmeter']['num_threads']
        configuration.jmeter_key_name = data['jmeter']['key_name']

        configuration.as_cooldown = data['fr']['cooldown']
        configuration.as_is_enabled = True if data['fr']['autoscaling'] == 'yes' else False

        configuration.results_id = uuid.uuid4()

        configuration.save()

        return configuration
