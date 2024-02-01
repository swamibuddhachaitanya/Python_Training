"""
test release: to test ORM using flask and SQL alchemy
"""

from flask_sqlalchemy import SQLAlchemy
# SQLAlchemy : For ORM

from flask_marshmallow import Marshmallow
# Marshmallow: For Serialization & Deserialization

from flask import Flask

my_app = Flask(__name__)

my_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_alchemy_test_db.sqlite3"

db = SQLAlchemy(my_app)
ma = Marshmallow(my_app)

# Define the model
class MyModel(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    user_password = db.Column(db.String(100))
    user_email = db.Column(db.String(100))

# Which column we need to serialize
class MyAppSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'user_name', 'user_password', 'user_email')

my_app_schema = MyAppSchema(many=True)


if __name__ == "__main__":
    with my_app.app_context():
        db.create_all()