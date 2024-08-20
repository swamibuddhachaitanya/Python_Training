
# Django Framework
 
#### Create Project
    django-admin startproject my_project_rel_1
### Run the server
    python manage.py runserver
### Access admin page
    http://127.0.0.1:8000/admin

### Create Table
 #### prepare the schema
      python manage.py makemigrations
 #### Excecute schema in db
     python manage.py migrate

### admin page credentials
    python manage.py createsuperuser

###  welcome page
step-1. python manage.py startapp homeapp
step-2. add app name in settings.py INSTALLED_APPS
step-3. project-level/urls.py
step-4. app-level/urls.py

### Return html file
step-1. create folder called 'templates' inside 'homeapp'
step-2. return using 'render'

### URL MAPPING
For the URL: # http://127.0.0.1:8000/about
project-level-urls.py
       -- check are there any mapping 'about/'
       -- Mapping Not Found for 'about/'
       -- then
       -- check atleast are there any mapping for remaining
           part of the URL # http://127.0.0.1:8000/
       -- yes. Found mapped to "homeapp/urls.py"
       -- inside "homeapp/urls.py"
               check mapping for remaing part of the URL i.e 'about/'
       -- if found execute the function in views.py else throw error

### Create table
step-1. define the model in models.py
step-2. add entry in admin.py so that it will appear in admin page
Step-3: python manage.py makemigrations
Step-4: python manage.py migrate


### Interact with table
 ##### OPTION-1:
       Through admin page

 ##### OPTION-2: through DJango shell
        python manage.py shell
         Example:
            >> from loginapp.models import MyModel
            >> dir(MyModel)
            >> MyModel.objects
            >> dir(MyModel.objects)
            >> MyModel.objects.all()
            >> MyModel.objects.first()
            
            Get the data
            >> c = MyModel.objects.get(username='u1')
            >> c.username
            >> c.password
            >> c.email
            
            add new record
            >>> new_record = MyModel()
            >>> new_record.username = "u2"
            >>> new_record.password = "p2"
            >>> new_record.email = "u2@p2.com"
            >>> new_record.save()

