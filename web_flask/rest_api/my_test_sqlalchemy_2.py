"""
SQL Alchemy Example
add entry to database
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

        print("Inside the object 'db'")
        print("-"*20)
        # -------------
        print(dir(db))
        print("#"*40, end="\n\n")
        ##########################

        print("Inside the object 'mycoursetable'")
        print("-"*20)
        # -------------
        print(dir(mycoursetable))
        print("#"*40, end="\n\n")
        ##########################

        print("1-way to add new record to 'mycoursetable'")
        print("-"*20)
        # -------------
        new_record = mycoursetable(course_id = 1, course_name = 'n1', course_mode = 'm1', course_location='l1')
        db.session.add(new_record)
        db.session.commit()
        print("1st record added")
        print("#"*40, end="\n\n")
        ##########################

        print("2-way to add new record to 'mycoursetable'")
        print("-"*20)
        # -------------
        new_record = mycoursetable()
        new_record.course_id = 2
        new_record.course_name = 'n2'
        new_record.course_mode = 'm2'
        new_record.course_location='l2'
        db.session.add(new_record)
        db.session.commit()
        print("2nd record added")
        print("#"*40, end="\n\n")
        ##########################

        print("-" * 20)
        # -------------
        new_record = mycoursetable()
        new_record.course_id = 3
        new_record.course_name = 'n3'
        new_record.course_mode = 'm3'
        new_record.course_location = 'l3'
        db.session.add(new_record)
        db.session.commit()
        print("3rd record added")
        print("#" * 40, end="\n\n")
        ##########################

######################