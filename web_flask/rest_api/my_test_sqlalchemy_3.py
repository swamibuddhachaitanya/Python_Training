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

        print("Inside the object 'mycoursetable'")
        print("-"*20)
        # -------------
        print(dir(mycoursetable))
        ##########################

        print("Inside the object 'mycoursetable.query'")
        print("-"*20)
        # -------------
        print(dir(mycoursetable.query))
        ##########################

        print("All records")
        print("-"*20)
        # -------------
        all_records = mycoursetable.query.all() # [<mycoursetable 1>, <mycoursetable 2>]
        print(all_records)
        ##########################

        print("One record info")
        print("-"*20)
        # -------------
        all_records = mycoursetable.query.all() # [<mycoursetable 1>, <mycoursetable 2>]
        one_record = all_records[0] # <mycoursetable 1>
        print(one_record.course_id)
        print(one_record.course_name)
        print(one_record.course_mode)
        print(one_record.course_location)
        ##########################

        # print("Other method for One record info")
        # print("-"*20)
        # # -------------
        # one_record = mycoursetable.query.one() # We will get error because we have multiple rows
        # print(one_record.course_id)
        # print(one_record.course_name)
        # print(one_record.course_mode)
        # print(one_record.course_location)
        # ##########################

        # print("Other method for One record info")
        # print("-"*20)
        # # -------------
        # one_record = mycoursetable.query.one_or_404() # We will get error because we have multiple rows
        # print(one_record.course_id)
        # print(one_record.course_name)
        # print(one_record.course_mode)
        # print(one_record.course_location)
        # ##########################

        # print("Other method for One record info")
        # print("-"*20)
        # # -------------
        # one_record = mycoursetable.query.one_or_none() # We will get error because we have multiple rows
        # print(one_record.course_id)
        # print(one_record.course_name)
        # print(one_record.course_mode)
        # print(one_record.course_location)
        # ##########################

        # print("record info using get()")
        # print("-"*20)
        # # -------------
        # one_record = mycoursetable.query.get(1) # mention primary key but DEPRECATED
        # print(one_record.course_id)
        # print(one_record.course_name)
        # print(one_record.course_mode)
        # print(one_record.course_location)
        # ##########################

        print("record info using session.get()")
        print("-"*20)
        # -------------
        one_record = db.session.get(mycoursetable, 1)
        print(one_record.course_id)
        print(one_record.course_name)
        print(one_record.course_mode)
        print(one_record.course_location)
        ##########################

######################

