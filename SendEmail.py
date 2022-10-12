# -*- coding : utf-8 -*-
# @Time      : 2022/9/10 20:11
# @Author    : Zong
# @File      : EmailServer.py
# @Software  : PyCharm
# @Function  : 
# @ChangeLog :

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import Config


## 邮件设置
message = MIMEMultipart('mixed')   # 邮件内容，第二个可选参数要为html才可以
message['From'] = Header('2481814748@qq.com')   # 邮件发送者名字
message['To'] = Header('2481814748@qq.com')   # 邮件接收者名字
message['Subject'] = Header('理财助手Vitar的今日报告')   # 邮件主题

# html文本
html_text = '''
<p>大盘整体回暖，宜补仓购入。</p>
<p>正在等待您的下一步操作</p>
<img src="cid:image1">
<img src="cid:image2">
'''

# html邮件
message_html = MIMEText(html_text, 'html')

# 图片
with open(Config.imgs_path + "BasicFund_3year.png", 'rb') as image1:
    message_image1 = MIMEImage(image1.read())
    message_image1.add_header('Content-ID', '<image1>')
with open(Config.imgs_path + "BasicFund_3year.png", 'rb') as image2:
    message_image2 = MIMEImage(image2.read())
    message_image2.add_header('Content-ID', '<image2>')

# 附加到message
message.attach(message_html)
message.attach(message_image1)
message.attach(message_image2)

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")   # 连接 qq 邮箱
smtp.login("2481814748@qq.com", "idbzsqjqcyqbecae")   # 账号和授权码
smtp.sendmail("2481814748@qq.com", ["2481814748@qq.com"], message.as_string())   # 发送账号、接收账号和邮件信息
smtp.quit()