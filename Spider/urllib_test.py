# urllib
import urllib.request
import urllib.parse

'''
# get 方法
import urllib.request
response = urllib.request.urlopen('https://cn.bing.com/?mkt=zh-CN')
print(response.read())
print(response.status)
print(response.getheaders())
for k, v in response.getheaders():
    print(k, '=', v)
'''

'''
# request 对象
# 请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36'}
requests = urllib.request.Request('https://movie.douban.com/', headers = headers)
# 进行请求，把Request对象传入urlopen参数中
response = urllib.request.urlopen(requests)
print(response.read())
# 反爬豆瓣成功^_^
'''

'''
# 使用post方法来进行模拟登陆豆瓣
data = {'source': 'None',
        'redir': 'https://movie.douban.com/',
        'form_email': '15623856683',
        'form_password': '1114558916.',
        'remember': 'on',
        'login': '登录'}
# 将data的字典类型转换为get请求方式
data = bytes(urllib.parse.urlencode(data), encoding='utf8')
requests = urllib.request.Request('https://accounts.douban.com/password/login')
response = urllib.request.urlopen(requests)
print(response.read())
'''

'''
# post_method
import urllib.parse
import urllib.request
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
print(data)
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())
'''


'''
# TIME OUT
import socket
import urllib.request
import urllib.error


try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

'''

'''
import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(type(response))
print(response.read().decode('utf-8'))
'''

from http import cookiejar
cookie = cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://movie.douban.com/')
for c in cookie:
    print(c.name, '=', c.value)