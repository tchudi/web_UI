#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

import ddt
import unittest

d=[{'username':1}]

@ddt.ddt
class MyTest(unittest.TestCase):
    @ddt.data(*d)
    def test01(self,d):
        print(d)

if __name__=='__main__':
    unittest.main()
