# upis




Meni je ovako radilo. Nakon sto sam klonirao kreirao sam virtual enviroment: 
  
  python3 -m venv env
  
  source env/bin/activate - aktivirao je 
   
   
   U virutal env se instalira django 
   
   pip3 install django 
   
  Kada sam instalirao django nakon toga kad se navigiram u direktortij gdje se nalazi manage.py file kada pokrenem runama mi se program. 
  python manage.py runserver-
  
  Nakon toga bi trebalo da se kreira superuser:
  
  python manage.py createsuperuser

NAkon toga migracije 
python manage.py makemigrations 

Nakon toga:
python manage.py migrate
