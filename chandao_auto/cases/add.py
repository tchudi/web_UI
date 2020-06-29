#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


dr=webdriver.Chrome()
dr.implicitly_wait(10)
dr.maximize_window()
dr.get('http://127.0.0.1:81/zentao/user-login.html')
dr.find_element(By.ID,'account').send_keys('hudi')
dr.find_element(By.NAME,'password').send_keys('Hd123456')
dr.find_element(By.ID,'submit').click()

dr.find_element(By.LINK_TEXT,'测试').click()
dr.find_element(By.CSS_SELECTOR,'#subNavbar > ul > li:nth-child(1)').click()
dr.find_element(By.CSS_SELECTOR,'a.btn.btn-primary').click()


dr.find_element(By.CSS_SELECTOR,'div.input-group>div#product_chosen').click()
dr.find_element(By.CSS_SELECTOR,'div.input-group>div#product_chosen>div>ul>li:nth-child(2)').click()


time.sleep(2)
dr.find_element(By.CSS_SELECTOR,'div#openedBuild_chosen>ul.chosen-choices').click()
dr.find_element(By.CSS_SELECTOR,'div#openedBuild_chosen>div>ul>li:nth-child(2)').click()


title=time.strftime('%Y%m%d%H%M%S',time.localtime())
dr.find_element(By.CSS_SELECTOR,'input#title').send_keys(title)



frame=dr.find_element(By.CSS_SELECTOR,'iframe.ke-edit-iframe')
dr.switch_to.frame(frame)
dr.find_element(By.CSS_SELECTOR,'body.article-content').clear()
dr.find_element(By.CSS_SELECTOR,'body.article-content').send_keys('1111 2222   333333')

dr.switch_to_default_content()
time.sleep(1)
js='$(window).scrollTop(document.body.scrollHeight)'
dr.execute_script(js)
time.sleep(1)
dr.find_element(By.CSS_SELECTOR,'button#submit').click()

time.sleep(2)
dr.quit()