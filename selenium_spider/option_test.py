#!/usr/bin/env python
# -*- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


req_url = "https://www.baidu.com"
chrome_options=Options()
#设置chrome浏览器无界面模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('lang=zh_CN.UTF-8')

browser = webdriver.Chrome(chrome_options=chrome_options)
# 开始请求
browser.get(req_url)
#打印页面源代码
print(20*'=')
#关闭浏览器
browser.close()
#关闭chreomedriver进程
