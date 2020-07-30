import requests
from requests.exceptions import RequestException
import re


def get_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response.text.encode('utf8'))
            return response.text
        return None
    except RequestException:
        return None


def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    parse_one_page(html)


def parse_one_page(html):
    pattern = re.compile(r'<dd>.*?board-index.*?">(\d+)</i>.*?'
                         r'data-src="(.*?)".*?', re.VERBOSE | re.DOTALL)
    items = re.findall(pattern, html)
    print(items)

# def parse_one_page(html):


if __name__ == '__main__':
    main()

'''
name"><a.*?>(.*?)</a>' +
                         r'.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?' +
                         r'fraction">(.*?)</i>.*?</dd>
                         '''



