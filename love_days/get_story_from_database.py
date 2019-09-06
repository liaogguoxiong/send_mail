'''
@author: lgx
@Email:297979949@qq.com
@project: 发送邮件
@file: get_story_from_database.py
@time: 2019-08-20 21:56
@desc:
'''

import pymysql

#初始化参数
database_ip='192.168.1.126'
username='root'
passwd='123456'
port=3309
dbname='crawler_data'



def get_send_status(days):

    sql='SELECT  send_status FROM story WHERE id={}'.format(days)
    db = pymysql.connect(host=database_ip, user=username, password=passwd, port=port, db=dbname)
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchone()[0]
    return res



def get_stort(days):

    sql = 'select content from story where id={}'.format(days)
    db = pymysql.connect(host=database_ip, user=username, password=passwd, port=port, db=dbname)
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchone()[0]
    # print(res)
    return res


def change_send_status(id):
    sql='''UPDATE story SET send_status='0' WHERE id={};'''.format(id)
    db = pymysql.connect(host=database_ip, user=username, password=passwd, port=port, db=dbname)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print("更新更改")
    except:
        db.rollback()




# get_stort(1)
# # get_send_status(1)
#
# change_send_status('1')


