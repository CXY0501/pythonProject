import time
import urllib.request
import urllib.parse
import json
import ssl

while True:
    content = input('请输入需要翻译的内容(输入q退出)：')
    if content == 'q' or content == 'Q':
        break
    else:
        context = ssl._create_unverified_context()
        # print(type(context))
        # url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        # data = {
        # 'from': 'zh',
        # 'to': 'en',
        # 'query': '我要学python，哈哈哈哈哈哈',
        # 'transtype': 'translang',
        # 'simple_means_flag': '3',
        # 'sign': '620952.891561',
        # 'token': '34a769e91427ad6d4d24cceaa355deb2',
        # 'domain': 'common'
        # }
        url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        data = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '16211214280498',
        'sign': '313a6a78ec15417b289e318c6416f954',
        'lts': '1621121428049',
        'bv': 'cf6acf0703967eb2d4e6429633fcbf38',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
        }

        data = urllib.parse.urlencode(data).encode('utf-8')

        req = urllib.request.Request(url,data,head)
        response = urllib.request.urlopen(req,context=context)
        html = response.read().decode('utf-8')
        result = json.loads(html)['translateResult'][0][0]['tgt']

        print('翻译的结果为：',end='')
        print(result)

        # print (req.headers)

    time.sleep(2)
