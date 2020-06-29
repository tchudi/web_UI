#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class BasePage():
    def __init__(self, dr,url='http://127.0.0.1:81/zentao/user-login.html'):
        self.dr = dr
        self.url=url


    def openbrowser(self):
        self.dr.get(self.url)

    def find_element(self, loc):
        try:
            element = WebDriverWait(self.dr, 10).until(lambda dr: dr.find_element(*loc))
            return element

        except:
            print(loc,'元素未找到')
            #return False

    def click(self, loc):
        return self.find_element(loc).click()

    def input(self, loc, value):
        return self.find_element(loc).send_keys(value)

    def get_text(self,loc):
        return self.find_element(loc).text

    def switch_frame(self,loc):
        frame_loc=self.find_element(loc)
        return self.dr.switch_to.frame(frame_loc)

    def switch_content_frame(self):
        return self.dr.switch_to_default_content()

    def scroll_end(self):
        js = '$(window).scrollTop(document.body.scrollHeight)'
        return self.dr.execute_script(js)

    def clear(self,loc):
        return self.find_element(loc).clear()

    def close(self):
        return self.dr.quit()


if __name__ == "__main__":
    dr = webdriver.Chrome()
    b = BasePage(dr,'https://www.baidu.com')
    b.openbrowser()
    loc = (By.ID, 'kw')
    b.input(loc, 'python')

