'''
@author: lgx
@Email:297979949@qq.com
@project: 发送邮件
@file: 发送附件.py
@time: 2019-08-16 16:33
@desc:
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_server='smtp.qq.com'
mail_user='297979949@qq.com'
mail_passwd='rhoexjltojtcbghc'
sender='297979949@qq.com'
receiver=['297979949@qq.com','526831381@qq.com']

#如果需要发送文本,附件,图片的话,可以使用MIMEMultipart对象
mes=MIMEMultipart()

mes['From']=Header(sender,'utf-8').encode()
mes['To']=Header(';'.join(receiver),'utf-8').encode()
suj='测试发送附件'
mes['Subject']=Header(suj,'utf-8').encode()

#构建邮件正文内容
text='python发送测试带附件的邮件'
text_plain=MIMEText(text,'plain','utf-8')
mes.attach(text_plain)


#构建附件
file='企业信息批量导入样表_上海 .xls'
send_file=MIMEText(open(file,'rb').read(),'base64','utf-8')
send_file['Content-Type']='application/octet-stream'''
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# send_file['Content-Disposition']='attachment;filename={}'.format(file)  这个发送不了中文名称的附件,下面这行代码才可以
send_file.add_header('Content-Disposition', 'attachment',filename=Header(file, 'utf-8').encode())
mes.attach(send_file)

smtp=smtplib.SMTP()
smtp.connect(mail_server,25)
# smtp.set_debuglevel(1)
smtp.login(mail_user,mail_passwd)
smtp.sendmail(sender,receiver,mes.as_string())

smtp.quit()



