from data.data_config import DataConfig
from common.method import Method
from common.get_data import GetData
from jsonpath_rw import parse
from common.excel import Excel
class DependData():
    def __init__(self,caseid):
        self.caseid=caseid
        self.method=Method()
        self.getdata=GetData()
        self.excel=Excel()
    # 获取依赖的响应数据
    def get_response_data(self):
        #caseid = self.get_case_depend(row)
        row_num = self.excel.get_case_row(self.caseid)
        url = self.getdata.get_url(row_num)
        request_method = self.getdata.get_request_method(row_num)
        request_data = self.getdata.get_request_data(row_num)
        response_data = self.method.main(request_method, url, request_data)
        return response_data

    #获取依赖字段的值
    def get_data_value(self,row):
        depend_data=self.getdata.get_data_depend(row)
        response_data=self.get_response_data()
        json_exe=parse(depend_data)
        madle=json_exe.find(response_data)
        return [math.value for math in madle][0]


if __name__=='__main__':
    pass