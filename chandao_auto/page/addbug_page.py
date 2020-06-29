#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from base.basepage import BasePage
from selenium.webdriver.common.by import By
import time
from page.login_page import LoginPage
from selenium import webdriver

class AddbugPage(BasePage):
    test_loc = (By.LINK_TEXT,'测试')
    bug_loc = (By.CSS_SELECTOR, '#subNavbar > ul > li:nth-child(1)')
    add_loc = (By.CSS_SELECTOR, 'a.btn.btn-primary')
    product_loc1 = (By.CSS_SELECTOR, 'div.input-group>div#product_chosen')
    product_loc2 = (By.CSS_SELECTOR, 'div.input-group>div#product_chosen>div>ul>li:nth-child(2)')

    version_loc1 = (By.CSS_SELECTOR, 'div#openedBuild_chosen>ul.chosen-choices')
    version_loc2 = (By.CSS_SELECTOR, 'div#openedBuild_chosen>div>ul>li:nth-child(2)')

    title_loc = (By.CSS_SELECTOR, 'input#title')

    frame_loc=(By.CSS_SELECTOR,'iframe.ke-edit-iframe')
    body_loc = (By.CSS_SELECTOR, 'body.article-content')

    submit_loc = (By.CSS_SELECTOR, 'button#submit')

    result_loc=(By.CSS_SELECTOR,'#bugList > tbody > tr:nth-child(1) > td.c-title.text-left > a')
    title = time.strftime('%Y%m%d%H%M%S', time.localtime())

    def add_bug(self):
        self.click(self.test_loc)
        self.click(self.bug_loc)
        self.click(self.add_loc)
        self.click(self.product_loc1)
        self.click(self.product_loc2)
        time.sleep(1)
        self.click(self.version_loc1)
        self.click(self.version_loc2)

        #输入用例标题
        print(self.title)
        self.input(self.title_loc,self.title)

        #切换表单
        self.switch_frame(self.frame_loc)

        #输入重现步骤
        body = '''
        [步骤]111111,
        22222,
        33333.
        [结果]rrrrrrr
        [期望]eeeee
        '''

        self.clear(self.body_loc)
        self.input(self.body_loc,body)


        self.switch_content_frame()

        self.scroll_end()

        self.click(self.submit_loc)

    def is_content(self):
        #time.sleep(2)
        # print(self.get_text(self.result_loc))
        # print(self.title)
        if self.get_text(self.result_loc)==self.title:

            return True
        else:
            return False

if __name__=="__main__":
    dr=webdriver.Chrome()
    dr.maximize_window()

    l=LoginPage(dr)
    a=AddbugPage(dr)

    l.login()

    a.add_bug()
    print(a.is_content())


