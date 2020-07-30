# coding:utf-8
import requests
from bs4 import BeautifulSoup


def get_html_code(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36'}
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        print('--网页获取成功--')
    return html.content


def get_name(html):
    soup = BeautifulSoup(html, 'lxml')
    book_list = soup.find(attrs={'id': 'book'})
    book_names = book_list.find_all(attrs={'class': 'title'})
    for book_one in book_names:
        print(book_one.string)


url = 'https://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book'
get_name(get_html_code(url))



