import pymysql.cursors

#connect to the database
connection=pymysql.connect(host=127.0.0.1,
                        user='root',
                        password='root',
                        db='test',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql="insert into sign_guest(realname,phone,email,sign,event_id,create_time) values('alen',18800110001,'alen@mail.com',0,2,NOW());"
        cursor.execute(sql)

    connection.commit()


    with connection.cursor() as cursor:
        sql="select relaname,phone,email,sign from sign_guest where phone=%s"
        cursor.execute(sql,('18800110001',))
        result=cursor.fetchone()
        print(result)
finally:
    connection.close()