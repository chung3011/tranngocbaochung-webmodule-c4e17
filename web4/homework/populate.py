import mlab
from models.user import User

mlab.connect()

user = User(name="",
            email="",
            account="admin",
            password="admin")
user.save()
