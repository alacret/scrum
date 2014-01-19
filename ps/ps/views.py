from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def add(request):
    return render_to_response("add.html",{},context_instance = RequestContext(request))

def all(request):
    return render_to_response("pubs.html",{},context_instance = RequestContext(request))
