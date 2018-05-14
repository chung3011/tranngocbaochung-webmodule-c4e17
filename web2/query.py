import mlab
from models.service import Service

mlab.connect()

# all_service = Service.objects()
# for service in all_service:
#     print(service['name'])
# for index,service in enumerate(all_service):
#     print(index,service['name'])
#     if index==9:
#         break
all_service = Service.objects(gender=0)
for service in all_service:
    print(service['name'])
