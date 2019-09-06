'''
@author: lgx
@Email:297979949@qq.com
@project: 发送邮件
@file: 发送文本.py
@time: 2019-08-15 11:29
@desc:
'''
import smtplib
from email.mime.text import MIMEText
from  email.header import Header

#初始化发送邮件邮件服务器,用户,授权密码,发送人,收件人
mail_server='smtp.qq.com'
mail_user='297979949@qq.com'
mail_passwd='rhoexjltojtcbghc'
sender='297979949@qq.com'
#收件人可以是一个,也可以是多个,多个使用列表表示
receiver=['526831381@qq.com','297979949@qq.com']
# receiver='526831381@qq.com'

#########构造头部信息,也就是主题,收件人,发件人,内容############

#构建MIMEText对象,第一个参数是邮件正文，第二个参数是MIME的subtype，最后一定要用utf-8编码保证多语言兼容性
#如果是html,则第二个参数改为html
content='test'
msg=MIMEText(content,'plain','utf-8')
msg['From']=Header(sender,'utf-8').encode()
msg['To']=Header('526831381@qq.com;297979949@qq.com','utf-8').encode()
msg['Subject']=Header('this is a test,这是一个测试 ','utf-8').encode()

##########发送邮件###########
smtp=smtplib.SMTP()
smtp.connect(mail_server,25)
smtp.login(mail_user,mail_passwd)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

