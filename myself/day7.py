import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.text import MIMENonMultipart
from email.mime.application import MIMEApplication
def send_email(smtpHost,sendAddr,password,recipientAddrs,subject='',content=''):
    msg=email.mime.multipart.MIMEMultipart()#定义内嵌自由资源的邮件体
    msg['from']=sendAddr #发件人邮箱
    receivers=recipientAddrs #收件人邮箱
    msg['subject']=subject
    content=content
    if len(receivers)>1:
        msg['To']=','.join(receivers) #群发邮件
    else:
        msg['To']=receivers[0]  #单个发邮件
    txt=MIMEText
