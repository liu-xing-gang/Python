
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from app.forms import MomentForm
import os

# Create your views here.
def welcome(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect('welcome')
    else:
        form = MomentForm
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'app/templates', 'moments_input.html'), {'form': form})