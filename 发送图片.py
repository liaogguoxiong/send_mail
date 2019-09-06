'''
@author: lgx
@Email:297979949@qq.com
@project: 发送邮件
@file: 发送图片.py
@time: 2019-08-16 17:32
@desc:
'''

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

#初始化收件人,发件人,发送人的账号和授权密码
mail_server='smtp.qq.com'
mail_user='297979949@qq.com'
mail_passwd='rhoexjltojtcbghc'
sender='297979949@qq.com'
receiver='602823525@qq.com'

#构建邮件对象MIMEMUltipart
msg=MIMEMultipart('mixed')


#构建主题，发件人，收件人，日期是显示在邮件页面上的。
subject='天气预告'
msg['From']=Header(sender,'utf-8').encode()
msg['To']=Header(receiver,'utf-8').encode()
msg['Subject']=Header(subject,'utf-8').encode()

#构建邮件的文本内容
text='嘿嘿嘿'
text_plain=MIMEText(text,'plain','utf-8')
msg.attach(text_plain)

#构建图片链接
pic_name='天气情况.png'
send_image_file=open(pic_name,'rb').read()
image=MIMEImage(send_image_file)
image.add_header('Content-ID','<image1>')
image.add_header('Content-Disposition', 'attachment',filename=Header(pic_name, 'utf-8').encode())
msg.attach(image)

smtp=smtplib.SMTP()
smtp.connect(mail_server,25)
smtp.login(mail_user,mail_passwd)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

