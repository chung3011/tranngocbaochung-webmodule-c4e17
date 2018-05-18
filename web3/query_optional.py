import mlab_optional
from mongoengine import *


mlab_optional.connect()

class river(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

all_river = river.objects(continent="Africa")
for i,river in enumerate(all_river):
    print(i+1,'/',river['name'],',',river['continent'],',',river['length'])

# all_river = river.objects(continent="S. America", length__lt=1000)
# for i,river in enumerate(all_river):
#     print(i+1,'/',river['name'],',',river['continent'],',',river['length'])
