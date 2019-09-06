'''
@author: lgx
@Email:297979949@qq.com
@project: send_mail
@file: database_of_class.py
@time: 2019-08-23 10:55
@desc:
'''

import pymysql

class DATABASE_STORY:


    def __init__(self,id):
        # 初始化参数
        database_ip = '192.168.1.126'
        username = 'root'
        passwd = '123456'
        port = 3309
        dbname = 'crawler_data'
        self.id=id
        self.db = pymysql.connect(host=database_ip, user=username, password=passwd, port=port, db=dbname)
        self.cursor = self.db.cursor()

    def get_send_status(self):
        sql=sql='SELECT  send_status FROM story WHERE id={}'.format(self.id)
        self.cursor.execute(sql)
        # print(self.cursor.fetchone())
        res = self.cursor.fetchone()[0]
        return res


    def get_story(self):
        story_dic={}
        sql='select title,content from story where id={}'.format(self.id)
        self.cursor.execute(sql)
        # res = self.cursor.fetchone()[0]
        # print(res)
        res=self.cursor.fetchone()
        story_dic['title']=res[0]
        story_dic['content']=res[1]
        print(story_dic)
        return story_dic


    def change_send_status(self):
        sql='''UPDATE story SET send_status='0' WHERE id={};'''.format(self.id)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("更新成功")
        except:
            self.db.rollback()


# ds=DATABASE_STORY(200)
# res=ds.get_story()
# print(type(res))
# print(res['title']+"\n\n\n"+res['content'])

