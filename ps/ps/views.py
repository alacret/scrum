from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ps.forms import PublicacionForm, ComercianteForm
from comercio.models import Publicacion

def add(request):
    form = PublicacionForm()
    return render_to_response("add.html",{"form":form},context_instance = RequestContext(request))

def all(request):
	all = Publicacion.objects.all()
	return render_to_response("pubs.html",{'all':all},context_instance = RequestContext(request))

def registrar(request):
	if request.method == 'POST':
		comerciante = ComercianteForm(request.POST)
		comerciante.save()
		return HttpResposeRedirect('/login')
	else:
		form = ComercianteForm()
		return render_to_response("register.html",{"form":form},context_instance = RequestContext(request))


def agregar(request):
	saved_pub = save_pub(request.POST)
	if saved_pub is not None:
		where_to_go = '/pubs'
	else:
		where_to_go = '/'
	return HttpResponseRedirect(where_to_go)

def save_pub(post):
	form = PublicacionForm(post)
	if form.is_valid():
		return form.save()
	return None
	
