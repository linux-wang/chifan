# -*- coding:utf-8 -*-
from flask import Flask
app = Flask(__name__)

try:
    from local_setting import key, secret, username, password
except:
    from config import key, secret, username, password


def tweet(content):
    import fanfou 
    consumer = {'key': key, 'secret': secret}
    client = fanfou.XAuth(consumer, username, password)
    fanfou.bound(client)
    body = {'status': content}
    resp = client.statuses.update(body)
    return resp


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/fanfou/<content>', methods=['GET'])
def fanfou(content):
    resp = tweet(content)
    if resp.code == 200:
        return "SUCESS!"
    else:
        return "FAILED!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
