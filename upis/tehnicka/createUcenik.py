from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import  Predmet,Ucenik,Predmet_Ocjena,Priznanja,Skola,Smjer
from django.db import transaction
from django.urls import reverse

import sys

def getStudent(request):
    #ys.setrecursionlimit(10000)
  

    context={
    'smjerovi': Smjer.objects.all(),
    
    }
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    return render(request, 'tehnicka/dodajucenika.html', context)



def saveStudent(request):
    ime=request.POST['ime']
    prezime=request.POST['prezime']
    osnovna_skola=request.POST['skola']
    skola=Skola.objects.get(pk=osnovna_skola)
    smjer_id=request.POST['smjer']
    smjer=Smjer.objects.get(pk=smjer_id)

    predmet_razred6_ocjena=request.POST.getlist('razred6')
    predmet_razred7_ocjena=request.POST.getlist('razred7')
    predmet_razred8_ocjena=request.POST.getlist('razred8')
    predmet1_razred6_ocjena=request.POST.getlist('razred9')
    priznanja_naziv=request.POST.getlist('priznanje_naziv')
    priznanje_bodovi=request.POST.getlist('priznanje_bodovi')

    #Isto i sa i bez ovoga 
    transaction.set_autocommit(False)
    try:
        
        ucenik=Ucenik(ime=ime,prezime=prezime,smjer=smjer,skola_id=skola)
        ucenik.save()
        i=6
        j=1
        #Prva while petlja se koristi za prolazak kroz predmete 
        #Druga za razred 
        while j<3:
            predmet=Predmet.objects.get(id=j)
            while i<10:
                predmet_ocjene1=Predmet_Ocjena(ucenik=ucenik,predmet=predmet,ocjena= predmet_razred6_ocjena,razred=i)
                predmet_ocjene1.save()
                predmet_ocjene2=Predmet_Ocjena(ucenik=ucenik,predmet=predmet,ocjena= predmet_razred7_ocjena,razred=i)
                predmet_ocjene2.save()
                predmet_ocjene3=Predmet_Ocjena(ucenik=ucenik,predmet=predmet,ocjena= predmet_razred8_ocjena,razred=i)
                predmet_ocjene3.save()
                predmet_ocjene4=Predmet_Ocjena(ucenik=ucenik,predmet=predmet,ocjena= predmet_razred9_ocjena,razred=i)
                predmet_ocjene4.save()
                i=i+1
            j=j+1   
    except:
        transaction.rollback()
        raise
    else:
        transaction.commit()
    finally:
        transaction.set_autocommit(True)
