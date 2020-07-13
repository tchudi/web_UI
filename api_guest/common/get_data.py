from common.excel import Excel
from data.data_config import DataConfig
from common.method import Method
import json
class GetData():
    def __init__(self):
        self.excel=Excel()
        self.method=Method()

    def get_case_lines(self):
        return self.excel.get_lines()

    def get_id(self,row):
        col=DataConfig.id
        return self.excel.get_cell_value(row,col)

    def get_name(self,row):
        col=DataConfig.name
        return self.excel.get_cell_value(row,col)

    def get_url(self,row):
        col=DataConfig.url
        return self.excel.get_cell_value(row,col)

    def get_is_run(self,row):
        col=DataConfig.is_run
        flag=None
        is_run=self.excel.get_cell_value(row,col)
        if is_run=='yes':
            flag=True
        else:
            flag=False
        return flag

    def get_request_method(self,row):
        col=DataConfig.method
        return self.excel.get_cell_value(row,col)


    def get_request_data(self,row):
        col=DataConfig.data
        request_data=self.excel.get_cell_value(row,col)
        return json.loads(request_data)

    def get_expect(self,row):
        col=DataConfig.expect
        return self.excel.get_cell_value(row,col)

    def write_result(self,row,value):
        col=DataConfig.result
        self.excel.write_data(row,col,value)

    def write_response_data(self,row,value):
        col=DataConfig.response
        value=json.dumps(value)
        self.excel.write_data(row,col,value)

    def get_case_depend(self,row):
        col=DataConfig.case_depend
        case_depend=self.excel.get_cell_value(row,col)
        if case_depend=='':
            return None
        else:
            return case_depend

    def get_data_depend(self,row):
        col=DataConfig.data_depned
        return self.excel.get_cell_value(row,col)

    def get_data_key_depend(self,row):
        col=DataConfig.data_key_depend
        return self.excel.get_cell_value(row,col)



if __name__=='__main__':
    getdata=GetData()
    getdata.write_data_value(2,'fail')