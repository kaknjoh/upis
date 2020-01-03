from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import  Predmet,Ucenik,Predmet_Ocjena,Priznanja,Smjer,Skola
from django.contrib.auth import authenticate, login, logout

import json
from .createUcenik import *
from .statistika import *
from .updateUcenik import *
from .deleteUcenik import *

#------------------ INDEX BASE --------------------------#
def index_base(request):
    context={
    'smjerovi': Smjer.objects.all()
    }
    return render(request, 'tehnicka/index_base.html',context)

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
#----------------------DODAJ UCENIKA -----------------------------------#

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

#------------ DETAILS UPDATE UCENIK -----------------------#
def details(request, ucenik_id):
    if request.method == "POST":
        try:
            return updateStudent(request, ucenik_id)
        except KeyError:
            return HttpResponse("Key error - post uredi")

    else:
        return get_for_update(request, ucenik_id)


#----------- DELETE UCENIK -----------------------------#
def delete(request, ucenik_id):

    if request.user.is_authenticated:
        return deleteStudent(request, ucenik_id)