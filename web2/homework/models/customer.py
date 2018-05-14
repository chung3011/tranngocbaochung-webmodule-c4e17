from mongoengine import StringField, IntField, BooleanField, Document
# from mongoengine import *
import mlab
# design db
# create collection
class Customer(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    email = StringField()
    phone = StringField()
    address = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()
