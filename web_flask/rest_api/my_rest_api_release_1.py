"""
flask for developing RESTFul web services like REST-API and Micro Services
"""

"""
Example: Suppose if we need to provide access to our log data table
with others then

OPTION-1: is providing all credentials with others/public

OPTION-1 will not work for many reason including security

OPTION-1 is like
out-data/db  <--DIRECT ACCESS-->    others/public
"""

"""
Then we got 2 solutions/procedure/architecture/design/style
1) SOAP : Simple Object Access Protocal
2) REST : REpresentational State Transfer

Both tells, introduce some gate/interface b/n your application with others

This OPTION is like
out-data/db  <--INTERFACE-->    others/public

We can also call this INTERFACE as "APPLICATION PROGRAMMING INTERFACE"(API)

SOAP-API
REST-API
"""

"""
REST came after SOAP
- REST is easy to implement
- REST is popular
"""

"""
Again
how to create REST-API using REST architecture to share log data table?
- No need to implement from the scratch

Because,
flask is already implmented REST architecture
"""

"""
Again
how to create REST-API using FLASK to share log data table?

Steps
1. create app
2. create end point
3. in endpoint get data from log data table
4. return data in json
5. run the server
6. Share end point url with others so that they can 
access through the end point url

"""

"""
flask for developing RESTFul web services like REST-API and Micro Services
"""

"""
Example: Suppose if we need to provide access to our log data table
with others then

OPTION-1: is providing all credentials with others/public

OPTION-1 will not work for many reason including security

OPTION-1 is like
out-data/db  <--DIRECT ACCESS-->    others/public
"""

"""
Then we got 2 solutions/procedure/architecture/design/style
1) SOAP : Simple Object Access Protocal
2) REST : REpresentational State Transfer

Both tells, introduce some gate/interface b/n your application with others

This OPTION is like
out-data/db  <--INTERFACE-->    others/public

We can also call this INTERFACE as "APPLICATION PROGRAMMING INTERFACE"(API)

SOAP-API
REST-API
"""

"""
REST came after SOAP
- REST is easy to implement
- REST is popular
"""

"""
Again
how to create REST-API using REST architecture to share log data table?
- No need to implement from the scratch

Because,
flask is already implmented REST architecture
"""

"""
Again
how to create REST-API using FLASK to share log data table?

Steps
1. create app
2. create end point
3. in endpoint get data from log data table
4. return data in json
5. run the server
6. Share end point url with others so that they can 
access through the end point url

"""


# -------
# create app
#########
import flask

import sqlite3



my_api_app = flask.Flask(__name__)
##############

# -------
# REST API END POINT: URL http://127.0.0.1:5000/ mapped to route("/")
#########
@my_api_app.route("/")
def my_rest_api():
    my_db_connection = sqlite3.connect("../website/my_data_db.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_DATA_TABLE")
    my_db_result = my_db_cursor.fetchall()
    return flask.jsonify(my_db_result)
##############



# -------
# Run the server
#########
my_api_app.run()
##############