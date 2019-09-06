'''
@author: lgx
@Email:297979949@qq.com
@project: 发送邮件
@file: send_mail_image.py
@time: 2019-08-21 11:01
@desc:
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.multipart import MIMEMultipart


def send_email(day,text,image):
    '''

    :param day: 天数
    :param text:传入一个字典,对应的值分别是文章的标题和内容
    :param image: 图片路径,绝对路径
    :return:
    '''
    # 初始化收件人,发件人,发送人的账号和授权密码
    mail_server = 'smtp.qq.com'
    mail_user = '297979949@qq.com'
    mail_passwd = 'rhoexjltojtcbghc'
    sender = '297979949@qq.com'
    receiver = '602823525@qq.com'

    #构建邮件对象Multipart对象,由于发送的邮件里面有图片,需要需要组合构建
    msg=MIMEMultipart('mixed')

    #构建主题，发件人，收件人，日期是显示在邮件页面上的。
    subject="这是我爱你的{}天!么么哒0_0".format(day)
    msg['From']=Header(sender,'utf-8').encode()
    msg['To']=Header(receiver,'utf-8').encode()
    msg['Subject']=Header(subject,'utf-8').encode()

    #构建邮件内容
    text_content=text['content']
    text_title=text['title']
    text_type=text_title+"\n\n\n"+text_content
    mail_content=MIMEText(text_type,'plain','utf-8')
    msg.attach(mail_content)

    #构建图片附件
    pic_path=open(image,'rb').read()
    mail_image=MIMEImage(pic_path)
    mail_image.add_header('Content-ID','<image1>')
    mail_image.add_header('Content-Disposition','attachment',filename=Header(image,'utf-8').encode())
    msg.attach(mail_image)


    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(mail_server, 25)
    smtp.login(mail_user, mail_passwd)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
