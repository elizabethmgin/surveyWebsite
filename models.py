from flask import Flask

"""
Commented out Mongo stuff for now while we figure out the server situation.
from flaskext.mongoalchemy import MongoAlchemy

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'x'
app.config['MONGOALCHEMY_USER'] = 'x'
app.config['MONGOALCHEMY_PASSWORD'] = 'x'
app.config['MONGOALCHEMY_SERVER_AUTH'] = False
db = MongoAlchemy(app)
"""

#This assumes we're using shelve but should work for anything
class User(object):
    def __init__(self, given_name=None, surname=None, home=None, age=None, gender=None):
        self.given_name = given_name
        self.surname = surname
        self.full_name = str(given_name) + " " + str(surname)
        self.home = home
        self.age = age
        self.gender = gender
    def set_phone(self, own_phone, phone_type):
        self.own_phone = own_phone
        self.phone_type = phone_type
    def set_social_media(self, facebook, email):
        self.facebook = facebook
        self.email = email
    def set_web_sites(self, web_sites):
        self.web_sites = []