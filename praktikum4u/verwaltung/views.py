from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import HttpRequest, Http404
from .models import *
from django.contrib.auth.models import User
from praktikum4u import settings
from django.contrib.auth.hashers import make_password






# Create your views here.
def index(request):
    template = 'landingpage/index.html'
    return render(request,template,{})

def impressum(request):
    template = 'sites/impressum.html'
    return render(request,template,{})

def reg(request):
    template = 'sites/register.html'
    ds = User.objects.all()
    print(request.POST)
    if request.method == "GET":
        return render(request,template,{})
        
    else:
        button = request.POST['button']
        if button == "save":
            if 'dtsch' in request.POST  and 'ntzb' in request.POST:
                psw1 = request.POST['psw1']
                psw2 = request.POST['psw2']
                if psw1 == psw2:
                    psw2 = make_password(psw1)
                    username = request.POST['username']
                    if username != '':
                        first_name = request.POST['first_name']
                        if first_name != '':
                            last_name = request.POST['last_name']
                            if last_name != '':
                                email = request.POST['email']
                                if email != '':
                                    ds = User(username=username,first_name=first_name,last_name=last_name,email=email,password=psw2)
                                    ds.save()
                                    return render(request,template,{})
                                else:
                                    bitte = "Bitte E-Mail eingeben!"
                                    return render(request,template,{'bitte':bitte})                        
                            else:
                                bitte = "Bitte Nachnamen eingeben!"
                                return render(request,template,{'bitte':bitte})                        
                        else:
                            bitte = "Bitte Vornamen eingeben!"
                            return render(request,template,{'bitte':bitte})                        
                    else:
                        bitte = "Bitte Username eingeben!"
                        return render(request,template,{'bitte':bitte})                        
                else:
                    bitte = "Die Passwörter stimmen nicht überein!"
                    return render(request,template,{'bitte':bitte})
            elif 'dtsch' in request.POST:
                print("Nutzungsbedinungen fehlen!")
                bitte = "Bitte Akzeptieren sie die Nutzungsbedingungen!"
                return render(request,template,{'bitte':bitte})
            elif 'ntzb' in request.POST:
                print("Datenschutz Akzeptieren bitte!")
                bitte = "Bitte den Datenschutz Akzeptieren!"
                return render(request,template,{'bitte':bitte})
            else:
                print("Nix")
                bitte = "Bitte Akzeptieren sie die Nutzungsbedingungen sowie den Datenschutz!"
                return render(request,template,{'bitte':bitte})
        elif button == "cancel":
            return redirect("/")
        elif button == "delete":
            return render(request,template,{})

