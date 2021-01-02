from common.fengzhuangdingwei import Base
from pageses.allpage.pages import SetPage
from appium import webdriver
import openpyxl
def loginOut():
    des = {
        "platformName": "Android",  # 手机是android还是ios
        "deviceName": "ca548277",  # 手机名称，通过adb devices获得
        "platformVersion": "10",  # android版本号
        "appPackage": "com.xingin.xhs",  # app包名
        "appActivity": "com.xingin.xhs.activity.SplashActivity",  # apk第一个启动页
        "noReset": True  # 不重置手机app
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des)
    bae = Base(driver)
    bae.click(SetPage.我)
    bae.click(SetPage.设置按钮)
    bae.click(SetPage.登出账户)
    bae.click(SetPage.确定)