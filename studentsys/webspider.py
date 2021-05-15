import urllib.request

response = urllib.request.urlopen('http://placekitten.com/1000/1000')
html = response.read()
with open('cat1000_1000.jpg','wb') as file:
    file.write(html)

print(response.geturl())
print(response.info())
print(response.getcode())