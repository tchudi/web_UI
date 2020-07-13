from common.get_data import GetData
from common.method import Method
from common.is_content import CommContent
from common.depend_data import DependData
from log.common_log import Logger
from db import test_data


class Run():
    def __init__(self):
        self.getdata = GetData()
        self.method = Method()
        self.content = CommContent()
        self.logger = Logger().getlog()

    def go_on_run(self):
        cases_count = self.getdata.get_case_lines()
        for i in range(1, cases_count):
            name = self.getdata.get_name(i)
            request_url = self.getdata.get_url(i)
            request_method = self.getdata.get_request_method(i)
            request_data = self.getdata.get_request_data(i)
            is_run = self.getdata.get_is_run(i)
            expect = self.getdata.get_expect(i)
            case_depend = self.getdata.get_case_depend(i)

            if is_run:
                # print(request_url,request_data,request_method)
                if case_depend:
                    key_depend = self.getdata.get_data_key_depend(i)
                    dependdata = DependData(case_depend)
                    request_data[key_depend] = dependdata.get_data_value(i)

                self.logger.info('-----%s-----' % name)
                self.logger.info('请求url地址：{}'.format(request_url))
                self.logger.info('请求参数：%s' % request_data)
                res = self.method.main(request_method, request_url, request_data)
                self.logger.info('响应结果：%s' % res)
                is_content = self.content.content(expect, res)
                if is_content:
                    self.getdata.write_result(i, 'pass')
                    self.logger.info('通过')
                else:
                    self.getdata.write_result(i, 'fail')
                    self.getdata.write_response_data(i, res)
                    self.logger.info('失败')

        return res


if __name__ == '__main__':
    test_data.init_datas()
    run = Run()
    run.go_on_run()
