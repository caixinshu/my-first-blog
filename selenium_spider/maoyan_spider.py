#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400",
}

r = requests.get('https://maoyan.com/films/1218273',headers=headers)


# 字体加密