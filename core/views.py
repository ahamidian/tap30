from django.http.response import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from core.models import Driver


def home(request):
    return HttpResponse("hello")


@csrf_exempt
def send_location(request):
    if request.method == "GET":
        return HttpResponseNotFound()

    driver, created = Driver.objects.get_or_create(number=request.POST["number"])
    driver.last_latitude = float(request.POST["lat"])
    driver.last_longitude = float(request.POST["long"])
    driver.save()

    return HttpResponse("got it")


def get_location(request):
    drivers_list = list(Driver.objects.all().values('number', 'last_latitude', 'last_longitude'))
    return JsonResponse(drivers_list, safe=False)
