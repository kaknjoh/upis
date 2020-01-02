from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import  Predmet,Ucenik,Predmet_Ocjena,Priznanja,Smjer,Skola
from django.contrib.auth import authenticate, login, logout

import json
from .createUcenik import *
from .statistika import *




def index_viev_predmet(request):
    predmeti=Predmet.objects.all()
    context={
        'predmeti':predmeti
        }
    return render(request,'tehnicka/dodajUcenika.html',context)


# Create your views here.
def index(request,smjer_id):
    message=''
    if request.session.get('message'):
        message='Korisnik obrisan!'
        del request.session['message']
    return racunajStatistiku(request, smjer_id, message)

def dodajucenika(request):
        if request.method == "POST":
            try:
                #predmet_razred9_ocjena=request.POST.getlist('razred9')
                #predmeti_razred7_ocjena=request.POST.getlist('razred7')
                #context={
                    #'ocjene':predmet_razred9_ocjena
                   # }
                #return render(request,'tehnicka/dodajUcenika.html',context)
                saveStudent(request)
                response=redirect('/admin/')
                return response
            except KeyError:
               
                return HttpResponse(" Error dodajucenika")
        else: # GET request
           
            return getStudent(request)