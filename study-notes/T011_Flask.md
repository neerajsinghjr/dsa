````
-------------------------------------------------------------------------------------
-> Title : Flask Notes
-> Author : @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 12/06/2023
-> Updated : 23/02/2024
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q004 : Flask HTTP Methods;;
-> Q003 : Flask URL Building;;
-> Q002 : Flask App Routing;;
-> Q001 : Introduction to Flask;;
-------------------------------------------------------------------------------------
````

### FLASK NOTES : BEGINNING

-------------------------------------------------------------------------------------
### Q004 : Flask HTTP Methods;;

There are different types of Method 

1) `GET` : It is the most common method which can be used to send data in the 
unencrypted form to the server.
2) `HEAD` : It is similar to the GET but used without the response body.
3) `POST` : It is used to send the form data to the server. The server does not 
cache the data transmitted using the post method.
4) `PUT` : It is used to replace all the current representation of the target 
resource with the uploaded content.
5) `PATCH` : The PATCH HTTP method is used to modify the values of the resource 
properties. The PATCH HTTP method requires a request body. 
6) `DELETE` : It is used to delete all the current representation of the target 
resource specified in the URL.


-------------------------------------------------------------------------------------
### Q003 : Flask URL Building;;

The `url_for()` function is used to build a URL to the specific function dynamically. 
The first argument is the name of the specified function, and then we can pass any 
number of keyword argument corresponding to the variable part of the URL.

for eg,
````
````




-------------------------------------------------------------------------------------
### Q002 : Flask App Routing;;

App routing is used to map the specific URL with the associated function that is 
intended to perform some task. It is used to access some particular page like Flask 
Tutorial in the web application.

#### Flask : Basic Routing 

The following converters are used to convert the default string type to the associated 
data type...

- `string` : default
- `int` : used to convert the string to the integer
- `float` : used to convert the string to the float.
- `path` : It can accept the slashes given in the URL.

for eg,
````
from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home/<int:age>')  
def home(age):  
    return "Age = %d"%age;  
  
if __name__ =="__main__":  
    app.run(debug = True)
````

#### Flask : Add Routing

There is one more approach to perform routing for the flask web application that can 
be done by using the `add_url()` function of the Flask class. 

> Syntax: add_url_rule(url-rule, url-endpoint, view-function)

for eg,
````
from flask import Flask

# app initialization;;
app = Flask(__name__)  
  
def about():
    return "TEST PAGE";  
  
app.add_url_rule("/about", "about", about)  
  
if __name__ =="__main__":  
    app.run(debug = True)  
````


-------------------------------------------------------------------------------------
### Q001 : Introduction to Flask;;

`Flask` is a web framework that provides libraries to build lightweight web applications 
in python. It is developed by Armin Ronacher who leads an international group of python 
enthusiasts (POCCO).

`WSGI` is an acronym for web server gateway interface which is a standard for python 
web application development. It is considered as the specification for the universal 
interface between the web server and web application.

`Jinja2` is a web template engine which combines a template with a certain data 
source to render the dynamic web pages.


#### Flask : Setup Virtual Environment 

Step 1 : `$ pip install virtualenv`

Step 2 : `$ mkdir new`

Step 3 : `$ cd project`

Step 4 : `$ virtualenv env`

Step 5 : `$ venv/bin/activate`

Step 6 : `$ venv\scripts\activate`

Step 7 : `$ pip install flask`


#### Flask : Flask Application

Build the python web application, we need to import the Flask module. An object of 
the Flask class is considered as the WSGI application.

We need to pass the name of the current module, i.e. `__name__` as the argument into 
the Flask constructor.

The `route()` function of the Flask class defines the URL mapping of the associated 
function. 

> Syntax: app.route(rule, options)  

It accepts the following parameters.

- `rule` : It represents the URL binding with the function.
- `options` : It represents the list of parameters to be associated with the rule object

The `/ URL` is bound to the main function which is responsible for returning the 
server response. It can return a string to be printed on the browser's window or 
we can use the HTML template to return the HTML file as a response from the server.

eg,
````
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "HOME PAGE"

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 5050
    debug = True
    app.run(
        host=ip,
        port=port,
        debug=True
    )

````


-------------------------------------------------------------------------------------