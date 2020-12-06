from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpRequest, Http404

# Create your views here.
def index(request):
    template = 'landingpage/index.html'
    return render(request,template,{})

def impressum(request):
    template = 'sites/impressum.html'
    return render(request,template,{})
