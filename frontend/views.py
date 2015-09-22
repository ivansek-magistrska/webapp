import uuid

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from backend import models
from loadtesting.settings import FRONTEND_DEFAULT_SETTINGS


class IndexView(View):
    template_name = 'frontend/index.html'

    def get(self, request):
        if request.session.get('uid') == None:
            request.session['uid'] = str(uuid.uuid4())

        return render(request, self.template_name, {'uid': request.session.get('uid')})

class EC2InstanceTypesView(View):

    def get(self, request):
        instance_types = models.EC2InstanceType.objects.all()
        return JsonResponse([{'id': i.id, 'name': i.instance_type} for i in instance_types], safe=False)

class RDSInstanceTypesView(View):
    def get(self, request):
        instance_types = models.RDSInstanceType.objects.all()
        return JsonResponse([{'id': i.id, 'name': i.instance_type} for i in instance_types], safe=False)

class AvailabilityZonesView(View):

    def get(self, request):
        availability_zones = models.AvailabilityZone.objects.all()
        return JsonResponse([{'id': i.id, 'name': i.abbreviation} for i in availability_zones], safe=False)

class RegionsView(View):

    def get(self, request):
        regions = models.AWSRegion.objects.all()
        return JsonResponse([{'id': i.id, 'name': i.display_name} for i in regions], safe=False)



def get_default_frontend_form_data(request):
    if request.is_ajax():
        return JsonResponse(FRONTEND_DEFAULT_SETTINGS, safe=False)
    return HttpResponse(status=500)
