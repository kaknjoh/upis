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
    'skole':Skola.objects.all(),
    'predmeti':Predmet.objects.all()
    
    }
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    return render(request, 'tehnicka/dodajucenika.html', context)



def saveStudent(request):
    ime=request.POST['ime']
    prezime=request.POST['prezime']
    osnovna_skola=request.POST['osnovna_skola']
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
    
    try:
        
        ucenik=Ucenik(ime=ime,prezime=prezime,smjer_id=smjer,skola_id=skola)
        ucenik.save()
        temp=0
        #h je brojac za porlaz kroz listu gdje se nalaze ocjene za razred 6 
        i=1
        #Brojac koji se koristi da se prode kroz sve ocjene za predmete u 6 razredu
        #Spremanje ocjena za sve predemete u 6 razredu 
        #for predmet in predmeti:
        for ocjena in predmet_razred6_ocjena:
            predmet=Predmet.objects.get(pk=i)
            if(predmet.naziv_predmeta =='Informatika'):
                temp=temp+1
            else:
             predmet_ocjene1=Predmet_Ocjena(ucenik=ucenik,predmet=predmet,ocjena=ocjena,razred=6)
             predmet_ocjene1.save()
            i=i+1

        #Brojac za prolazak korz ocjene razreda 7 
        #Upis ocjena za sedmi razredd za sve predmete
        
        #for predmet in predmeti:
            #predmet_razred7_ocjena=predmet_razred6_ocjena[brojac]
            #brojac=brojac+1
            #Informatika, Fizika i hemija nemaju u 6 razredu 
            #if(predmet.naziv_predmeta=='Informatika' or predmet.naziv_predmeta=='Fizika' or predmet.naziv_predmeta=='Hemija'):
                #temp=temp+1
            #else:
                #predmet_ocjene1=Predmet_Ocjena(ucenik=ucenik,predmet=predmet,ocjena= predmet_razred7_ocjena,razred=7)
                #predmet_ocjene1.save()
        i=1
        for ocjena in predmet_razred7_ocjena:
           predmet1=Predmet.objects.get(pk=i)
           if(predmet1.naziv_predmeta =='Informatika'):
                temp=temp+1
           else:
             predmet_ocjene2=Predmet_Ocjena(ucenik=ucenik,predmet=predmet1,ocjena=ocjena,razred=7)
             predmet_ocjene2.save()
           i=i+1


       
    except:
        transaction.rollback()
        raise
    