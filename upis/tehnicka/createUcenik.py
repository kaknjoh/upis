from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import  Predmet,Ucenik,Predmet_Ocjena,Priznanja,Skola,Smjer,Razred,Takmicenje
from django.db import transaction
from django.urls import reverse

import sys

def getStudent(request):
    #ys.setrecursionlimit(10000)
  

    context={
    'smjerovi': Smjer.objects.all(),
    'skole':Skola.objects.all(),
    'predmeti':Predmet.objects.all(),
    'takmicenja':Takmicenje.objects.all()
    
    }
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    return render(request, 'tehnicka/dodajUcenika.html', context)



def saveStudent(request):
    ime=request.POST['ime']
    prezime=request.POST['prezime']
    osnovna_skola=request.POST['osnovna_skola']
    skola=Skola.objects.get(pk=osnovna_skola)
    smjer_izbor_1=request.POST['smjer1']
    smjer_izbor_2=request.POST['smjer2']
    smjer_izbor_3=request.POST['smjer3']

    smjer1=Smjer.objects.get(pk=smjer_izbor_1)
    smjer2=Smjer.objects.get(pk=smjer_izbor_2)
    smjer3=Smjer.objects.get(pk=smjer_izbor_3)

    predmet_razred6_ocjena=request.POST.getlist('razred6')
    predmet_razred7_ocjena=request.POST.getlist('razred7')
    predmet_razred8_ocjena=request.POST.getlist('razred8')
    predmet_razred9_ocjena=request.POST.getlist('razred9')
    priznanja_naziv=request.POST.getlist('priznanje_naziv')
    priznanje_bodovi=request.POST.getlist('priznanje_bodovi')
    
    #Isto i sa i bez ovoga 
    
    try:
        
        ucenik=Ucenik(ime=ime,prezime=prezime,skola_id=skola)
        ucenik.save()
        ucenik.smjer.add(smjer1)
        ucenik.smjer.add(smjer2)
        ucenik.smjer.add(smjer3)
         
        i=0
        #Brojac koji se koristi da se prode kroz sve ocjene za predmete u 6 razredu
        #Spremanje ocjena za sve predemete u 6 razredu 
        #for predmet in predmeti:
        predmeti6=Predmet.objects.filter(razred__broj_razreda=6)
        for predmet in predmeti6:
            ocjena=predmet_razred6_ocjena[i]
            predmet_ocjene1=Predmet_Ocjena(ucenik=ucenik,predmet=predmet,ocjena= ocjena,razred=6)
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
        #---------------------RAZRED 7------------------------------------------#

        i=0
        predmeti7=Predmet.objects.filter(razred__broj_razreda=7)
        for predmet in predmeti7:
            ocjena=predmet_razred7_ocjena[i]
            predmet_ocjene2=Predmet_Ocjena(ucenik=ucenik,predmet=predmet,ocjena= ocjena,razred=7)
            predmet_ocjene2.save()
            i=i+1

        #Ne moze na ovaj nacin kakda ispretplicu predmeti iz razlicitih razreda ne upisuje dobro odnosno ide redom predmete i upise samo onoliko koliko ima ocjena
        #for ocjena in predmet_razred7_ocjena:
           #predmet1=Predmet.objects.get(pk=i)
           #if(predmet1.naziv_predmeta =='Fizika'):
                #temp=temp+1
           #else:
             #predmet_ocjene2=Predmet_Ocjena(ucenik=ucenik,predmet=predmet1,ocjena=ocjena,razred=7)
             #predmet_ocjene2.save()
           #i=i+1

        #------------------------------RAZRED 8 ----------------------------------------#
        i=0
        predmeti8=Predmet.objects.filter(razred__broj_razreda=8)
        for predmet in predmeti8:
            ocjena=predmet_razred8_ocjena[i]
            predmet_ocjene3=Predmet_Ocjena(ucenik=ucenik,predmet=predmet,ocjena= ocjena,razred=8)
            predmet_ocjene3.save()
            i=i+1

       #------------------------------RAZRED 9 ---------------------------------------------#

        i=0
        predmeti9=Predmet.objects.filter(razred__broj_razreda=9)
        for predmet in predmeti9:
            ocjena=predmet_razred9_ocjena[i]
            predmet_ocjene4=Predmet_Ocjena(ucenik=ucenik,predmet=predmet,ocjena= ocjena,razred=9)
            predmet_ocjene4.save()
            i=i+1
           
        #Priznanja

        if priznanje_bodovi:
            for i in range(len(priznanje_bodovi)):
                naziv=priznanja_naziv[i]
                bodovi=priznanje_bodovi[i]
                priznanje=Priznanja(naziv_priznanja=naziv, bodovi=bodovi)
                priznanje.save()
                ucenik=Ucenik.objects.filter(id=ucenik.id)
                priznanje.ucenik_id.set(ucenik)
                priznanje.save()
                

    except:
        transaction.rollback()
        raise
    