"""
Python for web development

We have many web development frameworks in python
- bottle framework
- flask framework # POPULAR # Micro Framework
- django framework  # POPULAR # MVT (Model View Template) Framework
- web2py framework
- pyramid framework
- falcon framework
- fastapi framework
Many More...
"""

"""
Using flask,
1) we can develop websites
2) we can develop RESTFul web services like REST-API and Micro Services
"""

"""
Here,
We will discuss on how to use flask for developing websites
"""

"""
For any web application, we need 3 things
1) web server # flask has builtin web server which can be used for development purpose only
2) database # SQLite
3) browser

List of web servers
https://wsgi.readthedocs.io/en/latest/servers.html
"""


# ----------
# Create App for our website
############
import flask
# my_website_app = flask.Flask("MyApp")
my_website_app = flask.Flask(__name__)
######################


# EMPTY WEBSITE, No Pages Created Yet

# ----------
# Run builtin server
############
my_website_app.run(debug=True)
# my_website_app.run(host='127.0.0.1', port=1234)
######################


