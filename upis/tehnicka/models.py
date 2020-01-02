from django.db import models
import datetime
# Create your models here.


class Smjer(models.Model):
    naziv_smjera=models.CharField(max_length=60)
    
    class Meta:
        verbose_name_plural='Smjerovi'

    def __str__(self):
        return self.naziv_smjera

def current_year():
    return datetime.date.today().year

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

class Skola(models.Model):
    ime_skole=models.CharField(max_length=60)

    class Meta:
        verbose_name_plural='Skole'
    def __str__(self):
        return self.ime_skole
       

class Ucenik(models.Model): 
    ime=models.CharField(max_length=60)
    prezime=models.CharField(max_length=60)
    godina_upisa=models.IntegerField(default=current_year)
    smjer=models.ManyToManyField(Smjer)
    skola_id=models.ForeignKey(Skola, on_delete=models.CASCADE )

    class Meta:
        verbose_name_plural = "Učenici"

    def __str__(self):
        return  f"{self.ime} {self.prezime}" 

class Priznanja(models.Model):
    naziv_priznanja=models.CharField(max_length=40)
    bodovi=models.IntegerField(default='0')
    ucenik_id=models.ManyToManyField(Ucenik)
    class Meta:
        verbose_name_plural = "Priznanja"

    def __str__(self):
        return f"id:{self.id}:{self.naziv_priznanja}-{self.bodovi}"


class Predmet(models.Model):
    naziv_predmeta=models.CharField(max_length=60)
    
    #Prosljeduje se ManyToMany veza u novu tabelu Predmet_Ocjene
    ocjene_ucenika=models.ManyToManyField(Ucenik, through='Predmet_Ocjena')
    class Meta:
        verbose_name_plural = "Predmeti"

    def __str__(self):
        return f"{self.naziv_predmeta}"

class Predmet_Ocjena(models.Model):
    ucenik=models.ForeignKey(Ucenik, on_delete=models.CASCADE)
    predmet=models.ForeignKey(Predmet, on_delete=models.CASCADE)
    ocjena=models.IntegerField(default='0')
    razred=models.IntegerField(default='6')

    class Meta:
        verbose_name_plural = "Ocjene iz predmeta"

    def __str__(self):
        return f"{self.ucenik.ime}_{self.ucenik.prezime}_{self.predmet.naziv_predmeta}_{self.ocjena}_{self.razred}"

class Kljucni_Predmeti(models.Model):
    naziv_pr=models.CharField(max_length=40)
    smjer=models.ManyToManyField(Smjer)

class Razred(models.Model):
    naziv_razreda=models.CharField(max_length=50)
    broj_razreda=models.IntegerField(default='6')
    predmet=models.ManyToManyField(Predmet)
