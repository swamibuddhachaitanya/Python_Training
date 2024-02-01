"""
Integrated SQLAlchemy
"""


# ----------
# Create App for our website
############
import flask
from flask_sqlalchemy import SQLAlchemy
# SQLAlchemy : For ORM

from flask_marshmallow import Marshmallow
# Marshmallow: For Serialization & Deserialization

from flask import Flask

my_website_app = Flask(__name__)

my_website_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_alchemy_users_db.sqlite3"

db = SQLAlchemy(my_website_app)
ma = Marshmallow(my_website_app)

# Define the model
class MyTable(db.Model):
    user_name = db.Column(db.String(100), primary_key=True)
    user_password = db.Column(db.String(100))
    user_email = db.Column(db.String(100))

# Which column we need to serialize
class MyAppSchema(ma.Schema):
    class Meta:
        fields = ('user_name', 'user_password', 'user_email')

my_website_app_schema = MyAppSchema(many=True)

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
    return flask.render_template("newindex.html")
######################


# ----------
# END POINT - 2: URL http://127.0.0.1:5000/about MAPPED to route("/about")
############
@my_website_app.route("/about")
def my_about_page():
    return flask.render_template("newabout.html")
######################


# ----------
# END POINT - 3: URL http://127.0.0.1:5000/login MAPPED to route("/login")
############
@my_website_app.route("/login")
def my_login_page():
    return flask.render_template("newlogin.html")
######################


# ----------
# END POINT - 4: URL http://127.0.0.1:5000/register MAPPED to route("/register")
############
@my_website_app.route("/register")
def my_register_page():
    return flask.render_template("newregister.html")
######################


# ----------
# END POINT - 5: URL http://127.0.0.1:5000/addnewuser MAPPED to route("/addnewuser")
############
@my_website_app.route("/addnewuser", methods=["POST"])
def my_addnewuser_page():
    """
    Our Plan:
    Task-1: Get new user details
    Task-2: verify whether both the passwords are matching
    Task-3: Create database and table
    Task-4: verify whether user already exists
    Task-5: add new user to db
    """
    # -----------
    # Task-1: Get new user details
    # -----------
    # flask will keep all form data in a dictionary
    # flask.request.form = {uname: entered_username, pw1: entered_password}
    entered_username = flask.request.form.get("uname")
    entered_password_1 = flask.request.form.get("pw1")
    entered_password_2 = flask.request.form.get("pw2")
    entered_email = flask.request.form.get("email")
    ######################

    # -----------
    # Task-2: verify whether both the passwords are matching
    # -----------
    if entered_password_1 != entered_password_2:
        return "Both the passwords should match.<br><a href='/register'>Go Back</a>"
    ######################

        # -----------
    # Task-4: verify whether user already exists
    # -----------
    # get_entry = my_website_app.query.get_or_404(entered_username)
    get_entry = MyTable.query.get(entered_username)

    if get_entry:
        return "User already exist.<br><a href='/register'>Go Back</a>"
    else:
        new_entry = MyTable(user_name=entered_username, user_password= entered_password_1, user_email=entered_email)
        db.session.add(new_entry)
        db.session.commit()
        return "Account Created.<br><a href='/register'>Go Back</a>"
    ######################
######################

# ----------
# END POINT - 6: URL http://127.0.0.1:5000/validatelogin MAPPED to route("/validatelogin")
############
@my_website_app.route("/validatelogin", methods=["POST"])
def my_validatelogin_page():
    """
    Our Plan:
    Task-1: Get entered username and password
    Task-2: Validate with db and return success or failure
    """
    # ----------
    # Task-1: Get entered username and password
    ############
    entered_username = flask.request.form.get("uname")
    entered_password = flask.request.form.get("pw")
    ######################

    # ----------
    # Task-2: Validate with db and return success or failure
    ############
    import sqlite3
    my_db_connection = sqlite3.connect("my_users_db.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_query = f"SELECT COUNT(*) FROM MY_USERS_TABLE WHERE USERNAME = '{entered_username}' AND PASSWORD = '{entered_password}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchone() # Example: (10, )
    user_count = my_db_result[0] # Example 10
    if user_count > 0:
        my_log_db_connection = sqlite3.connect("my_data_db.sqlite3")
        my_log_db_cursor = my_log_db_connection.cursor()
        my_log_db_cursor.execute("SELECT * FROM MY_DATA_TABLE")
        my_log_db_result = my_log_db_cursor.fetchall()
        image_folder_path = 'static'
        # image_file_path = 'sub-folder/mygraph.png'
        image_file_path = "mygraph.png"
        return flask.render_template("newlogreport.html", my_db_data = {"my_log_db_result": my_log_db_result, "image_folder_path": image_folder_path, "image_file_path": image_file_path})
    else:
        return "Login Failed.<br><a href='/login'>Go Back</a>"
    ######################
# ----------
# Python code inside html file
############
# - We can write python code inside html using below syntax
#
# - {% any python statement %} # Use this syntax to write any python statement

# - {% if some_condn %} # Use this syntax to write any block
#   {% endif  %}
#
# - {{ python_variable }} # Use this syntax to print any python variable
#
# - python code present inside html will be executed by the program
#   called TEMPLATE ENGINE
#
# - name of the TEMPLATE ENGINE used in flask is JINJA2
######################


# ----------
# END POINT - 7: URL http://127.0.0.1:5000/weatherapi MAPPED to route("/weatherapi")
############
@my_website_app.route("/weatherapi", methods=["GET"])
def my_weatherapi_page():
    return flask.render_template("newweatherapi.html")
######################


# ----------
# END POINT - 8: URL http://127.0.0.1:5000/weatherreport MAPPED to route("/weatherreport")
############
@my_website_app.route("/weatherreport", methods=["POST"])
def my_weatherreport_page():
    """
    Our Plan:
    Task-1: Get entered city name
    Task-2: prepare final end point url
    Task-3: Access API and display
    """

    # ----------
    # Task-1: Get entered city name
    ############
    city_name = flask.request.form.get("city")
    ######################

    # ----------
    # Task-2: prepare final end point url
    ############
    final_api_endpoint = f"https://demoqa.com/utilities/weather/city/{city_name}"
    ######################

    # ----------
    # Task-3: Access API and display
    ############
    import requests
    api_response = requests.get(final_api_endpoint)
    api_response = api_response.json()
    return flask.render_template("newweatherreport.html", api_data=api_response)
    ######################

######################

if __name__ == "__main__":
    with my_website_app.app_context():
        db.create_all()
    my_website_app.run(debug=True)