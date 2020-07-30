import re
import requests
import json
from requests.exceptions import RequestException
import time
import pymongo


# Mongo DB 配置
collection_str = 'mongodb://localhost:27017'
client = pymongo.MongoClient(collection_str)
db = client.movies_top100
collection = db.movies


def get_one_page(url):  # 获取网页源代码
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Cookie': '__mta=121508535.1595848561485.1595922483191.1595922529540.5; uuid_n_v=v1; uuid='
                      '8CDABAE0CFFA11EABF2811F0086C462EB54447A08793412D822C82EF2719F3AA; _csrf=4beb4c6d'
                      '9d2ae07e5ede5ef2a6b5c2fe53dab246a35cf51a9825d36f360a9c6f; Hm_lvt_703e94591e87be6'
                      '8cc8da0da7cbd0be2=1595848561; _lxsdk_cuid=1738ffc8fa4c8-0913a087bb8933-b7a1334-14'
                      '4000-1738ffc8fa4c8; _lxsdk=8CDABAE0CFFA11EABF2811F0086C462EB54447A08793412D822C82E'
                      'F2719F3AA; mojo-uuid=e08ab01de6911fa57c11cf9819127ee3; mojo-session-id={"id":"4c'
                      '543d28a74d38f6dae62136a431f578","time":1595922431886}; __mta=121508535.15958485614'
                      '85.1595848616892.1595922450273.3; mojo-trace-id=9; Hm_lpvt_703e94591e87be68cc8da0da'
                      '7cbd0be2=1595922529; _lxsdk_s=1739463bf3b-a0a-402-d47%7C%7C14',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    # 提取 ：序号 封面图 电影名称 主演 上映时间 评分
    pattern = re.compile(r'<dd>.*?board-index.*?>(.*?)</i>.*?'
                         r'<img data-src="(.*?)".*?'
                         r'name">.*?title="(.*?)".*?'
                         r'star">\s*(.*?)\s*</p>.*?'
                         r'releasetime">(.*?)</p>.*?'
                         r'integer">(.*?)</i>.*?fraction">(.*?)</i>', re.S)
    items = re.findall(pattern, html)
    lists = []
    for item in items:
        lists.append({
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5].strip() + item[6].strip(),
        })
    return lists


def write_2_json(content):  # 接收解析后的字典列表,并将dict转换为str，写入json文件中
    with open('result.text', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    lists = parse_one_page(html)
    for dict_content in lists:
        print(dict_content)
        write_2_json(dict_content)
        save_data(dict_content)


def save_data(data):
    collection.update_one(
        {'title': data.get('title')},
        {'$set': data}, upsert=True)
    print('Saving successfully！')


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)











