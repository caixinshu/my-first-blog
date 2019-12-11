#!/usr/bin/env python
# -*- coding=utf-8 -*-
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get('https://flight.qunar.com/')

#等待页面加载
tocity = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,'//input[@name="toCity"]'))
)
# tocity = driver.find_element_by_xpath('//input[@name="toCity"]')

tocity.send_keys('昆明')
time.sleep(1)

tocity.send_keys(Keys.RETURN)
search = driver.find_element_by_css_selector('button.btn_search')
search.click()
# 所有飞机信息
time.sleep(2)
# 等待
flights = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.XPATH,'//div[@class="m-airfly-lst"]/div[@class="b-airfly"]'))
)

for f in flights:
    row = {}
    airlines = f.find_element_by_xpath('.//div[@class="d-air"]')
    row['airline'] = airlines.text
    row['l-time'] = f.find_element_by_xpath('.//div[@class="sep-lf"]').text
    row['c-time'] = f.find_element_by_xpath('.//div[@class="sep-ct"]').text
    row['r-time'] = f.find_element_by_xpath('.//div[@class="sep-rt"]').text
    row['fake-price'] = f.find_element_by_xpath('//span[@class="prc_wp"]/em/b[i]').text

    print(row)
driver.quit()