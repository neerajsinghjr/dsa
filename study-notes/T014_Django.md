````
-------------------------------------------------------------------------------------
-> Title : Django Notes
-> Author : @neeraj-singh-jr
-> Status : Ongoing
-> Created : 09/10/2023
-> Updated : 20/03/2024
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q015 : Transaction Lock in Django;;
-> Q014 : Model Serializer vs HyperLinked Serializer;; 
-> Q013 : Combine multiple QuerySets in a View;;
-> Q012 : Permanent Redirection not a good options;;
-> Q011 : Mixins classes in Django;;
-> Q010 : File Based Session in Django;;
-> Q009 : Caching strategies supported by Django;;
-> Q008 : Middleware usage in Django;;
-> Q007 : Filer data using django models;;
-> Q006 : Signal and Dispatcher in Django;;
-> Q005 : Django OAuth2.0 Toollkit Flow;;
-> Q004 : Django Migration Workflow;;
-> Q003 : Django Path Function;;
-> Q002 : Djanog Core Architecture;;
-> Q001 : What is Django Serializer;;
-------------------------------------------------------------------------------------
````

### DJANGO NOTES : BEGINNING 

-------------------------------------------------------------------------------------
### Q015 : Transaction Lock in Django;;

In Django, the `transaction.atomic()` context manager is used to ensure that a block 
of database operations are executed within a single transaction. Transactions 
are important for maintaining data consistency and integrity, especially when dealing 
with multiple database operations that need to be executed together as a single unit.

#### WORK ARCHITECUTRE

`Atomicity`: By wrapping database operations inside transaction.atomic(), Django 
ensures that either all operations within the block are successfully committed 
to the database or none of them are. If an exception occurs during the execution 
of the block, Django automatically rolls back the transaction to its initial state, 
preventing any partial updates from being persisted in the database.

`Consistency`: Transactions help maintain data consistency by enforcing constraints 
and validations. For example, if you have a set of database operations that need to 
be executed together to maintain referential integrity or satisfy business rules, 
wrapping them inside a transaction ensures that these constraints are applied as a whole.

`Isolation`: Transactions provide isolation between concurrent database transactions, 
ensuring that the operations performed by one transaction are not visible to other 
transactions until the transaction is committed. This prevents data corruption and 
ensures that each transaction sees a consistent view of the database.

for eg,
````
from django.db import transaction

# Define a function that performs database operations within a transaction
def perform_database_operations():
    with transaction.atomic():
        # Perform database operations here
        # For example:
        # Create, update, or delete database records
        # Perform bulk inserts or updates
        # Execute complex database queries

# Call the function to execute database operations within a transaction
perform_database_operations()
````


-------------------------------------------------------------------------------------
### Q014 : Model Serializer vs HyperLinked Serializer;;

`Hyperlinked APIs` and `simple primary key (PK)` lookups often revolves around 
the design principles of REST and the requirements of the application

Here are the key reasons to consider using hyperlinked APIs instead of simple 
primary key lookups

#### Improved Readability and User Experience:
- Hyperlinked APIs use URLs that are more human-readable and descriptive.
- URLs based on resource relationships (hyperlinks) provide context about the 
relationship between different resources.

#### Consistency and Predictability:
- Hyperlinked APIs provide consistent URLs for related resources, making it easier 
for developers to predict and understand the structure of the API.
- Simple PK lookups may expose internal database details and may not be as 
consistent or predictable.

#### Loose Coupling:
- Hyperlinked APIs promote loose coupling between the client and the server. Clients 
can navigate through the API based on hyperlinks without depending on the internal
implementation details.
- Simple PK lookups may tightly couple clients to the structure of the server's database.

for eg,

> Simple Primary Key Lookups:
````
# serializers.py
from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# views.py
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'  # Using simple primary key lookup

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'  # Using simple primary key lookup
    
