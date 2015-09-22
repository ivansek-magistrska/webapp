from django.contrib import admin

from backend import models

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'provider', 'ec2_instance_type', 'rds_instance_type')

class EC2InstanceTypeAdmin(admin.ModelAdmin):
    list_display = ('instance_type', 'vcpu_number', 'ram_size')

class RDSInstanceTypeAdmin(admin.ModelAdmin):
    list_display = ('instance_type', 'max_connections')

admin.site.register(models.RDSInstanceType, RDSInstanceTypeAdmin)
admin.site.register(models.EC2InstanceType, EC2InstanceTypeAdmin)
admin.site.register(models.AWSRegion)
admin.site.register(models.AvailabilityZone)
admin.site.register(models.Log)
admin.site.register(models.Configuration, ConfigurationAdmin)
