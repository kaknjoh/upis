from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import  Predmet,Ucenik,Predmet_Ocjena,Priznanja,Skola,Smjer,Razred,Takmicenje
from django.db import transaction
from django.urls import reverse

import sys

def deleteStudent(request, ucenik_id):
    ucenik=Ucenik.objects.get(id=ucenik_id)
    #smjer_id=ucenik.smjer.id ne moze ovako jer je ucenik-smjer M2M pa se vraca query set
    smjer_id=Smjer.objects.filter(ucenik__id=ucenik_id)
    smjer=smjer_id[0].id
    ucenik.delete()
    request.session['message']="Obrisan korisnik"
    return HttpResponseRedirect(reverse('tehnicka:index', args=(smjer,)))
