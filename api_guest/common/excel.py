import xlrd
from xlutils.copy import copy

class Excel():
    def __init__(self,filename=None,sheetid=None):
        if filename:
            self.filename=filename
            self.sheetid=sheetid
        else:
            self.filename='D:/api_guest/data/case.xls'
            self.sheetid=1
        self.data=self.get_data()

    def get_data(self):
        table=xlrd.open_workbook(self.filename)
        sheet=table.sheet_by_index(self.sheetid)
        return sheet

    #获取excel表格行数
    def get_lines(self):
        return self.data.nrows

    #获取某个单元格内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    #某个单元格写入数据
    def write_data(self,row,col,value):
        read_data=xlrd.open_workbook(self.filename)
        write_data=copy(read_data)
        sheet_data=write_data.get_sheet(1)
        sheet_data.write(row,col,value)
        write_data.save(self.filename)

    #获取某一列的数据
    def get_col_value(self,col=None):
        data=None
        if col!=None:
            data=self.data.col_values(col)
        else:
            data=self.data.col_values(0)
        return data

    #根据case依赖，获取case行号
    def get_case_row(self,caseid):
        caseids=self.get_col_value()
        row_num=caseids.index(caseid)
        return row_num





if __name__=="__main__":
    e=Excel()
    print(e.get_lines())
    print(e.get_cell_value(1,3))
    e.write_data(1,11,'pass')