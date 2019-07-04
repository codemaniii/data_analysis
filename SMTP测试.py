# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:26:31 2018

@author: 51869
"""
'''
前置入库
'''
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import pandas as pd
import numpy as np

my_sender='51869162@qq.com'                 # 发件人邮箱账号
my_pass = 'jsmtqapljpknbjgj'                # 发件人邮箱密码
my_user='51869162@qq.com'                   # 收件人邮箱账号，我这边发送给自己
test_message=str(np.random.rand(20,10))+"测试1231234"#测试传输额内容
'''

'''
def mail(massage):
    ret=True
    try:
        msg=MIMEText(massage,'plain','utf-8')
        msg['From']=formataddr(["邓耀宗昵称1234",my_sender])   # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["DYZ",my_user])                   # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="主题：发送邮件测试"                        # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)         # 发件人邮箱中的SMTP服务器，腾讯SMTP发送端口是465或者587
        server.login(my_sender, my_pass)                    # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret


#函数调用 
ret=mail(test_message)
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")