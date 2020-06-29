#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
dr=webdriver.Chrome()
dr.maximize_window()
dr.get('https://www.baidu.com')
sleep(1)

print(dr.title)
result=EC.title_is('百度一下，你就知道')(dr)
print(result)

loc=(By.ID,'s-bottom-layer-right')
text=dr.find_element(By.ID,'s-bottom-layer-right').text
print(text)
result1=EC.text_to_be_present_in_element(loc,'©2020 Baidu (京)-经营性-2017-0020京公网安备11000002000001号京ICP证030173号')(dr)
print(result1)
sleep(1)
dr.quit()
