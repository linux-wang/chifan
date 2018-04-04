# -*- coding:utf-8 -*-
from flask import Flask
app = Flask(__name__)

try:
    from local_setting import key, secret, username, password
except:
    from config import key, secret, username, password



def get_client():
    import fanfou
    consumer = {'key': key, 'secret': secret}
    client = fanfou.XAuth(consumer, username, password)
    fanfou.bound(client)
    return client


def tweet(content):
    client = get_client()
    body = {'status': content}
    resp = client.statuses.update(body)
    return resp


def get_public_timeline(count=10):
    import json
    client = get_client()
    resp = client.statuses.public_timeline()
    data = json.loads(resp.read())
    
    for fan in data:
        print fan['text']


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