# NOTE :
In this approach, to get details about an author or a book, the client needs 
to construct URLs like /api/authors/1/ or /api/books/2/.
````

> Hyperlinked APIs:

````
# serializers.py
from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# views.py
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

NOTE:
In this hyperlinked approach, the serializers use HyperlinkedModelSerializer, 
and clients can navigate the API using hyperlinks. For example, the client can 
follow links from an author's details to the books they have written and vice versa.
````


-------------------------------------------------------------------------------------
### Q013 : Combine multiple QuerySets in a View;;

QuerySets can be combined into another QuerySet, and they do not have to be from 
the same model.

To merge QuerySets from the same model, use the `Python union operator`.

The `union operator` can be used to combine two or more QuerySets with the 
following syntax: 

> model_combination = model_set1 | model_set2 | model_set3 

Additionally, you can concatenate two or more QuerySets from other models by using 
the `chain()` method from the Itertools package. 

````
from itertools import chain

model_combination = list(chain(model_set1, model_set2))
````

As an alternative, you can merge two or more QuerySets from other models using 
`union()`, `passing all=TRUE` to allow for duplication.

> model_combination = model_set1.union(model_set2, all=TRUE) 


-------------------------------------------------------------------------------------
### Q012 : Permanent Redirection not a good options;;

Permanent redirection is only employed if it does not require visitors to be 
directed to the old URLs. The browser caches the response of permanent redirections, 
thus attempting to redirect to somewhere different will cause problems. 

Because this is a `browser-side process`, if your user navigates to a different page, 
it will load the same page.


-------------------------------------------------------------------------------------
### Q011: Mixins classes in Django;;

In Django, a mixin is a Python class that is inherited by another class to carry 
out extra functions. Classes that can be reused and scaled are mixins. A unique 
form of multiple inheritances is a mixin.

Mixins are typically employed in two contexts:
- You wish to give a class several optional features.
- You wish to apply a specific feature to numerous classes.


-------------------------------------------------------------------------------------
### Q010 : File Based Session in Django;;


-------------------------------------------------------------------------------------
### Q009 : Caching strategies supported by Django;;


-------------------------------------------------------------------------------------
### Q008 : Middleware usage in Django;;


-------------------------------------------------------------------------------------
### Q007 : Filer data using django models;;


-------------------------------------------------------------------------------------
### Q006 : Signal and Dispatcher in Django;;


-------------------------------------------------------------------------------------
### Q005 : Django OAuth2.0 Toollkit Flow;;


-------------------------------------------------------------------------------------
### Q004 : Django Migration Workflow;;

Database engine are library which lets your project connect to any database client.

- sqlite3 :'django.db.backends.sqlite3' ~ default 
- postgres : 'django.db.backends.postgresql',
- msql : 'django.db.backends.mysql'
- oracle : 'django.db.backends.oracle'

#### Default apps

- django.contrib.admin – The admin site. You’ll use it shortly.
- django.contrib.auth – An authentication system.
- django.contrib.contenttypes – A framework for content types.
- django.contrib.sessions – A session framework.
- django.contrib.messages – A messaging framework.
- django.contrib.staticfiles – A framework for managing static files.

NOTE : We have to migrate the table for these default apps

`$ python manage.py migrate`

The migrate command looks at the INSTALLED_APPS setting and creates any necessary 
database tables according to the database settings in your `mysite/settings.py`
file and the database migrations shipped with the app.

#### Creating Model

````
# from mysite/polls/models.py

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
````


-------------------------------------------------------------------------------------
### Q003 : Django Path Function;;

The path() function is passed four arguments, two required: 
- route
- view
- kwargs, 
- name

#### path() argument: route

route is a string that contains a URL pattern. When processing a request, Django
starts at the first pattern in urlpatterns and makes its way down the list,
comparing the requested URL against each pattern until it finds one that
matches.

for eg, Patterns don’t search GET and POST parameters, or the domain name. For
example, in a request to https://www.example.com/myapp/


