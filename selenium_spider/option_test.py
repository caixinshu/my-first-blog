#!/usr/bin/env python
# -*- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 需要Chrome 59版本以上 最新selenium
# req_url = "https://www.baidu.com"
# chrome_options=Options()
# #设置chrome浏览器无界面模式
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('lang=zh_CN.UTF-8')
#
# browser = webdriver.Chrome(chrome_options=chrome_options)
# # 开始请求
# browser.get(req_url)
# #打印页面源代码
# print(20*'=')
# #关闭浏览器
# browser.close()
# #关闭chreomedriver进程


# 反爬手段
'''
1.useragent识别
修改头信息里的useragent
2. 修改头信息
构造头信息
3.异步加载
分析网络请求，找到对应请求
4.参数加密
分析前端的代码构造。或者使用selenium和splash

'''
