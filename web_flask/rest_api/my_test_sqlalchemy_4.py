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

        print("Inside the object 'mycoursetable'")
        print("-" * 20)
        # -------------
        print(dir(mycoursetable))
        ##########################

        print("Inside the object 'mycoursetable.query'")
        print("-" * 20)
        # -------------
        print(dir(mycoursetable.query))
        ##########################

        print("All records")
        print("-" * 20)
        # -------------
        all_records = mycoursetable.query.all()  # [<mycoursetable 1>, <mycoursetable 2>,<mycoursetable 3>]
        print(all_records)
        ##########################

        print("record info using session.get()")
        print("-" * 20)
        # -------------
        one_record = db.session.get(mycoursetable, 3)
        db.session.delete(one_record)
        db.session.commit()
        print("Record Deleted")
        ##########################

        print("All records After Delete")
        print("-" * 20)
        # -------------
        all_records = mycoursetable.query.all()  # [<mycoursetable 1>, <mycoursetable 2>,<mycoursetable 3>]
        print(all_records)
        ##########################

######################

        print("'filter' and 'where'")
        print("-"*20)
        # -------------
        all_records = mycoursetable.query.filter(mycoursetable.course_name == 'n2').first()
        print(all_records)
        all_records = mycoursetable.query.where(mycoursetable.course_name == 'n2').first()
        print(all_records)
        ##########################