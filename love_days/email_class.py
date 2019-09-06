'''
@author: lgx
@Email:297979949@qq.com
@project: send_mail
@file: email_class.py
@time: 2019-08-26 9:48
@desc:
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SEND_MAIL:

    def __init__(self,day):
        '''
        # 初始化收件人,发件人,发送人的账号和授权密码
        :param day:
        '''
        self.mail_server = 'smtp.qq.com'
        self.mail_user = '297979949@qq.com'
        self.mail_passwd = 'rhoexjltojtcbghc'
        self.sender = '297979949@qq.com'
        self.receiver = '602823525@qq.com'
        # self.receiver = '297979949@qq.com'
        self.day=day

        # 构建邮件对象Multipart对象
        self.msg=MIMEMultipart('mixed')


    def email_heading(self):
        '''
        构建主题，发件人，收件人，日期是显示在邮件页面上的。
        :return:
        '''
        subject = "这是我爱你的{}天!么么哒0_0".format(self.day)
        self.msg['From'] = Header(self.sender, 'utf-8').encode()
        self.msg['To'] = Header(self.receiver, 'utf-8').encode()
        self.msg['Subject'] = Header(subject, 'utf-8').encode()


    def send_text(self,text):
        '''
        发送文本邮件,传入的参数为邮件内容
        :return:
        '''
        mail_content = MIMEText(text, 'plain', 'utf-8')
        self.msg.attach(mail_content)


    def send_image(self,pic_path):
        '''
        构建邮件附件图片
        :param pic_path: 传入图片的绝对路径
        :return:
        '''
        picture=open(pic_path,'rb').read()
        mail_image=MIMEImage(picture)
        mail_image.add_header('Content-ID', '<image1>')
        mail_image.add_header('Content-Disposition', 'attachment', filename=Header(pic_path, 'utf-8').encode())
        self.msg.attach(mail_image)


    def send_mail(self):
        '''
        发送邮件
        :return:
        '''
        smtp = smtplib.SMTP()
        smtp.connect(self.mail_server, 25)
        smtp.login(self.mail_user, self.mail_passwd)
        smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
        smtp.quit()


# pic_path='天气情况.png'
# sm=SEND_MAIL('1170')
# sm.email_heading()
# sm.send_text("test")
# sm.send_image(pic_path)
# sm.send_mail()
