
  
from django.urls import path

from django.urls import path
from . import views
# we could say: from application import views as application_view and use it as application_view.details

app_name = 'tehnicka'
urlpatterns = [
    path("",views.index_base,name="index_base"),
    path("add-student/", views.dodajucenika, name='dodajucenika'),
    path("smjer/<int:smjer_id>", views.index, name='index'),
    path("details/<int:ucenik_id>", views.details, name='details'),
    path("delete/<int:ucenik_id>", views.delete, name='delete'),
   # path("pdf/example/",views.print_pdf,name='pdf'),
    path("pdf/<int:smjer_id>",views.get_pdf,name='get_pdf'),
   
]