# upis



Markup:
* Meni je ovako radilo. Nakon sto sam klonirao kreirao sam virtual enviroment: 

   python3 -m venv env
   source env/bin/activate - aktivirao je 
   
   
* U virutal env se instalira django  

   pip3 install django 
   
* Prije pokretanja potrebno je intstalirati biblioteku: 

    pip install xhtml2pdf
   
* Kada sam instalirao django nakon toga kad se navigiram u direktortij gdje se nalazi manage.py file kada pokrenem runama mi se program.

  python manage.py runserver-
  
* Nakon toga bi trebalo da se kreira superuser:

  python manage.py createsuperuser

* Nakon toga pokrenuti migracije ali potrebno je specifirati app

  python manage.py makemigrations tehnicka

* Nakon toga:

python manage.py migrate tehnicka nakon toga ponovo python manage.py migrate da se dodaju migracije za usera i superusera

* Nakon toga za upis u bazu testnih podataka potrebno je navigirati se na /tscze/popuni
