# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '18868191695@163.com'  #发件人
receiver = '1024306881@qq.com'#收件人
subject = '放假通知' #主题
smtpserver = 'smtp.163.com' #163SMTP服务器
username = '18868191695@163.com'#登录名
password = 'yym940216' #

msg = MIMEText('大家关好窗户', 'plain', 'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要；文本内容
subject='关好窗户，关好门窗'
msg['Subject']=subject
#msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = '18868191695@163.com'
msg['To'] = "1024306881@qq.com"
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

