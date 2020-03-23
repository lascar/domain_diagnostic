import pdb
import re
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .forms import SpeedForm

@csrf_exempt
def speed_json(request):
    data = make_response(request.body.decode("utf-8"))
    return JsonResponse(data)

def speed_html(request):
    if request.method == 'POST':
        form = SpeedForm(request.POST)

        if form.is_valid():
            form = SpeedForm()
            body = request.body.decode("utf-8")
            response = make_response(body)
            response.update({'form': form})
            # return render(request, 'speed.html', {dict({'form': form}.items() + make_response(request.body.decode("utf-8").items()))})
            return render(request, 'speed.html', response)


    form = SpeedForm()
    return render(request, 'speed.html', {'form': form})

def make_response(request_body):
    error = ''
    time = 0
    status = ''
    domain = ''
    domain_regex = '.*domain=(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$|[a-z0-9]+[a-z0-9-.]*\.+[a-z]{2,}$)'
    match = re.findall(domain_regex, request_body)
    if ( match ):
        domain = match[0]
        response = requests.get('http://' + domain)
        time = response.elapsed.microseconds / 1000
        status = response.status_code
    else:
        error = 'dominio mal formado'

    return {'domain': domain, 'status': status, 'time': time, 'error': error}
