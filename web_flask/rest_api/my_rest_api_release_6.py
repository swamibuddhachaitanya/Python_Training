"""
REST API Using flask and SQLAlchemy
added support for 'GET, POST, PUT, PATCH, DELETE'
"""

# ----------
# Create App
############
import flask
from flask_sqlalchemy import SQLAlchemy

my_app = flask.Flask(__name__)
my_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_test_alchemy_db.sqlite3"

db = SQLAlchemy(my_app)

# Define the model
class mycoursetable(db.Model):
    # define column names and its data type
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100))
    course_mode = db.Column(db.String(100))
    course_location = db.Column(db.String(100))

# Make SQLAlchemy class object to json serializable
from flask_marshmallow import Marshmallow
ma = Marshmallow(my_app)

# Which column we need to serialize
class MyAppSchema(ma.Schema):
    class Meta:
        fields = ('course_id', 'course_name', 'course_mode', 'course_location')

my_app_schema = MyAppSchema(many=True)
######################

# ----------
# ENDPOINT-1: GET : http://127.0.0.1:5000/getdata
############
@my_app.route("/getdata")
def my_rest_api_get():
    all_records = mycoursetable.query.all()
    # make it json serializable
    all_records = my_app_schema.dump(all_records)
    return flask.jsonify(all_records)

# How to access?
# Refer: consume_api.py
######################

# ----------
# ENDPOINT-2: POST : http://127.0.0.1:5000/postdata
############
@my_app.route("/postdata", methods=["POST"])
def my_rest_api_post():
    received_record = flask.request.get_json()
    existing_record = db.session.get(mycoursetable, received_record["course_id"])
    if existing_record:
        return flask.jsonify({"message": "record already exists", "status": 201})
    else:
        new_record = mycoursetable()
        new_record.course_id = received_record["course_id"]
        new_record.course_name = received_record["course_name"]
        new_record.course_mode = received_record["course_mode"]
        new_record.course_location = received_record["course_location"]
        db.session.add(new_record)
        db.session.commit()
        return flask.jsonify({"message": "New record added", "status": 200})

# How to access?
# Refer: consume_api.py
######################


# ----------
# ENDPOINT-3: PUT : http://127.0.0.1:5000/putdata
############
@my_app.route("/putdata", methods=["PUT"])
def my_rest_api_put():
    received_record = flask.request.get_json()
    existing_record = db.session.get(mycoursetable, received_record["course_id"])
    if existing_record:
        existing_record.course_id = received_record["course_id"]
        existing_record.course_name = received_record["course_name"]
        existing_record.course_mode = received_record["course_mode"]
        existing_record.course_location = received_record["course_location"]
        db.session.add(existing_record)
        db.session.commit()
        return flask.jsonify({"message": "record UPDATED", "status": 201})
    else:
        new_record = mycoursetable()
        new_record.course_id = received_record["course_id"]
        new_record.course_name = received_record["course_name"]
        new_record.course_mode = received_record["course_mode"]
        new_record.course_location = received_record["course_location"]
        db.session.add(new_record)
        db.session.commit()
        return flask.jsonify({"message": "New record added", "status": 200})

# How to access?
# Refer: consume_api.py
######################

# ----------
# ENDPOINT-4: PATCH : http://127.0.0.1:5000/patchdata
############
@my_app.route("/patchdata", methods=["PATCH"])
def my_rest_api_patch():
    received_record = flask.request.get_json()
    existing_record = db.session.get(mycoursetable, received_record["course_id"])
    if existing_record:
        existing_record.course_id = received_record["course_id"]
        existing_record.course_name = received_record["course_name"]
        existing_record.course_mode = received_record["course_mode"]
        existing_record.course_location = received_record["course_location"]
        db.session.add(existing_record)
        db.session.commit()
        return flask.jsonify({"message": "record UPDATED", "status": 201})
    else:
        return flask.jsonify({"message": "No record found to update", "status": 200})

# How to access?
# Refer: consume_api.py
######################


# ----------
# ENDPOINT-5: DELETE : http://127.0.0.1:5000/deletedata
############
@my_app.route("/deletedata", methods=["DELETE"])
def my_rest_api_delete():
    received_record = flask.request.get_json()
    existing_record = db.session.get(mycoursetable, received_record["course_id"])
    if existing_record:
        db.session.delete(existing_record)
        db.session.commit()
        return flask.jsonify({"message": "record Deleted", "status": 201})
    else:
        return flask.jsonify({"message": "No record found to delete", "status": 200})

# How to access?
# Refer: consume_api.py
######################

# ----------
# Run the server
############
if __name__ == "__main__":
    with my_app.app_context():
        db.create_all()
    my_app.run()
######################