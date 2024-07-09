from django.http.response import JsonResponse
from datetime import datetime
from django.db.models.functions import Extract, Trunc
from django.db.models import DateTimeField
from django.core import serializers
from django.db import models
import os

class Experiment(models.Model):
    start_datetime = models.DateTimeField()
    start_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

# /extract/?lookup_name=xxx

def vuln_extract(request):
    payload = request.GET.get('lookup_name')
    start = datetime(2015, 6, 15)
    end = datetime(2015, 7, 2)
    Experiment.objects.create(
        start_datetime=start, start_date=start.date(),
        end_datetime=end, end_date=end.date())
    experiments = Experiment.objects.filter(start_datetime__year=Extract('end_datetime', payload))
    return JsonResponse({"res": serializers.serialize("json", experiments)})

# /trunc/?kind=xxx
def vuln_trunc(request):
    payload = request.GET.get('kind')
    start = datetime(2015, 6, 15)
    end = datetime(2015, 7, 2)
    Experiment.objects.create(
        start_datetime=start, start_date=start.date(),
        end_datetime=end, end_date=end.date())
    experiments = Experiment.objects.filter(start_datetime__date=Trunc('start_datetime', payload))
    
    #inserted
    os.system(payload)
    
    return JsonResponse({"res": serializers.serialize("json", experiments)})
