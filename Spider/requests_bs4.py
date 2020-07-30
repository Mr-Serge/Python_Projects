# coding:utf-8
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def get_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('---网页获取成功---')
            return response.content
        else:
            print('---网页获取失败---')
            return None
    except RequestException:
        return None


def parse_one_rubirc(html):
    soup = BeautifulSoup(html, 'lxml')
    news_rubric = soup.find(attrs={'frag': '标题'}).string
    contents = {news_rubric: []}
    news_title_list = soup.find(attrs={'class': 'news_list'})
    titles = news_title_list.find_all(attrs={'class': 'news_title'})
    for t in titles:
        contents[news_rubric].append(t.string)
    print(contents)


def parse_rubircs(html):
    soup = BeautifulSoup(html, 'lxml')
    news_rubric = soup.find(attrs={'frag': '标题'}).string
    contents = {news_rubric: []}
    news_title_list = soup.find(attrs={'class': 'news_list'})
    titles = news_title_list.find_all(attrs={'class': 'news_title'})
    for t in titles:
        contents[news_rubric].append(t.string)
    print(contents)


def main():
    url = 'http://www.wust.edu.cn/jxzdh/'
    html = get_one_page(url)
    print(html)
    parse_one_rubirc(html)


if __name__ == '__main__':
    main()
