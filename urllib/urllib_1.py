from  urllib import request

response = request.urlopen('http://www.baidu.com')   # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型

page = response.read()
page = page.decode('utf-8')
#print(page)

print(response.info())
print(response.getcode())
print(response.geturl())


