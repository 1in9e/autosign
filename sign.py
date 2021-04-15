#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 14:01
# @Author  : le31ei
# @File    : auto_sign.py
import requests,json
import smtplib
from email.mime.text import MIMEText

session = requests.session()
req_header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}


def login():
    login_url = 'https://www.t00ls.net/login.json'
    login_data = {
        'action': 'login',
        'username': 'xx',
        'password': 'xx',
        'questionid': 3,    # 抓登陆包
        'answer': 'xx'
    }
    resp = session.post(login_url, data=login_data, headers=req_header)
    if resp.json()['status'] == 'success':
        return resp.json()['formhash']
    else:
        raise Exception('登录失败')

def sign(formhash):
    sign_url = 'https://www.t00ls.net/ajax-sign.json'
    sign_data = {
        'formhash': formhash,
        'signsubmit': 'true'
    }
    resp = session.post(sign_url, data=sign_data, headers=req_header)
    if resp.json()['status'] == 'success':
        print('签到成功')
        return '签到成功'
    else:
        print('签到失败: {}'.format(resp.json()['message']))
        return '签到失败：{}'.format(resp.json()['message'])

def show_my_ip():
    s = requests.get(url='http://httpbin.org/ip', headers=req_header)
    # js = json.loads(s.content)
    return str(json.loads(s.content)['origin'])

def send_mail(title, content=''):
    mail_pass = 'xxx'
    mail_name = 'xxx'
    mail_host = 'smtp.163.com'
    sender = 'xx@163.com'
    receivers = ['xx@qq.com']
    message = MIMEText(content)
    message['Subject'] = title
    message['From'] = sender
    message['To'] = receivers[0]
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(mail_name, mail_pass)
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        smtpObj.quit()
        print('发送成功')
    except smtplib.SMTPException as e:
        print('error', e)



def main():
    formhash = login()
    sign_output = sign(formhash)
    show_my_ip_output = show_my_ip()

    #
    # title: sign and home_ip
    # content: 
    #
    content = 'Home IP: ' + show_my_ip_output + '\n' + sign_output
    send_mail('sign and home_ip', content=content)


if __name__ == '__main__':
    main()
