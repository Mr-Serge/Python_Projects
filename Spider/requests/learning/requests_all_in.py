import requests
import re
import io
import sys

'''
# requests get请求 及相关方法
r = requests.get('https://www.baidu.com/')
r.encoding = 'utf8'
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
'''

'''
# requests get请求
r = requests.get('http://httpbin.org/get')
print(r.text)
'''

'''
# requests get + data请求
data = {'name': 'germey',
        'age': 22, }
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
'''

'''
# requests get + data请求 json转字典
data = {'name': 'germey',
        'age': 22, }
r = requests.get('http://httpbin.org/get', params=data)
print(type(r.text))
print(r.json())
print(type(r.json()))
'''

'''
# 知乎爬取探索页面
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
r = requests.get('http://www.zhihu.com/explore', headers = headers)
pattern = re.compile('<a class="ExploreRoundtableCard-title.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
'''

'''
# 抓取二进制数据(存储图片、视频、音频等)
# r.text 返回headers中的编码解析的结果，可以通过r.encoding = 'gbk'来变更解码方式
# r.content返回二进制结果
r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
'''

'''
# 上传文件_post方法_files关键词
files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)
'''

'''
# cookies 登录
# 写入text文件时，win会默认用GBK的方式去编码经过unicode解码的HTML源代码，会报错
# 解决方法：在创建text文件时，规定编码方式为utf-8"/print中加入encode
headers = {'Cookie':'_zap=439137d5-2e8a-430d-894e-68f80d3aab0a; _xsrf=AkSsQF7SQWYnPNOUVqHhJRDiMoRXLSat; '
                    'd_c0="ABAvCE1kdBCPTqYDQcVM3I487hntuAl64bQ=|1575468828"; ISSW=1; _ga=GA1.2.2062375179.'
                    '1582628950; UM_distinctid=17123fdf85a4bd-0b4927f859a8ea-f313f6d-144000-17123fdf85b3ae;'
                    ' tst=h; tshl=; CNZZDATA1272960301=1725803390-1585446625-%7C1590415223; z_c0="2|1:0|10:'
                    '1591254333|4:z_c0|92:Mi4xWlZLUUJRQUFBQUFBRUM4SVRXUjBFQ1lBQUFCZ0FsVk5QZXZGWHdCRUNBe'
                    'TZBdkJqLXQ3MV9MRHRqWGJUR3RnYWV3|7589e8938e3623e341204203d68b2b5f2e44c1a41166920cba444'
                    '729acc75805"; q_c1=215e01451ba549579a29955a8f0163df|1593488243000|1582590715000; _gid='
                    'GA1.2.818282931.1595645509; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1595725664,159572'
                    '5895,1595740604,1595757625; SESSIONID=IZnr2FCWUpSXmnJZkly1JtUXKTD2hXxNI8f7v8OBs7i; JO'
                    'ID=UVwXC0Nhd2m4f2yxVWqLvXlGgSxFLysNykYt9Ag_ADzqEgn8CfUsfuxzbb1fupRAAPkYHHM5oLzIkU-iOL'
                    'ZPFbM=; osd=U1oUBExjcWq3cG63VmWEv39FjiNHKSgCxUQr9wcwAjrpHQb-D_Yjce51brJQuJJDD_YaGnA2r'
                    '77OkkCtOrBMGrw=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1595766535; KLBRSID=e42bab77'
                    '4ac0012482937540873c03cf|1595766536|1595765522; _gat_gtag_UA_149949619_1=1',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/84.0.4147.89 Safari/537.36',
           }
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text.encode('utf8'))
#with open('zhihu.text', 'w', encoding= 'utf8') as f:
#    f.write(r.text)
'''

'''
# 会话维持
requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)


s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
'''

'''
# SSL验证
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
'''

'''
# 代理设置
proxies = {
    'http':'http://10.10.1.10:3128',
    'https':'http://10.10.1.10:1080',
}
requests.get('https://taobao.com', proxies=proxies)
'''

'''
# 超时设置
r = requests.get('https://www.taobao.com', timeout = 5)
print(r.text.encode('utf8'))
'''













