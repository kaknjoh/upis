from django.contrib import admin
from .models import Predmet,Ucenik,Predmet_Ocjena,Priznanja,Skola,Smjer,Kljucni_Predmeti,Razred,Takmicenje

# Register your models here.
admin.site.register(Predmet)
admin.site.register(Ucenik)
admin.site.register(Predmet_Ocjena)
admin.site.register(Priznanja)
admin.site.register(Skola)
admin.site.register(Smjer)
admin.site.register(Kljucni_Predmeti)
admin.site.register(Razred)
admin.site.register(Takmicenje)
admin.site.site_header = 'Upis ucenika'
admin.site.index_title = 'Tehnicka skola Zenica'
admin.site.site_title = 'Upis ucenika u skolu' 