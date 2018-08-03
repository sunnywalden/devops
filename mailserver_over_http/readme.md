邮件发送服务器

一、功能说明

    邮件服务器，提供统一的邮件发送接口。

二、用例

2.1 首先，请构造自己的邮件主题：

    
def http_post(html):

    url = 'http://ipaddr:5000/sendmail'           #调用邮件服务器API

    log_time = (date.today() - timedelta(1)).strftime("%Y年%m月%d日")  

    html = '<p>主机：%s</p><p></p>' % socket.gethostname() + html         #统一邮件格式要求，邮件正文中需要输出邮件来源的主机名

    receivers = [receivers_mailaddress]

    fromer = senders_mailaddress

    data = {'smtpserver': {'server': 'smtp.exmail.qq.com', 'mailuser': user, 'mailpasswd': pass},

            #邮件格式，主题中需要包含邮件类型，日期，服务，例如“统计结果：2018年08月02日日志状态统计”

            'emailsubject': {'subject': '统计结果：' + log_time + '日志状态统计', 'mess': html},

            'receivesuser': {'receiver': receivers},

            'fromuser': {'fromer': fromer},

            'filepath': {'path': '/tmp/', 'files': 'demo.txt'}}           #注意，附件需要上传到邮件服务器的对应路径，不支持远程发送

    headers = {'Content-Type': 'application/json'}

    req = urllib2.Request(url=url, headers=headers, data=json.dumps(data))

    response = urllib2.urlopen(req)

    return response.read()


2.2 发送

        http_post(html)
