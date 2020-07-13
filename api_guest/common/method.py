import requests

'''请求方法'''
class Method():
    def get(self,url,data=None,header=None):
        res=None
        if header!=None:
            res=requests.get(url=url,params=data,headers=header)
        else:
            res=requests.get(url=url,params=data)
        return res.json()

    def post(self,url,data,header=None):
        res=None
        if header!=None:
            res=requests.post(url=url,data=data,headers=header)
        else:
            res=requests.post(url=url,data=data)
        return res.json()

    def main(self,method,url,data=None,header=None):
        res=None
        if method=='get':
            res=self.get(url,data,header)

        else:
            res=self.post(url,data,header)
        return res

if __name__=="__main__":
    m=Method()
    url='http://127.0.0.1:8000/api/get_event_list/'
    data={'eid':1}
    print(m.get(url,data))


