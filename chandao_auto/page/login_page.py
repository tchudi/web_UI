#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from base.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage(BasePage):

    username_loc=(By.ID,'account')
    pwd_loc=(By.NAME,'password')
    submit_loc=(By.ID,'submit')
    user_loc=(By.CLASS_NAME,'user-name')


    def input_username(self,username):
        self.input(self.username_loc,username)

    def input_pwd(self,pwd):
        self.input(self.pwd_loc,pwd)

    def submit(self):
        self.click(self.submit_loc)

    def login_action(self,username='admin',pwd='Hd123456'):
        self.input_username(username)
        self.input_pwd(pwd)
        self.submit()

    def login(self,username='hudi',pwd='Hd123456'):
        self.openbrowser()
        self.input_username(username)
        self.input_pwd(pwd)
        self.submit()


    def get_login_user(self):
        user=self.find_element(self.user_loc)
        if user:
            return user.text
        else:
            return False

if __name__=="__main__":
    dr=webdriver.Chrome()
    l=LoginPage(dr)
    l.login()

