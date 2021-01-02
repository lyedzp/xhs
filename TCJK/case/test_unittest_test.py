#encoding='UTF-8'
import sys
sys.path.extend(['D:\\TCJK'])
from appium import webdriver

import unittest
from time import sleep
des = {
        "platformName":"Android",#手机是android还是ios
        "deviceName":"ca548277",#手机名称，通过adb devices获得
        "platformVersion":"10",#android版本号
        "appPackage":"com.xingin.xhs",#app包名
        "appActivity":"com.xingin.xhs.activity.SplashActivity",#apk第一个启动页
        "noReset":True#不重置手机app
    }


class TestYaoQing(unittest.TestCase):
    s1={'by': 'text', 'value': '我的'}
    s2 = {'by': 'text', 'value': '我的足迹'}
    s3 = {'by': 'text', 'value': 'sharenew'}
    s4 = {"by":"class","value":"android.view.View"}
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des)
        cls.driver.wait_activity("com.yipiao/com.zt.main.entrance.MainActivity", 20)
        cls.base = Base(cls.driver)
        # 判断更新弹框中“下次再说”是否存在,如果弹框存在，先点下次再说，如果不存在，直接点我的
        tan_loc = {"by": "text", "value": "下次再说", "timeout": "5"}
        if cls.base.is_element_exist(tan_loc):
            cls.base.click({"by": "text", "value": "下次再说"})
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def get_Result(self):
        result = []
        # 分享页面有微信好友，朋友圈等选项，所以用class可以获取这一组元素
        els = self.base.click(self.s4)
        # 循环去元组里面取每个元素的text
        for i in els:
            r = i.text
            result.append(r)
        return result


    def test_01(self):
        """我的足迹页面-分享"""
        self.base.click(self.s1)
        self.base.click(self.s2)
        self.base.click(self.s3)
        resultR = self.get_Result()

            #期望值
        exceptresult = ["微信好友","朋友圈"]
        self.assertTrue(resultR==exceptresult)
    if __name__=="__main__":
        unittest.main()



