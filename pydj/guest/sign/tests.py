from django.test import TestCase

# Create your tests here.

import requests
# url='http://127.0.0.1:8000/guest_manage/'
#header={"sessionid":"mtbi7ugy3v6z2p8wtdg8cmx900d122wv"}
# r=requests.get(url,cookies=header)
# print(r.status_code,r.text)


# url="http://127.0.0.1:8000/api/add_event/"
# data={
#     "eid":5,
#     "name":"oppor发布会",
#     "limit":10000,
#     "status":"1",
#     "address":"深圳宝体",
#     "start_time":"2019-08-15 09:00:00"
# }
#


# url="http://127.0.0.1:8000/api/get_event_list/"
# data={
#     "eid":2
# }
# r=requests.get(url=url,params=data)
# print(r.status_code,r.json())


# url="http://127.0.0.1:8000/api/add_guest/"
# data={
#     "eid":"2",
#     "realname":"liu",
#     "phone":"13243177777",
#     "email":"liu@mail.com"
# }




# url="http://127.0.0.1:8000/api/user_sign/"
# data={
#     "eid":"1",
#     "phone":13243167815
# }
# r=requests.post(url=url,data=data)
# print(r.status_code,r.json())


url="http://127.0.0.1:8000/api/sec_get_event_list/"
data={"name":"华为mate30发布会"}
auth1=("admin","admin123456")
r=requests.get(url=url,auth=auth1,params=data)
print(r.json())


