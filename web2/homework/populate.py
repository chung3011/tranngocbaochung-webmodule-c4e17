import mlab
from models.customer import Customer
from faker import Faker
from random import randint, choice
from cFake import *
mlab.connect()

fake = Faker()

for i in range(10):
    print(i,"....")
    g=randint(0,1)
    if g==0:
        n=female_name()
    elif g==1:
        n=male_name()
    customer = Customer(name=n,
                 yob=randint(1990,2001),
                 gender=g,
                 email= fake.ascii_email(),
                 phone=sdt(),
                 address=tp(),
                 job=job(),
                 company=cty(),
                 contacted= choice([True,False]))
    customer.save()
