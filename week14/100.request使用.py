# coding:utf-8

"""
    robots.txt协议：
        是一个君子协议，规定了网站中哪些数据可以被爬取，哪些数据不能被爬取
"""

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = 'http://www.biqukan.com/1_1094/5403177.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = requests.get(url, headers=headers)
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    content = bf.find_all('div', class_='showtxt')
    print(content[0].text.replace('\xa0' * 8, '\n\n'))
