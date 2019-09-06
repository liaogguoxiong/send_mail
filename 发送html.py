'''
@author: lgx
@Email:297979949@qq.com
@project: 发送邮件
@file: 发送html.py
@time: 2019-08-16 15:06
@desc:
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_server='smtp.qq.com'
mail_user='297979949@qq.com'
mail_passwd='rhoexjltojtcbghc'
sender='297979949@qq.com'
receiver=['526831381@qq.com','297979949@qq.com']

content='''<html>  
  <body>  
    <p> 
       Here is the <a href="http://www.baidu.com">link</a> you wanted.
    </p> 
  </body>  
</html>  '''

msg=MIMEText(content,'html','utf-8')
msg['From']=Header(sender,'utf-8')
msg['To']=Header(';'.join(receiver),'utf-8')
msg['Subject']=Header('send html test','utf-8')

smtp=smtplib.SMTP()
smtp.connect(mail_server,25)
smtp.login(mail_user,mail_passwd)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
