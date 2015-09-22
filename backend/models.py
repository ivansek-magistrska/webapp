from django.db import models
import hashlib
from swampdragon.models import SelfPublishModel
from serializers import LogSerializer

IAAS_PROVIDERS = (
    ('openstack', 'OpenStack'),
    ('google', 'Google Computing Cloud'),
    ('aws', 'Amazon Web Services')
)

class AvailabilityZone(models.Model):
    abbreviation = models.CharField(max_length=20)

    def __str__(self):
        return self.abbreviation

class AWSRegion(models.Model):
    display_name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=20)
    availability_zones = models.ForeignKey(AvailabilityZone)

    def __str__(self):
        return self.display_name

class RDSInstanceType(models.Model):
    instance_type = models.CharField(max_length=20)
    max_connections = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.instance_type

    class Meta:
        verbose_name = "RDS instance type"

class EC2InstanceType(models.Model):
    instance_type = models.CharField(max_length=20)
    vcpu_number = models.IntegerField(verbose_name='# VCPU')
    ram_size = models.FloatField(verbose_name='RAM size')
    price = models.FloatField()

    def __str__(self):
        return self.instance_type

    class Meta:
        verbose_name = "EC2 instance type"

class Configuration(models.Model):

    pub_date = models.DateTimeField('date published', auto_now=True)
    results_id = models.CharField(max_length=36)

    provider = models.CharField(max_length=20, choices=IAAS_PROVIDERS)
    test_finished = models.BooleanField(default=False)
    skip_deployment = models.BooleanField(default=False)
    skip_test = models.BooleanField(default=False)
    test_url = models.TextField()

    '''
    Database
    '''
    db_name = models.CharField(max_length=20)
    db_username = models.CharField(max_length=20)
    db_password = models.CharField(max_length=32)
    db_dump_url = models.CharField(max_length=1000)
    db_num_instances = models.IntegerField()

    '''
    Application
    '''
    app_distribution_url = models.CharField(max_length=1000)
    app_connection_pool_size = models.IntegerField()
    app_num_instances = models.IntegerField()
    app_ami_id = models.CharField(max_length=20)

    '''
    Auto scalability
    '''
    as_is_enabled = models.BooleanField(default=False)
    as_cooldown = models.IntegerField()

    '''
    AWS account information
    '''
    aws_access_key_id = models.CharField(max_length=50)
    aws_secret_key_id = models.CharField(max_length=50)
    aws_region = models.ForeignKey(AWSRegion, related_name='aws_region')
    aws_availability_zone = models.ForeignKey(AvailabilityZone)

    '''
    RDS settings
    '''
    rds_instance_type = models.ForeignKey(RDSInstanceType)
    rds_num_replicas = models.IntegerField()
    rds_master_identifier = models.CharField(max_length=20)
    rds_slave_identifier = models.CharField(max_length=20)

    '''
    EC2 settings
    '''
    ec2_instance_type = models.ForeignKey(EC2InstanceType, related_name='ec2_instance_type')
    ec2_ami_id = models.CharField(max_length=20)
    ec2_key_name = models.CharField(max_length=20)
    ec2_remote_user = models.CharField(max_length=20)
    ec2_instance_identifier = models.CharField(max_length=20)

    '''
    JMeter settings
    '''
    jmeter_aws_secret_key = models.CharField(max_length=50)
    jmeter_aws_access_key = models.CharField(max_length=50)
    jmeter_instance_type = models.ForeignKey(EC2InstanceType)
    jmeter_num_threads = models.IntegerField()
    jmeter_duration_in_minutes = models.IntegerField()
    jmeter_ami_id = models.CharField(max_length=20)
    jmeter_key_name = models.CharField(max_length=20)
    jmeter_url = models.CharField(max_length=1000)

    def __str__(self):
        return '%s|%s|%s|%s' % (
            self.id,
            self.provider.title().lower(),
            self.ec2_instance_type,
            self.rds_instance_type
        )

class Measurement(models.Model):
    graphs_file_path = models.CharField(max_length=1024)

class Log(SelfPublishModel, models.Model):
    serializer_class = LogSerializer
    configuration = models.ForeignKey(Configuration)
    message = models.TextField()
    finished = models.BooleanField(default=False)

    def _publish(self, action, changed_fields=None):
        suffix = '_%s' % self.configuration.id
        if not str(self.serializer_class.Meta.base_channel).endswith(suffix):
            self.serializer_class.Meta.base_channel += suffix
        super(Log, self)._publish(action, changed_fields)