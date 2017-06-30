#! -*- coding=utf-8 -*-


import pymysql




def create_mysql_conn():
    """
     获取conn ，cursor 方式2
    :return:
    """
    connection = pymysql.connect(host='127.0.0.1',
                                 user='zhouze',
                                 password='zhouze',
                                 db='stone_schema',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    return connection, cursor




def create_mysql_conn2():
    """
    获取conn ，cursor 方式1
    :return:
    """
    # 1.创建连接：
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='zhouze', passwd='zhouze', db='stone_schema')
    # 2.创建游标以字典的类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    return conn,cursor




def select_demo():
    conn,cursor = create_mysql_conn()

    # 3.执行sql，并返回受到的影响行数
    effect_row = cursor.execute("select * from stone_user")

    # 查询所有的记录
    result = cursor.fetchall()
    print result

    # absolute绝对移动
    cursor.scroll(0, mode='absolute')
    # 查询光标的下一条记录
    result = cursor.fetchone()
    print result
    result = cursor.fetchone()
    print result
    result = cursor.fetchone()
    print result

    # absolute绝对移动
    cursor.scroll(6, mode='absolute')
    result = cursor.fetchone()
    print result
    result = cursor.fetchone()
    print result

    # relative相对移动；
    cursor.scroll(-1, mode='relative')
    result = cursor.fetchone()
    print result

    # 4.关闭游标
    cursor.close()
    # 5.关闭连接
    conn.close()


def get_auto_increament():
    """
    获取自增id，
    pS: 得用insert语句做桥梁，不用真的提交。
    :return:
    """
    conn, cursor = create_mysql_conn()
    cursor.execute("insert into stone_user(username) values(%s)", ('ggg'))
    # cursor.execute("select * from stone_user")
    print '----', cursor.lastrowid
    #
    cursor.close()
    conn.close()


def insert_demo():
    """
    insert 语句测试
    :return:
    """
    conn, cursor = create_mysql_conn()
    cursor.execute("insert into stone_user(username) values(%s)", ('ggg'))
    #
    conn.commit()
    #
    cursor.close()
    conn.close()


def update_demo():
    """
    update 语句测试
    :return:
    """
    conn, cursor = create_mysql_conn()
    cursor.execute("update stone_user SET username=%s where user_id =%s", ('zz-lt',14,))
    #
    conn.commit()
    #
    cursor.close()
    conn.close()


def delete_demo():
    """
    delete 语句测试
    :return:
    """
    conn, cursor = create_mysql_conn()
    cursor.execute("delete from stone_user where user_id=%s", (16,))
    #
    conn.commit()
    #
    cursor.close()
    conn.close()



if __name__ == '__main__':
    select_demo()
    # get_auto_increament()
    # insert_demo()
    update_demo()
    # delete_demo()

