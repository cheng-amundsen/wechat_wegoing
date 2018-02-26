# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 20:44
# @Author  : Mocha Lee
# @Email   : 1446684220@qq.com
# @File    : 1.py
# @Software: PyCharm Community Edition


import requests
import execjs
import json
import time
import traceback


session = requests.session()
APPID = 'wx7a727ff7d940bb3f'

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Accept-Encoding': 'br, gzip, deflate',
    'Accept-Language': 'zh-cn', 'Accept': '*/*',
    'Referer': 'https://servicewechat.com/wx7a727ff7d940bb3f/23/page-frame.html',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN'
}

def get_jsfile(filename):
    with open(filename, 'rb+') as f:
        data = f.read()
    return data.decode()


def aes_enc(data, key, iv):
    bjs = get_jsfile('crypto.js')
    result = execjs.compile(bjs).call('enc', data, key, iv)
    return result


def get_enckey(sessionid, nonce):
    n, s, r, a = '0123456789abcdef', '', 4026531840, 28
    for o in range(8):
        s += n[(r & nonce) >> a]
        r >>= 4
        a -= 4
    for h in range(12):
        s += n[(240 & ord(sessionid[h])) >> 4]
        s += n[15 & ord(sessionid[h])]
    return s


def data_enc(sessionid, nonce, data):
    if not isinstance(data, str):
        print('data type error!')
        return None

    key = get_enckey(sessionid, nonce)
    return aes_enc(data, key, '0123456789abcdef')


def sync_score(sessionid, data):
    url = 'https://game.weixin.qq.com/cgi-bin/gametetrisws/syncgamev2?session_id={}'.format(sessionid)
    print('url: ', url)
    req = session.post(
        url,
        data=json.dumps(data),
        headers = headers,
        verify=False
    ).json()
    print(req)
    if req.get('errcode', -1) == 0:
        print('sync_score success!')
    else:
        print('[sorry, some error happend! please contact the author.]')


def start_game(sessionid):
    url = 'https://game.weixin.qq.com/cgi-bin/gametetrisws/startgamev2?session_id={}'.format(sessionid)
    data = {
        "game_version": 5,
        "appid": "wx7a727ff7d940bb3f"
    }
    req = session.post(url, data=json.dumps(data), headers=headers, verify=False).json()
    print(req)
    if req.get('errcode', -1) == 0:
        print('start_game success!')
        return req.get('data').get('nonce')
    else:
        print('[sorry, some error happend! please contact the author.]')
        return None


def main():
    sessionid = input('please input sessionid:')

    # start game
    print('\r\n', '*'*30, 'start game', '*'*30)
    nonce = start_game(sessionid)
    use_time = 120
    param = {
        "game_behav_list": [
            {"key": "newscore", "value": 233000},
            {"key": "level", "value": 334},
            {"key": "baoshi", "value": 233},
            {"key": "combo", "value": 233}],
        "use_time": use_time,
        "sync_type": 1,
        "combo_list": [0, 233],
        "progress": 0
    }
    data = data_enc(sessionid, nonce, json.dumps(param))
    data = {
        "data": data,
        "game_version": 5,
        "appid": "wx7a727ff7d940bb3f",
        "nonce": nonce
    }

    print('\r\n', '*'*30, 'playing game', '*'*30)
    while use_time > 0:
        print('playing game, please wait {} seconds.'.format(use_time))
        use_time -= 10
        time.sleep(10)

    print('\r\n', '*'*30, 'sync score', '*'*30)
    sync_score(sessionid, data)
    input('run over.')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('[sorry, some error happend! please contact the author.]')
        traceback.print_exc()
        input('run over.')
