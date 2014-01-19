from django.http import HttpResponse

def add(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def all(request):
    return HttpResponse("Hello, world. You're at the poll index.")
