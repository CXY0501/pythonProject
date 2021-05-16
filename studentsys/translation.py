import urllib.request
import urllib.parse
import json
import ssl

while True:
    content = input('请输入需要翻译的内容：')
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

    response = urllib.request.urlopen(url,data,context=context)
    html = response.read().decode('utf-8')
    result = json.loads(html)['translateResult'][0][0]['tgt']

    print('翻译的结果为：',end='')
    print(result)

    keepOn = int(input('是否继续翻译？0 退出 1 继续'))
    if keepOn == 0:
        break
    elif keepOn == 1:
        continue
    else:
        print('输入有误，请重新输入')
        keepOn = int(input('是否继续翻译？0 退出 1 继续'))