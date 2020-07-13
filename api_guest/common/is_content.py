import json


class CommContent():
    def content(self, str_one, str_two):
        flag = None
        str_t = json.dumps(str_two)
        if str_one in str_t:
            flag = True
        else:
            flag = False
        return flag


if __name__ == '__main__':
    str_one = '"status": 200'
    str_two = {'status': 200, 'message': 'success'}
    con = CommContent()
    print(con.content(str_one, str_two))
