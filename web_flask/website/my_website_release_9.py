"""
if login success then display db data
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
    # Task-3: Create database and table
    # -----------
    import sqlite3
    my_db_connection = sqlite3.connect("my_users_db.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_query = """
    CREATE TABLE IF NOT EXISTS MY_USERS_TABLE (
    USERNAME VARCHAR(100),
    PASSWORD VARCHAR(100),
    EMAIL VARCHAR(100)
    )
    """
    my_db_cursor.execute(my_query)
    ######################

    # -----------
    # Task-4: verify whether user already exists
    # -----------
    my_query = f"SELECT COUNT(*) FROM MY_USERS_TABLE WHERE USERNAME = '{entered_username}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchone() # Example: (10, )
    user_count = my_db_result[0] # Example 10
    if user_count > 0:
        my_db_connection.close()
        return "User already exist.<br><a href='/register'>Go Back</a>"
    else:
        my_query = f"INSERT INTO MY_USERS_TABLE VALUES('{entered_username}', '{entered_password_1}', '{entered_email}')"
        my_db_cursor.execute(my_query)
        my_db_connection.commit()
        my_db_connection.close()
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
        return flask.render_template("logreport.html", my_db_data = my_log_db_result)
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
# Run builtin server
############
my_website_app.run(debug=True)
# my_website_app.run(host='127.0.0.1', port=1234)
######################