from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import  Predmet,Ucenik,Predmet_Ocjena,Priznanja,Skola,Smjer,Kljucni_Predmeti
from django.db import transaction
from django.urls import reverse

# Popunjavanje defaultnih smjerova
def dodajSmjerove(request):
    smjer1=Smjer(naziv_smjera="Racunarska tehnika i automatika")
    smjer1.save()
    smjer2=Smjer(naziv_smjera="Elektronicar")
    smjer2.save()
    smjer3=Smjer(naziv_smjera="Masinski tehnicar")
    smjer3.save()
    smjer4=Smjer(naziv_smjera="Tehnicar drumskog saobracaja")
    smjer4.save()
    smjer5=Smjer(naziv_smjera="Arhitektonski tehnicar")
    smjer5.save()
    smjer6=Smjer(naziv_smjera="Geodezija")
    smjer6.save()

#Dodavanje kljucnih predmeta po smjerovima
def dodajKljucnePredmete(request):
    kljucni_predmet__1=Kljucni_Predmeti(naziv_pr="Matematika")
    kljucni_predmet__1.save()
    smjer_aut=Smjer.objects.get(naziv_smjera="Racunarska tehnika i automatika")
    smjer_ele=Smjer.objects.get(naziv_smjera="Elektronicar")
    smjer_masinski=Smjer.objects.get(naziv_smjera="Masinski tehnicar")
    smjer_saobracaj=Smjer.objects.get(naziv_smjera="Tehnicar drumskog saobracaja")
    smjer_arhitektura=Smjer.objects.get(naziv_smjera="Arhitektonski tehnicar")
    smjer_geodezija=Smjer.objects.get(naziv_smjera="Geodezija")

    

    kljucni_predmet__1.smjer.add(smjer_aut)
    kljucni_predmet__1.smjer.add(smjer_ele)
    kljucni_predmet__1.smjer.add(smjer_masinski)
    kljucni_predmet__1.smjer.add(smjer_saobracaj)
    kljucni_predmet__1.smjer.add(smjer_arhitektura)
    kljucni_predmet__1.smjer.add(smjer_geodezija)



    kljucni_predmet__2=Kljucni_Predmeti(naziv_pr="Fizika")
    kljucni_predmet__2.save()
    kljucni_predmet__2.smjer.add(smjer_aut)
    kljucni_predmet__2.smjer.add(smjer_ele)
    kljucni_predmet__2.smjer.add(smjer_masinski)
    kljucni_predmet__2.smjer.add(smjer_saobracaj)
    kljucni_predmet__2.smjer.add(smjer_arhitektura)
    kljucni_predmet__2.smjer.add(smjer_geodezija)

    kljucni_predmet__3=Kljucni_Predmeti(naziv_pr="Informatika")
    kljucni_predmet__3.save()
    kljucni_predmet__3.smjer.add(smjer_aut)
    kljucni_predmet__3.smjer.add(smjer_ele)
    kljucni_predmet__3.smjer.add(smjer_arhitektura)

    kljucni_predmet__4=Kljucni_Predmeti(naziv_pr="Tehnicka kultura")
    kljucni_predmet__4.save()
    kljucni_predmet__4.smjer.add(smjer_masinski)

    kljucni_predmet__5=Kljucni_Predmeti(naziv_pr="Geografija")
    kljucni_predmet__5.save()
    kljucni_predmet__5.smjer.add(smjer_saobracaj)
    kljucni_predmet__5.smjer.add(smjer_geodezija)


    

#Testni predmeti

def dodajPredmete(request):
    #Dodavanje razreda kako bi se mogli povezati predmeti koji pripadaju odredenom razredu radi lakseg izvlacenja querija

        razred6=Razred(naziv_razreda="Sesti razred",broj_razreda=6)
        razred6.save()
        razred7=Razred(naziv_razreda="Sedmi razred",broj_razreda=7)
        razred7.save()
        razred8=Razred(naziv_razreda="Osmi razred",broj_razreda=8)
        razred8.save()
        razred9=Razred(naziv_razreda="Deveti razred",broj_razreda=9)
        razred9.save()


        predmet1=Predmet(naziv_predmeta="Matematika")
        predmet1.save()
        predmet2=Predmet(naziv_predmeta="Fizika")
        predmet2.save()
        predmet3=Predmet(naziv_predmeta="Informatika")
        predmet3.save()
        predmet4=Predmet(naziv_predmeta="Tehnicka kultura")
        predmet4.save()
        predmet5=Predmet(naziv_predmeta="Geografija")
        predmet5.save()
        predmet6=Predmet(naziv_predmeta="Tjelesni i zdravstveni odgoj")
        predmet6.save()

        #Dodavanje predmeta za odredeni razred
        razred6.predmet.add(predmet1)
        razred6.predmet.add(predmet3)
        razred6.predmet.add(predmet4)
        razred6.predmet.add(predmet5)
        razred6.predmet.add(predmet6)

        razred7.predmet.add(predmet1)
        razred7.predmet.add(predmet3)
        razred7.predmet.add(predmet4)
        razred7.predmet.add(predmet5)
        razred7.predmet.add(predmet6)

        razred8.predmet.add(predmet1)
        razred8.predmet.add(predmet2)
        razred8.predmet.add(predmet6)

        razred9.predmet.add(predmet1)
        razred9.predmet.add(predmet2)
        razred9.predmet.add(predmet6)
#Dodane skole za testiranja
def dodajSkole(request):
        skola1=Skola(ime_skole="Aleksa Santic")
        skola1.save()
        skola2=Skola(ime_skole="Mak Dizdar")
        skola2.save()
        skola3=Skola(ime_skole="Musa cazim Catic")
        skola3.save()
        skola4=Skola(ime_skole="Alija Nametak")
        skola4.save()



    
