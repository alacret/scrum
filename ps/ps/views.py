from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def add(request):
    return render_to_response("add.html",{},context_instance = RequestContext(request))

def all(request):
    return render_to_response("pubs.html",{},context_instance = RequestContext(request))

def agregar(request):
	if request.method == 'POST':
		form = PublicacionForm(request.POST)
		if form.is_valid():
			return HttpResposeRedirect('/pubs')
	return HttpResposeRedirect('/')