#### path() argument: view

When Django finds a matching pattern, it calls the specified view function with
an HttpRequest object as the first argument and any “captured” values from the
route as keyword arguments. We’ll give an example of this in a bit.


#### path() argument: kwargs

Arbitrary keyword arguments can be passed in a dictionary to the target view.

#### path() argument: name

Naming your URL lets you refer to it unambiguously from elsewhere in Django,
especially from within templates. This powerful feature allows you to make
global changes to the URL patterns of your project while only touching a single
file.


-------------------------------------------------------------------------------------
### Q002 : Djanog Core Architecture;;

#### Setup Django Model and Migration

````
# main django model for core
from django.db import models

# reporter model and fields 
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

# article model and fields
class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

Now from the shell, create and trigger the migration
$ python manage.py makemigrations

then migrate
$ python manage migrate
````

#### Django Test Migration from Shell

````
# Import the models we created from our "news" app
>>> from news.models import Article, Reporter

# No reporters are in the system yet.
>>> Reporter.objects.all()
<QuerySet []>

# Create a new Reporter.
>>> r = Reporter(full_name="John Smith")

# Save the object into the database. You have to call save() explicitly.
>>> r.save()

# Now it has an ID.
>>> r.id
1

Reporter.objects.get(id=1)
<Reporter: John Smith>

>>> Reporter.objects.get(full_name__startswith="John")
<Reporter: John Smith>

>>> Reporter.objects.get(full_name__contains="mith")
<Reporter: John Smith>
````

#### Register the created model with Admin Portal 

````
//--- from admin.py file

from django.contrib import admin
from . import models

admin.site.register(models.Reporter)
admin.site.register(models.Article)
````

````
//--- from urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<int:pk>/", views.article_detail),
]
````

````
//--- from views.py

from django.shortcuts import render
from .models import Article


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "news/year_archive.html", context)
````

````
//--- from templates

{% extends "base.html" %}

{% block title %}Articles for {{ year }}{% endblock %}

{% block content %}
<h1>Articles for {{ year }}</h1>

{% for article in article_list %}
    <p>{{ article.headline }}</p>
    <p>By {{ article.reporter.full_name }}</p>
    <p>Published {{ article.pub_date|date:"F j, Y" }}</p>
{% endfor %}
{% endblock %}
````


-------------------------------------------------------------------------------------
### Q001 : Django Framwork Getting Started;;

Django was developed in a fast-paced newsroom environment, it was designed to
make common web development tasks fast and easy.

#### check django version;;

`$ python -m django --version`

#### creating a project;;

`$ django-admin startproject mysite`

````
# project directory will look like this,
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
````

#### Directory Description: 

-  The outer mysite/ root directory is a container for your project. Its name
   doesn’t matter to Django; you can rename it to anything you like.

-  manage.py: A command-line utility that lets you interact with this Django
   project in various ways. You can read all the details about manage.py in
   django-admin and manage.py.

-  The inner mysite/ directory is the actual Python package for your project.
   Its name is the Python package name you’ll need to use to import anything
   inside it (e.g. mysite.urls).

-  mysite/__init__.py: An empty file that tells Python that this directory
   should be considered a Python package. If you’re a Python beginner, read
   more about packages in the official Python docs.

-  mysite/settings.py: Settings/configuration for this Django project. Django
   settings will tell you all about how settings work.

-  mysite/urls.py: The URL declarations for this Django project; a “table of
   contents” of your Django-powered site. You can read more about URLs in URL
   dispatcher.

-  mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your
   project. See How to deploy with ASGI for more details.

-  mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your
   project. See How to deploy with WSGI for more details.

### Django Run-Time Environment;;

`$ python manage.py runserver`

or, if you want to change the port
`$ python manage.py runserver 8080`

or, if you want to change the ip
`$ $ python manage.py runserver 0.0.0.0:8000`


-------------------------------------------------------------------------------------