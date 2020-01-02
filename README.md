# upis

	sudo apt install python3-venv python3-pip
  
  
  python3 -m pip install --user --upgrade pip
  
  
  python3 -m venv envir
  
   source env/bin/activate
   
   
   U virutal env se instalira django 
   
   pip3 install django 
   
  Pokretanjem trebalo bi da se pokrene django app 
  django-admin manage.py runserver
  
  Nakon toga bi trebalo da se kreira superuser:
  
  python manage.py createsuperuser

NAkon toga migracije 
python manage.py makemigrations 

Nakon toga:
python manage.py migrate
