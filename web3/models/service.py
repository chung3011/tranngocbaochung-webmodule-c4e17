from mongoengine import StringField, IntField, BooleanField, Document, ListField, ImageField
# from mongoengine import *
import mlab
# design db
# create collection
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    measurements = ListField()
    image = StringField()
