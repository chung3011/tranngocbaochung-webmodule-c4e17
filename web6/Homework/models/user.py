from mongoengine import *
import mlab
class User(Document):
    name = StringField()
    email = StringField()
    account = StringField()
    password = StringField()
