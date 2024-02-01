"""
added register.html
"""

# ----------
# Where to keep html files?
############
# - create a directory 'templates' inside 'website' folder
# - keep all html files inside 'templates'
######################

# ----------
# Create App for our website
############
import flask
# my_website_app = flask.Flask("MyApp")
my_website_app = flask.Flask(__name__)
######################


# # ----------
# # END POINT - 1: URL http://127.0.0.1:5000/ MAPPED to route("/")
# ############
# @my_website_app.route("/")
# def my_index_page():
#     return "WEL COME"
# ######################


# ----------
# END POINT - 1: URL http://127.0.0.1:5000/ MAPPED to route("/")
############
@my_website_app.route("/")
def my_index_page():
    return flask.render_template("index.html")
######################


# ----------
# END POINT - 2: URL http://127.0.0.1:5000/about MAPPED to route("/about")
############
@my_website_app.route("/about")
def my_about_page():
    return flask.render_template("about.html")
######################


# ----------
# END POINT - 3: URL http://127.0.0.1:5000/login MAPPED to route("/login")
############
@my_website_app.route("/login")
def my_login_page():
    return flask.render_template("login.html")
######################


# ----------
# END POINT - 4: URL http://127.0.0.1:5000/register MAPPED to route("/register")
############
@my_website_app.route("/register")
def my_register_page():
    return flask.render_template("register.html")
######################

# ----------
# Run builtin server
############
my_website_app.run(debug=True)
# my_website_app.run(host='127.0.0.1', port=1234)
######################

