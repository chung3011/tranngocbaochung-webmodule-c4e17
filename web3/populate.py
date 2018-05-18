import mlab
from models.service import Service
from faker import Faker
from random import randint, choice
from cFake import *
mlab.connect()

fake = Faker()
for i in range(200):
    print(i+1,"....")
    g=randint(0,1)
    if g==0:
        n=female_name()
        i=female_image()
    elif g==1:
        n=male_name()
        i=male_image()
    service = Service(name=n,
                 yob=randint(1990,2001),
                 gender=g,
                 height=randint(150,190),
                 phone=sdt(),
                 address=tp(),
                 description=description(),
                 measurements=measurements(),
                 image=i,
                 status= choice([True,False]))
    service.save()
