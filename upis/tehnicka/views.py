from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import  Predmet,Ucenik,Predmet_Ocjena,Priznanja,Smjer,Skola
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template, render_to_string


import json
from .createUcenik import *
from .statistika import *
from .updateUcenik import *
from .deleteUcenik import *
from .pdf_statistika import *
from .pretragaUcenika import *
from .seeds import *


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

#----------------- POPUNJAVANJE BAZE PODACIMA ZA TEST --------------------------#

def popuniBazu(request):
    dodajSmjerove(request)
    dodajKljucnePredmete(request)
    dodajPredmete(request)
    dodajSkole(request)
    return HttpResponse("Baza popunjena")
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
                response=redirect('/tscze/')
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



#-------- RENDER TO PDF ---------------------#
#class HtmlPdf(FPDF, HTMLMixin):
    #pass


#def print_pdf(request):    
    #pdf = HtmlPdf()
    #pdf.add_page()
    #pdf.write_html(render_to_string('tehnicka/index.html'))

    #response = HttpResponse(pdf.output(dest='S').encode('latin-1'))
    #response['Content-Type'] = 'application/pdf'

   # return response
def get_pdf(request,smjer_id):
       return pdf_racunajStatistiku(request,smjer_id)


#---------------------- PRETRAGA UCENIKA ------------------------------------#

def pretraga(request,smjer_id):
    if request.method=="POST":
        return pretragaUcenika(request,smjer_id)

