
  
from django.urls import path

from django.urls import path
from . import views
# we could say: from application import views as application_view and use it as application_view.details

app_name = 'tehnicka'
urlpatterns = [
    
    path("add-student/", views.dodajucenika, name='dodajucenika'),
   
]
