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
# all_service = Service.objects(gender=0)
# for service in all_service:
#     print(service['name'])

id_to_find="5af7cd4042198920ccdeb0eb"
# tìm id
# chung=Service.objects(id=id_to_find)
# chung=Service.objects.get(id=id_to_find)
c=Service.objects.with_id(id_to_find)
# xóa id
# c.delete()
# if c is not None:
#     c.delete()
#     print("deleted")
# else:
#     print("error")
# print(c.to_mongo())
if c is not None:
    print(c.phone)
    c.update(set__phone="01234567890", set__height="152")
    print("updated")
    print(c.phone) # vẫn in ra giá trị cũ do lấy c="id" từ ban đầu
    c.reload()
    print(c.height)
else:
    print("error")
