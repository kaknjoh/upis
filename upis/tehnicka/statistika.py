from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import  Predmet,Ucenik,Predmet_Ocjena,Priznanja,Skola,Smjer,Kljucni_Predmeti
from django.db import transaction
from django.urls import reverse

import sys
import logging

def racunajStatistiku(request, smjer_id, message):

    logger = logging.getLogger(__name__)

    # Put the logging info within your django view
    logger.info("Simple info")
    posebni_bodovi={}
    prosjek_6=0
    prosjek_7=0
    prosjek_8=0
    prosjek_9=0

    prosjek6_dict={}
    prosjek7_dict={}
    prosjek8_dict={}
    prosjek9_dict={}
    prosjek_ukupno_dict={}


    posebni_predmet_1_razred8_dict={} 
    posebni_predmet_1_razred9_dict={}
    posebni_predmet_2_razred8_dict={}
    posebni_predmet_2_razred9_dict={}
    posebni_predmet_3_razred6_dict={}
    posebni_predmet_3_razred7_dict={}

    posebni_predmeti_ukupno_dict={}

    ukupno_dict={}
  

    


    # Potrebno za dobivanje smjera koji je ucenik izabrao

    smjer=Smjer.objects.get(id=smjer_id)
    #Dohvatanje ucenika, ucenici su sleektovani po smjeru koji su odabrali
        #----------------SUME OCJENA I BROJACI PREDMETA ---------------------------#
    s=0
    brP=1
    s1=0
    brP1=1
    s2=0
    brP2=1
    s3=0
    brP3=1

    posebni_predmet_1_razred8=0
    posebni_predmet_1_razred9=0
    posebni_predmet_2_razred8=0
    posebni_predmet_2_razred9=0
    posebni_predmet_3_razred6=0
    posebni_predmet_3_razred7=0

    
    for ucenik in Ucenik.objects.filter(smjer_id=smjer):
        


        #For petlje za izracun sume ocjene za svaki razred
        for razred in Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=6):
            s=s+razred.ocjena
            brP=brP+1

        for razred in Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=7):
            s1=s1+razred.ocjena
            brP1=brP1+1

        for razred in Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=8):
            s2=s2+razred.ocjena
            brP2=brP2+1

        for razred in Predmet_Ocjena.objects.filter(ucenik=ucenik,razred=9):
            s3=s3+razred.ocjena
            brP3=brP3+1


        
        for predmet1 in Kljucni_Predmeti.objects.filter(smjer=smjer):
            predmet=Predmet.objects.get(naziv_predmeta=predmet1.naziv_pr)
            if(predmet1.naziv_pr=='Matematika'):
                ocjena=Predmet_Ocjena.objects.get(ucenik=ucenik,predmet=predmet,razred=9)
                posebni_predmet_1_razred9=ocjena.ocjena
                ocjena=Predmet_Ocjena.objects.get(ucenik=ucenik,predmet=predmet,razred=8)
                posebni_predmet_1_razred8=ocjena.ocjena


                

                #------ NE MOZE OVAKO DOBIJE SE QUERY SET NE OCJENA --------#
                #posebni_predmet_1_razred8=Predmet_Ocjena.objects.filter(ucenik=ucenik,predmet=predmet,razred=8)
                #posebni_predmet_1_razred9=Predmet_Ocjena.objects.filter(ucenik=ucenik,predmet=predmet,razred=9)

            elif(predmet1.naziv_pr=='Fizika'):
                ocjena=Predmet_Ocjena.objects.get(ucenik=ucenik,predmet=predmet,razred=9)
                posebni_predmet_2_razred9=ocjena.ocjena
                ocjena=Predmet_Ocjena.objects.get(ucenik=ucenik,predmet=predmet,razred=8)
                posebni_predmet_2_razred8=ocjena.ocjena

            elif(predmet1.naziv_pr=='Informatika'):
                ocjena=Predmet_Ocjena.objects.get(ucenik=ucenik,predmet=predmet,razred=6)
                posebni_predmet_3_razred6=ocjena.ocjena
                ocjena=Predmet_Ocjena.objects.get(ucenik=ucenik,predmet=predmet,razred=7)
                posebni_predmet_3_razred7=ocjena.ocjena

            elif(predmet1.naziv_pr=='Geografija'):
               ocjena=Predmet_Ocjena.objects.get(ucenik=ucenik,predmet=predmet,razred=6)
               posebni_predmet_3_razred6=ocjena.ocjena
               ocjena=Predmet_Ocjena.objects.get(ucenik=ucenik,predmet=predmet,razred=7)
               posebni_predmet_3_razred7=ocjena.ocjena

            elif(predmet1.naziv_pr=='Tehnicka kultura'):
               ocjena=Predmet_Ocjena.objects.get(ucenik=ucenik,predmet=predmet,razred=6)
               posebni_predmet_3_razred6=ocjena.ocjena
               ocjena=Predmet_Ocjena.objects.get(ucenik=ucenik,predmet=predmet,razred=7)
               posebni_predmet_3_razred7=ocjena.ocjena
                    
        prosjek6_dict[ucenik.id]=round(s/brP,2)
        prosjek7_dict[ucenik.id]=round(s1/brP1,2)
        prosjek8_dict[ucenik.id]=round(s2/brP2,2)
        prosjek9_dict[ucenik.id]=round(s3/brP3,2)
        prosjek_ukupno_dict[ucenik.id]=round(s/brP+s1/brP1+s2/brP2+s3/brP3,2)
        

        #Posebni predmeti po uceniku
        posebni_predmet_1_razred9_dict[ucenik.id]=posebni_predmet_1_razred9
        posebni_predmet_1_razred8_dict[ucenik.id]=posebni_predmet_1_razred8
        posebni_predmet_2_razred9_dict[ucenik.id]=posebni_predmet_2_razred9
        posebni_predmet_2_razred8_dict[ucenik.id]=posebni_predmet_2_razred8
        posebni_predmet_3_razred7_dict[ucenik.id]=posebni_predmet_3_razred7
        posebni_predmet_3_razred6_dict[ucenik.id]=posebni_predmet_3_razred6

        posebni_predmeti_ukupno_dict[ucenik.id]=round(posebni_predmet_1_razred9+posebni_predmet_1_razred8+posebni_predmet_2_razred9+posebni_predmet_2_razred8+posebni_predmet_3_razred7+posebni_predmet_3_razred6,2)


        ukupno_dict[ucenik.id]=round(posebni_predmeti_ukupno_dict[ucenik.id]+prosjek_ukupno_dict[ucenik.id],2)

    context={
    'ucenici':Ucenik.objects.filter(smjer_id=smjer),     # 'smjerovi':Smjer.objects.all(),
    'kljucni_predmeti':Kljucni_Predmeti.objects.filter(smjer=smjer),

    'prosjek_6':prosjek6_dict,
    'prosjek_7':prosjek7_dict,
    'prosjek_8':prosjek8_dict,
    'prosjek_9':prosjek9_dict,

    'prosjek_ukupno':prosjek_ukupno_dict, # mnozi se sa 3

    'posebni_predmet_1_ocjena_razred8':posebni_predmet_1_razred8_dict,
    'posebni_predmet_1_ocjena_razred9':posebni_predmet_1_razred9_dict,
    'posebni_predmet_2_ocjena_razred8':posebni_predmet_2_razred8_dict,
    'posebni_predmet_2_ocjena_razred9':posebni_predmet_2_razred9_dict,
    'posebni_predmet_3_ocjena_razred6':posebni_predmet_3_razred6_dict,
    'posebni_predmet_3_ocjena_razred7':posebni_predmet_3_razred7_dict,

    'posebni_predmet_ukupno':posebni_predmeti_ukupno_dict,
     
    'ukupno':ukupno_dict,

    'message':message
            
     }
    return render(request,'tehnicka/index.html',context)