import mlab
from models.service import Service
from faker import Faker
from random import randint, choice
from cFake import *
mlab.connect()

fake = Faker()
# print(fake.address())

# create Document
# service = Service(name="Chung", yob=1997, gender=1,height=168,phone="01693446595", address="Hà Nội", status= False)
for i in range(10):
    print(i,"....")
    g=randint(0,1)
    if g==0:
        n=female_name()
    elif g==1:
        n=male_name()
    service = Service(name=n,
                 yob=randint(1990,2001),
                 gender=g,
                 height=randint(150,190),
                 phone=sdt(),
                 address=tp(),
                 status= choice([True,False]))
    service.save()
