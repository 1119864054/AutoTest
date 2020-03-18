#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: yans
# @Time : 2020/3/17 17:38

import requests
from bs4 import BeautifulSoup


class Reptile(object):

    def __init__(self, url):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        self.url = url
        self.page = requests.get(url, headers=header)

    # 拉取最新跟新消息
    def get_url_title(self):
        result = []
        soup = BeautifulSoup(self.page.text, 'html.parser')
        mostly_news = soup.select('.grey ul')

        # 遍历列表，获取有效信息
        for news in mostly_news:
            new = news.select('a')

            for single in new:
                if len(single) > 0:
                    try:
                        if single['href']:
                            href = self.url + single['href']
                    except Exception:
                        href = None
                    # 新闻标题
                    try:
                        if single['title']:
                            title = single['title']
                    except Exception:
                        title = None

                    if title is not None and href is not None:
                        article = Article(title, href)
                        result.append(article)
        return result


class Article:
    def __init__(self, title, href):
        self.title = title
        self.href = href

    def __str__(self):
        print(" title: " + self.title + "\n href: " + self.href)


test = Reptile("http://www.china-cotton.org/")
mostly_new = test.get_url_title()

for every_new in mostly_new:
    every_new.__str__()
