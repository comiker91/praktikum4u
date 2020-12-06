from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request):
    template = 'landingpage/index.html'
    return render(request,template,{})