#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from page.login_page import LoginPage
from time import sleep
#import ddt
d=[{'username':'hudi','pwd':'Hd123456'},
   {'username':'admin','pwd':'Hd123456'}]

#@ddt.ddt
class Login(unittest.TestCase):
    def setUp(self):
        self.dr=webdriver.Chrome()
        self.dr.maximize_window()
        self.l=LoginPage(self.dr)
        self.l.openbrowser()

    def test_01(self):
        self.l.login_action()
        result=self.l.get_login_user()
        self.assertEqual(result,'admin')

    def test_02(self):
        self.l.login_action('admin','Hd1233333')
        result=self.l.get_login_user()
        self.assertFalse(result)
    #
    # @ddt.data(*d)
    # def test_03(self,d):
    #     self.l.login_action(d['username'],d['pwd'])
    #     result=self.l.get_login_user()
    #     self.assertEqual(result,'胡迪')

    def tearDown(self):
        sleep(2)
        self.l.close()

if __name__=="__main__":
    unittest.main()

