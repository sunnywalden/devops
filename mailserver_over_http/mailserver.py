#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from flask import Flask,request
import json
from mailsend import Sendmail
 
app = Flask(__name__)
 
@app.route('/sendmail' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        jsondata = request.get_data()
        data = json.loads(jsondata)
#        s,e,f,r= data['smtpserver'],data['emailsubject'],data['filepath'],data['receivesuser']
        s,e,f,r= data['smtpserver'],data['emailsubject'],data['fromuser'],data['receivesuser']
        print('server printing',data['fromuser'])
        email = Sendmail(s['server'],s['mailuser'],s['mailpasswd'])
        email.mess(f['fromer'],e['subject'],e['mess'])
#        email.files(f['path'],f['files'])

#        print(e['subject'])
        print('Henry print:',f['fromer'])
        print '邮件正在发送...'
        #email.send(f['fromer'],r['receiver'])
        email.send('no-reply-devops@cloudin.cn',r['receiver'])
        return '邮件发送成功'
    else:
        return '<h1>只接受post请求！</h1>'
 
if __name__ =='__main__':
    app.run(debug=False,host='0.0.0.0')
