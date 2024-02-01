"""
SQL Alchemy Example
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
######################

# ----------
# Create App
############
if __name__ == "__main__":
    with my_app.app_context():
        db.create_all()
######################