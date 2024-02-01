"""
added welcome message
"""

# ----------
# Create App for our website
############
import flask
# my_website_app = flask.Flask("MyApp")
my_website_app = flask.Flask(__name__)
######################


# ----------
# END POINT - 1: URL http://127.0.0.1:5000/ MAPPED to route("/")
############
@my_website_app.route("/")
def my_index_page():
    return "WEL COME"
######################


# ----------
# Run builtin server
############
my_website_app.run(debug=True)
# my_website_app.run(host='127.0.0.1', port=1234)
######################