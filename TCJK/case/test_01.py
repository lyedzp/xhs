import sys



from common.start import start_app
from common.fengzhuangdingwei import Base
from common.login import Login
from common.homepage import homePage

import unittest
import warnings
from selenium import webdriver

class TestYaoQing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print()
        Login()
        homePage()
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #
    # def get_Result(self):
    #     result = []
    #     # 分享页面有微信好友，朋友圈等选项，所以用class可以获取这一组元素
    #     els = self.base.click(self.s4)
    #     # 循环去元组里面取每个元素的text
    #     for i in els:
    #         r = i.text
    #         result.append(r)
    #     return result
    #
    # def test_01(self):
    #     """我的足迹页面-分享"""
    #     self.base.click(self.s1)
    #     self.base.click(self.s2)
    #     self.base.click(self.s3)
    #     resultR = self.get_Result()
    #
    #         #期望值
    #     exceptresult = ["微信好友","朋友圈"]
    #     self.assertTrue(resultR==exceptresult)
if __name__=="__main__":
    unittest.main()
