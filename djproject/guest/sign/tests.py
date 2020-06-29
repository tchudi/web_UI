from django.test import TestCase

# Create your tests here.
import requests
#
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# url="https://www.qhfax.com/user/login"
# data={
#         "userName":18576407718,
#         "password":"di4352089",
#         "retUrl":"https://www.qhfax.com/"
# }
# r=requests.post(url,data=data,verify=False)
# print(r.text)

url="https://sls.cdb.com.cn/slp/login"

data={
        "idCode":"421222199204190010",
        "hcode":"2",
        "password":"di4352089",
        "verification_code":"ZAVH",
        "idCard":"421222199204190010"
}
r=requests.post(url,data=data,verify=False)
print(r.json())
