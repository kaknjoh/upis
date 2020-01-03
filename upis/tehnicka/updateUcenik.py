from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import  Predmet,Ucenik,Predmet_Ocjena,Priznanja,Skola,Smjer,Razred,Takmicenje
from django.db import transaction
from django.urls import reverse

import sys

def get_for_update(request, ucenik_id):
    ucenik=Ucenik.objects.get(id=ucenik_id)
    sesti_predmeti=Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=6)
    sedmi_predmeti=Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=7)
    osmi_predmeti=Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=8)
    deveti_predmeti=Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=9)
   
    context={
    'ucenik':ucenik,
    'sesti':sesti_predmeti,
    'sedmi':sedmi_predmeti,
    'osmi':osmi_predmeti,
    'deveti':deveti_predmeti,
    'smjerovi':Smjer.objects.all(),
    'priznanja':Priznanja.objects.filter(ucenik_id=ucenik)
    }
    if request.user.is_authenticated:
        return render(request, 'tehnicka/details.html',context)
    else:
        return render(request, "users/login.html", {"message": "Please log in."})


    #-------------- UPDATE FUNKCIJA -------------------#

def updateStudent(request,ucenik_id):
        ime=request.POST["ime"]
        prezime=(request.POST["prezime"])
        osnovna_skola=(request.POST["osnovna_skola"])
        smjer_id=(request.POST["smjer"])
        smjer=Smjer.objects.get(id=smjer_id)

        razred6_ocjene=request.POST.getlist('razred6_ocjene')
        razred7_ocjene=request.POST.getlist('razred7_ocjene')
        razred8_ocjene=request.POST.getlist('razred8_ocjene')
        razred9_ocjene=request.POST.getlist('razred9_ocjene')

        priznanja_naziv=request.POST.getlist('priznanje_naziv')
        priznanje_bodovi=request.POST.getlist('priznanje_bodovi')
        vrsta_takmicenja=request.POST.getlist('vrsta_takmicenja')
        ucenik=Ucenik.objects.get(id=ucenik_id)

        #-----------------  6 RAZRED -------------------------------#
        #Sve ocjene za predmete u 6 razredu, updateovanje za promjene ocjena u 6 razredu#
        #------------------------------------------------------------#
        predmeti6_ocjene_update=Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=6)
        i=0
        for predmet in predmeti6_ocjene_update:
            predmet.ocjena=razred6_ocjene[i]
            predmet.save()
            i=i+1

        #-----------------  7 RAZRED -------------------------------#
        #Sve ocjene za predmete u 7 razredu, updateovanje za promjene ocjena u 7 razredu#
        #------------------------------------------------------------#
        predmeti7_ocjene_update=Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=7)
        i=0
        for predmet in predmeti7_ocjene_update:
            predmet.ocjena=razred7_ocjene[i]
            predmet.save()
            i=i+1
        #-----------------  8 RAZRED -------------------------------#
        #Sve ocjene za predmete u 8 razredu, updateovanje za promjene ocjena u 8 razredu#
        #------------------------------------------------------------#

        predmeti8_ocjene_update=Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=8)
        i=0
        for predmet in predmeti8_ocjene_update:
            predmet.ocjena=razred8_ocjene[i]
            predmet.save()
            i=i+1

        #-----------------  9 RAZRED -------------------------------#
        #Sve ocjene za predmete u 9 razredu, updateovanje za promjene ocjena u 9 razredu#
        #------------------------------------------------------------#
        predmeti9_ocjene_update=Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=9)
        i=0
        for predmet in predmeti9_ocjene_update:
            predmet.ocjena=razred9_ocjene[i]
            predmet.save()
            i=i+1

        #----------------- UPDATE UCENIK PODATAKA --------------------------------#
        ucenik.ime=ime
        ucenik.prezime=prezime
          
        ucenik.osnovna_skola=osnovna_skola
        ucenik.save()
        if priznanja_naziv:
            ucenik_priznanja=Priznanja.objects.filter(ucenik_id=ucenik)
            if not ucenik_priznanja:#Ukoliko nema vec priznanja, ovdje se spremaju priznanja dodana na btn dodaj priznanja
                for i in range(len(priznanje_bodovi)):
                    naziv_priznanja=priznanja_naziv[i]
                    bodovi_priznanje=priznanje_bodovi[i]
                    priznanje=Priznanja(naziv_priznanja=naziv_priznanja,bodovi=bodovi_priznanje)
                    priznanje.save()
                    priznanje.ucenik_id.add(ucenik)

            else: #Ukoliko vec ima updatamo samo postojeca
                 i=0
                 for priznanje in ucenik_priznanja:
                        naziv=priznanja_naziv[i]
                        bodovi=priznanje_bodovi[i]
                        priznanje.naziv=naziv
                        priznanje.bodovi=bodovi
                        # priznanje.vrsta_takmicenja=tip
                        priznanje.save()
                        i=i+1


        return HttpResponseRedirect(reverse('tehnicka:dodajucenika'))