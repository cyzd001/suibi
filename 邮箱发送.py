import smtplib
from email.mime.text import MIMEText
from email.header import Header

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# smtpserver = 'smtp.163.com'
# sender = 'caiy@huiyinxun.com'
# receivers = ['749949593@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
# message['To'] = Header("测试", 'utf-8')  # 接收者
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")

# 发送邮箱服务器
smtpserver = 'smtp.ym.163.com'
# 发送邮箱用户名/密码
user = 'caiy@huiyinxun.com'
password = 'Qwaszx12'
sender='caiy@huiyinxun.com'
# 接受者
receiver=['749949593@qq.com']
# 发送邮件主题
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(smtpserver, 994)    # 25 为 SMTP 端口号
    smtpObj.login(user,password)
    smtpObj.sendmail(sender, receiver, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")