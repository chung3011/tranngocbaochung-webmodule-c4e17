from mongoengine import *
# from models.service import Service
# from models.user import User
import mlab

class Order(Document):
    # service_name = ReferenceField(Service)
    # service_user = ReferenceField(User)
    service_name = StringField()
    service_user = StringField()
    time = DateTimeField()
    is_accepted = BooleanField()
