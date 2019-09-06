'''
@author: lgx
@Email:297979949@qq.com
@project: 发送邮件
@file: main_process.py
@time: 2019-08-21 10:29
@desc:
'''
from get_love_days import get_days
from database_of_class import *
from get_weather_info import *
from send_mail_image import *
from email_class import *
import os

def main():
    #获取sql的查询条件
    days=get_days()
    id=days['id']
    day=str(days['day'])
    ds = DATABASE_STORY(id)
    print(id,day)
    #获取邮件发送状态,默认为1,没发送,0为已发送
    # send_status=get_send_status(id)
    send_status=ds.get_send_status()
    print(send_status)
    if send_status == '0':
        print("今天的邮件已经发送")
    else:
        # story_content=get_stort(id)
        story_content=ds.get_story()
        print(story_content)
        text_content = story_content['content']
        text_title = story_content['title']
        email_content = text_title + "\n\n\n" + text_content
        get_weather_pic()
        pic_path='天气情况.png'
        # send_email(days['day'],story_content,pic_path)
        #实例化发送邮件的类
        sm=SEND_MAIL(day)
        #构造邮件标题
        sm.email_heading()
        #构建邮件内容
        sm.send_text(email_content)
        #构建邮件附件图片
        sm.send_image(pic_path)
        sm.send_mail()
        print('邮件已经发送')
        #改变邮件发送状态
        # change_send_status(id)
        ds.change_send_status()
        print('邮件发送状态已经更改')










if __name__ == '__main__':
    main()