# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart

from email.header import Header

mail_host = 'smtp.163.com'
mail_user = '17630704229@163.com'
mail_pass = 'ERHQKELJTYGDHJVJ'

# ERHQKELJTYGDHJVJ

sender = '17630704229@163.com'
receivers = ['2047023515@qq.com', '1919532973@qq.com']

msgRoot = MIMEMultipart('related')

msgRoot['From'] = Header('发送人', 'utf-8')
msgRoot['To'] = Header('接收人', 'utf-8')

subject = 'A letter to the king'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<h2>Who ary you?</h2>
<h2>Are you the king?</h2>
<p><img decoding="async" src="cid:image1"/></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

fp = open('creator.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error')
