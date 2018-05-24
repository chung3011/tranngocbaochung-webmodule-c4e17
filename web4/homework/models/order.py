from mongoengine import *
import mlab
class Order(Document):
    service_name = StringField()
    service_user = StringField()
    time = DateTimeField()
    is_accepted = BooleanField()
