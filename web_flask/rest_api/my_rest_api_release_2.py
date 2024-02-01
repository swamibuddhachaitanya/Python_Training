"""
REST API Using flask and SQLAlchemy
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
# Run the server
############
if __name__ == "__main__":
    with my_app.app_context():
        db.create_all()
    my_app.run()
######################