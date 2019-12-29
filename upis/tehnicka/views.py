from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import  Predmet,Ucenik,Predmet_Ocjena,Priznanja,Skola,Smjer
from django.contrib.auth import authenticate, login, logout

import json
from .createUcenik import *

def index_view(request):
    smjerovi=Smjer.objects.all()
    skole=Skola.objects.all()
    context={
        'smjerovi':smjerovi,
        'skole':skole
        }
    return render(request, 'tehnicka/base.html',context)


def index_viev_predmet(request):
    predmeti=Predmet.objects.all()
    context={
        'predmeti':predmeti
        }
    return render(request,'tehnicka/dodajUcenika.html',context)
# Create your views here.

def dodajucenika(request):
        if request.method == "POST":
            try:
                return saveStudent(request)
            except KeyError:
               
                return HttpResponse(" Error dodajucenika")
        else: # GET request
           
            return getStudent(request)