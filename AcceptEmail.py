# -*- coding : utf-8 -*-
# @Time      : 2022/9/12 20:19
# @Author    : Zong
# @File      : AcceptEmail.py
# @Software  : PyCharm
# @Function  : 接受邮件，每隔五分钟运行一次
# @ChangeLog :

import datetime
import poplib
from email import parser
import email
from email.header import decode_header
from email.utils import parseaddr
import dateutil.utils


# 接收邮件
def accpet_mail_func():
    # 登录server
    host = 'pop.qq.com'
    username = '2481814748@qq.com'
    password = 'idbzsqjqcyqbecae'
    server = poplib.POP3_SSL(host, 995)
    server.set_debuglevel(0)
    server.user(username)
    server.pass_(password)

    # 获取最新的邮件
    resp, mails, octets = server.list()
    index = len(mails)  # 邮件的总数
    resp, lines, octets = server.retr(index)  # 可以取出最新的邮件的信息
    # lines存储了邮件的原始文本的每一行，可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = parser.Parser().parsestr(msg_content)

    # 解析邮件
    # 如果发送人不是自己就return
    email_header = get_header(msg)
    if email_header.get('From') != '2481814748@qq.com':
        return

    # 如果日期不是今天就return
    email_date  = get_date(msg)
    if email_date.date() != dateutil.utils.today().date() :
        return

    # 判断操作
    email_content = get_content(msg)
    enter_loc = email_content.find('\n')
    action = email_content[0 : enter_loc]

    # 关闭连接:
    server.quit()

    return action

#通过decode，将Subject其变为中文
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# 获取邮件头
def get_header(msg):
    header_dict = {}
    for header in ['From', 'To', 'Subject']:
        value = msg.get(header, '')
        if value:
            #文章的标题有专门的处理方法
            if header == 'Subject':
                value = decode_str(value)
                header_dict[header] = value # 添加
            elif header in ['From','To']:
            #地址也有专门的处理方法
                hdr, addr = parseaddr(value)
                value = decode_str(addr)
                header_dict[header] = value # 添加
    return header_dict

# 获取邮件日期
def get_date(msg):
    date=email.header.decode_header(msg.get('date'))

    utcstr = date[0][0].replace('+00:00', '')
    global utcdatetime
    try:
        utcdatetime = datetime.datetime.strptime(utcstr, '%a, %d %b %Y %H:%M:%S +0000 (GMT)')
        localdatetime = utcdatetime + datetime.timedelta(hours=+8)
        localtimestamp = localdatetime.timestamp()
    except:
        utcdatetime = datetime.datetime.strptime(utcstr, '%a, %d %b %Y %H:%M:%S +0800')
        localtimestamp = utcdatetime.timestamp()
    return utcdatetime

# 获取邮件的字符编码，首先在message中寻找编码，如果没有，就在header的Content-Type中寻找
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos+8:].strip()
    return charset

# 获取正文信息
def get_content(msg):
    for part in msg.walk():
        content_type = part.get_content_type()
        charset = guess_charset(part)
        #如果有附件，则直接跳过
        if part.get_filename()!=None:
            continue
        email_content_type = ''
        content = ''
        if content_type == 'text/plain':
            email_content_type = 'text'
        elif content_type == 'text/html':
            continue #不要html格式的邮件
            email_content_type = 'html'
        if charset:
            try:
                content = part.get_payload(decode=True).decode(charset)
            #这里遇到了几种由广告等不满足需求的邮件遇到的错误，直接跳过了
            except AttributeError:
                print('type error')
            except LookupError:
                print("unknown encoding: utf-8")
        if email_content_type =='':
            continue
            #如果内容为空，也跳过
        return content


# 测试
accpet_mail_func()