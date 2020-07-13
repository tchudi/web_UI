from db.db_mysql import DB


datas = {
        # 发布会表数据
        'guest.sign_event': [
            {'id': 1, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
             'start_time': '2019-09-09 09:00:00'},
            {'id': 2, 'name': '苹果iphon6发布会', '`limit`': 1000, 'status': 1, 'address': '宝安体育馆',
             'start_time': '2019-09-09 09:00:00'},
            {'id': 3, 'name': '华为荣耀8发布会', '`limit`': 2000, 'status': 0, 'address': '深圳福田会展中心',
             'start_time': '2019-09-09 09:00:00'},
            {'id': 4, 'name': '苹果iphon8发布会', '`limit`': 2000, 'status': 1, 'address': '深圳湾体育中心',
             'start_time': '2019-09-09 09:00:00'},
            {'id': 5, 'name': '小米5发布会', '`limit`': 2000, 'status': 1, 'address': '北京国家会议中心',
             'start_time': '2019-09-09 09:00:00'},
        ],
        # 　嘉宾表数据
        'guest.sign_guest': [
            {'id': 1, 'realname': 'Tom', 'phone': 13511886601, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1},
            {'id': 2, 'realname': 'Jason', 'phone': 13511886602, 'email': 'sign@mail.com', 'sign': 1, 'event_id': 2},
            {'id': 3, 'realname': 'Jams', 'phone': 13511886603, 'email': 'tom@mail.com', 'sign': 0, 'event_id': 5},
        ],
    }



def init_datas():
    db=DB()
    db.init_data(datas)


