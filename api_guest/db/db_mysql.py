import pymysql

class DB():
    def __init__(self):
        try:
            self.conn=pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            db='guest',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  # 游标默认获取的数据是元组类型，使用字典数据
            )
        except pymysql.err.OperationalError as e:
            print("Mysql error %d:%s" % (e.args[0], e.args[1]))

    def clear(self,table):
        sql="delete from "+table+";"
        with self.conn.cursor() as cursor:
            cursor.execute("set foreign_key_checks=0;")
            cursor.execute(sql)
        self.conn.commit()

    def select(self,sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
        return cursor.fetchall()

    def insert(self,table,data):
        for key in data:
            data[key]="'"+str(data[key])+"'"
        key=','.join(data.keys())
        value=','.join(data.values())
        sql="insert into "+table+"("+key+") values ("+value+")"
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()

    def init_data(self,datas):
        for table,d in datas.items():
            self.clear(table)
            for data in d:
                self.insert(table,data)
        self.close()

if __name__=="__main__":
    datas = {
        # 发布会表数据
        'sign_event': [
            {'id': 1, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
             'start_time': '2019-09-09 09:00:00','create_time':'2020-10-10 12:00:00'},
            {'id': 2, 'name': '苹果iphon6发布会', '`limit`': 1000, 'status': 1, 'address': '宝安体育馆',
             'start_time': '2019-09-09 09:00:00','create_time':'2020-10-10 12:00:00'},
            {'id': 3, 'name': '华为荣耀8发布会', '`limit`': 2000, 'status': 0, 'address': '深圳福田会展中心',
             'start_time': '2019-09-09 09:00:00','create_time':'2020-10-10 12:00:00'},
            {'id': 4, 'name': '苹果iphon8发布会', '`limit`': 2000, 'status': 1, 'address': '深圳湾体育中心',
             'start_time': '2019-09-09 09:00:00','create_time':'2020-10-10 12:00:00'},
            {'id': 5, 'name': '小米5发布会', '`limit`': 2000, 'status': 1, 'address': '北京国家会议中心',
             'start_time': '2019-09-09 09:00:00','create_time':'2020-10-10 12:00:00'},
        ],
        # 　嘉宾表数据
        'sign_guest': [
            {'id': 1, 'realname': 'Tom', 'phone': 13511886601, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1,'create_time':'2020-10-10 12:00:00'},
            {'id': 2, 'realname': 'Jason', 'phone': 13511886602, 'email': 'sign@mail.com', 'sign': 1, 'event_id': 1,'create_time':'2020-10-10 12:00:00'},
            {'id': 3, 'realname': 'Jams', 'phone': 13511886603, 'email': 'tom@mail.com', 'sign': 0, 'event_id': 5,'create_time':'2020-10-10 12:00:00'},
        ],
    }

    db=DB()
    # db.clear('sign_event')
    # db.clear('sign_guest')

    db.init_data(datas)
