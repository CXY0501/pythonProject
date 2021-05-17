import base64
import urllib.request
import os
import base64

print(base64.b64decode('MjAyMTA1MTctNjY='.encode('utf-8')))
print(base64.b64decode('MjAyMTA1MTctNjg='.encode('utf-8')))

def get_page(url):
    pass

def download(folder='OOXX',pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/girl"
    page_num = get_page(url)

    for i in range(pages):
        page_num -= i
