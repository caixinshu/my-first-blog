#!/usr/bin/env python
# -*- coding=utf-8 -*-
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# import pyexcel





if __name__ == '__main__':
    keyword = 'iphone'
    if len(sys.argv)>1:
        keyword = sys.argv[1]
    # option = Options()
    # option.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=option)

    driver = webdriver.Chrome()
    driver.get('https://www.jd.com')
    driver.save_screenshot('1.jpg')

    ky = driver.find_element_by_id('key')
    ky.send_keys(keyword)
    # 直接使用键盘回车
    ky.send_keys(Keys.RETURN)

    driver.save_screenshot('2.jpg')
    has_next = True
    while has_next:
        time.sleep(1)

        cur_page = driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[@class="curr"]').text

        print(15*"="+cur_page+15*"=")

        # 获取全部列表的高度
        g_lists = driver.find_element_by_id('J_goodsList')
        y = g_lists.rect['y'] + g_lists.rect['height']
        # 下拉页面获得全部商品列表
        driver.execute_script('window.scrollTo(0,%s)'%y)
        # 找到商品列表
        pro = driver.find_elements_by_class_name('gl-item')


        for p in pro:
            row = {}
            sku = p.get_attribute('data-sku')
            row['price'] = p.find_element_by_css_selector('strong.J_%s'%sku).text
            row['name'] = p.find_element_by_css_selector('div.p-name>a>em').text
            row['comment'] = p.find_element_by_id('J_comment_%s'%sku).text
            try:
                row['shop'] = p.find_element_by_css_selector('div.p-shop>span>a').text
            except Exception:
                row['shop'] = 'None'

            print(row)

        next_page = driver.find_element_by_css_selector('a.pn-next')
        # if 'disabled' in next_page.get_attribute('class'):
        #     has_next = False
        if int(cur_page) == 5:
            has_next = False
        else:
            next_page.click()



    driver.quit()









