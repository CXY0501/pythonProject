import base64
import urllib.request
import os
import base64

print(base64.b64decode('MjAyMTA1MTgtNzc='.encode('utf-8')))
print(base64.b64decode('MjAyMTA1MTgtNzY='.encode('utf-8')))
print(base64.b64decode('MjAyMTA1MTgtNzU='.encode('utf-8')))
print(base64.b64decode('MjAyMTA1MTctNjg='.encode('utf-8')))

print(base64.b64encode(b'20210518-77'))
print(base64.b64encode(b'20210518-76'))
print(str(base64.b64encode(b'20210518-75')))

url = 'http://jandan.net/girl/'
page_num = 75
# print(type('20210518-' + str(page_num)))
page_bnum = bytes('20210518-' + str(page_num),'ascii')

page_byte = str(base64.b64encode(page_bnum))

page_new = page_byte.split('\'')[1]

page_url = url + page_new + '#comments'

print(page_byte)
print(type(page_byte))

print(page_byte.split('\'')[1])
print(page_url)

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('user-agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    return html[a,b]

def download(folder='OOXX',pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/girl/"
    page_num = 75
    # page_num = get_page(url)
    add_list = []

    for i in range(pages):
        page_num -= i
        page_bnum = bytes('20210518-' + str(page_num),'ascii')
        page_byte = str(base64.b64encode(page_bnum))
        page_new = page_byte.split('\'')[1]
        page_url = url + page_new + '#comments'
        add_list.append(page_url)

    print(add_list)


if __name__ == '__main__':
    download()