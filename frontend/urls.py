from django.conf.urls import url, patterns, include
from django.views import generic
from frontend import views
from backend import views as backend_views


angular_patterns = patterns('',
    url(r'^form-step1.html$', generic.TemplateView.as_view(template_name='frontend/form-step1.html'), name="form-step1"),
    url(r'^form-step2.html$', generic.TemplateView.as_view(template_name='frontend/form-step2.html'), name="form-step2"),
    url(r'^form-step3.html$', generic.TemplateView.as_view(template_name='frontend/form-step3.html'), name="form-step3"),
    url(r'^form-step4.html$', generic.TemplateView.as_view(template_name='frontend/form-step4.html'), name="form-step4"),
    url(r'^form-step5.html$', generic.TemplateView.as_view(template_name='frontend/form-step5.html'), name="form-step5"),
    url(r'^form-step6.html$', generic.TemplateView.as_view(template_name='frontend/form-step6.html'), name="form-step6"),
    url(r'^form-step7.html$', generic.TemplateView.as_view(template_name='frontend/form-step7.html'), name="form-step7")
)

urlpatterns = [
    url(r'$^', views.IndexView.as_view(), name='index'),
    url(r'^', include(angular_patterns), name='angular-patterns'),
    url(r'^finish', backend_views.FinishView.as_view()),
#    url(r'^get-openstack-data', views.GetOpenstackData.as_view(), name='get-openstack-data'),
    url(r'^ec2-instance-types$',  views.EC2InstanceTypesView.as_view(), name='ec2-instance-types'),
    url(r'^rds-instance-types$',  views.RDSInstanceTypesView.as_view(), name='rds-instance-types'),
    url(r'^get-availability-zones$',  views.AvailabilityZonesView.as_view(), name='get-availability-zones'),
    url(r'^get-regions$',  views.RegionsView.as_view(), name='get-regions'),
    url(r'^get-default-frontend-form-data', views.get_default_frontend_form_data, name='get-default-frontend-form-data'),
]