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


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/fanfou/chifan/<content>', methods=['GET'])
def fanfou(content):
    resp = tweet(content)
    if resp.code == 200:
        return "SUCESS!"
    else:
        return "FAILED!"


@app.route('/fanfou/public_timeline/get', methods=['GET'])
def get_public_timeline():
    import json
    client = get_client()
    resp = client.statuses.public_timeline()
    data = json.loads(resp.read())

    from datetime import datetime, timedelta
    output_file = 'data/' + (datetime.now() + timedelta(hours=8)).strftime("%Y%m%d") + '.txt'
    
    for fan in data:
        with open(output_file, 'a') as f:
            f.write(str(fan['user']['id']).encode('utf8') + '\n')

    return "WRITE SUCESS!"


@app.route('/fanfou/public_timeline/count/<dt>', methods=['GET'])
def get_user_num(dt):
    file_name = 'data/' + dt + '.txt'
    user_set = set()
    message_num = 0

    with open(file_name, 'r') as f:
        for i in f.readlines():
            if i.endswith('\n'):
                i = i[:-1]
            user_set.add(i)
            message_num = message_num + 1

    count_file = 'data/' + dt + '_count.txt'
    with open(count_file, 'a') as f:
        f.write(str(len(user_set)) + '_' + str(message_num))

    return "COUNT OVER!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
