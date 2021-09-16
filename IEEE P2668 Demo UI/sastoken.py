# coding: utf-8


import base64
import hmac
import random
import time
# from urllib.request import quote
from urllib.parse import quote


def sas_token(method, namespace, sec_key):
    version = '2018-10-31'
    res = 'mqs/%s' % namespace
    et = str(int(time.time()) + 10 ** 6)
    # res = 'mqs/%s' % namespace # 将要访问的资源URI，格式是mqs/{ns}，需要进行URL编码
    key = base64.b64decode(sec_key)
    org = et + '\n' + method + '\n' + res + '\n' + version
    b = hmac.new(key=key, msg=org.encode(), digestmod=method)
    sign = base64.b64encode(b.digest()).decode()
    sign = quote(sign, safe='')

    res = 'res=%s' % res
    sign = 'sign=%s' % sign
    et = 'et=%s' % et
    method = 'method=%s' % method
    version = 'version=%s' % version
    list_token = [res, sign, et, method, version]
    random.shuffle(list_token)
    token = '&'.join(list_token)
    return token

