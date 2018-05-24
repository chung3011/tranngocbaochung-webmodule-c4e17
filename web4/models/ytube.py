from mongoengine import *
import mlab

class ytube(Document):
    title = StringField()
    views = IntField()
    thumbnail = StringField()
    youtubeid = StringField()
    link=StringField()
