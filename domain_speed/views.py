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
def speed(request):
    error = ''
    time = 0
    status = ''
    domain = ''
    if request.method == 'POST':
        form = SpeedForm(request.POST)
        headers_accept = request.headers['Accept']

        # pdb.set_trace()
        if headers_accept == 'application/json':
            json_domain_regex = 'domain=(.*)'
            match = re.match(json_domain_regex, request.body.decode("utf-8"))
            json_request = True
            domain = match.group(1)
        else:
            if form.is_valid():
                json_request = False
                domain = form['domain'].value()
                form = SpeedForm()
                # pdb.set_trace()
            else:
                form = SpeedForm()
                return render(request, 'speed.html', {'form': form, 'domain': domain, 'time': time, 'error': error, 'status': status})

        ip = re.compile('^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$')
        domain_name = re.compile('^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$')

        if domain_name.match(domain) or ip.match(domain):
            response = requests.get('http://' + domain)
            time = response.elapsed.microseconds / 1000
            status = response.status_code
        else:
            error = 'dominio mal formado'
        
        if json_request:
            data = {
                'domain': domain,
                'time': time,
                'error': error,
                'status': status,
            }
            return JsonResponse(data)
        else:
            return render(request, 'speed.html', {'form': form, 'domain': domain, 'time': time, 'error': error, 'status': status})

    form = SpeedForm()
    return render(request, 'speed.html', {'form': form, 'domain': domain, 'time': time, 'error': error, 'status': status})
