from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    second_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
            return '<Contacts %r>' % self.id




#postgress sources
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date, ForeignKey

# engine = create_engine('postgresql+psycopg2://postgres:pilot123z@localhost:5432/Helper')
# Session = sessionmaker(bind=engine)
# Base = declarative_base()


    # def __init__(self, first_name, second_name, phone, email):
    #     self.first_name = first_name
    #     self.second_name = second_name
    #     self.phone = phone
    #     self.email = email
    #     self.date = date