'''
@author: lgx
@Email:297979949@qq.com
@project: 发送邮件
@file: get_love_days.py
@time: 2019-08-21 9:48
@desc:
'''
import time

def get_days():
    '''

    :return: 返回一个字段,id:数据库主键
    days:天数
    '''

    days={}
    s_time=time.strptime('2016-6-13','%Y-%m-%d')
    s_timestamp=time.mktime(s_time)
    #print(s_timestamp)
    timestamp_diff=time.time()-s_timestamp
    #print(timestamp_diff)
    love_day=int(timestamp_diff/60/60/24)+1
    id=love_day-1138
    days['day']=love_day
    days['id']=id
    return days
    # print(days)


#
# get_days()