from appium import webdriver
#显式等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from time import sleep
class Base():
    #driver:webdriver.Remote 对driver进行申明，是从webdriver.Remote来的，申明之后才能用MobileBy调用
    def __init__(self,driver:webdriver.Remote):
        self.driver = driver
    def find(self,locator):
        #这里locator传的是个字典，第一个传的是获取元素的方式，第二个参数传对应的值
        #locator--->{"by":"id","value":"xxxx",name:'模块名'}
        #如果by的值是desc,就用find_element_by_accessibility_id的方式去查找
        sleep(2)
        if locator['by']=="desc":
            element = WebDriverWait(self.driver, 30, 0.2).until(lambda x:x.find_element_by_accessibility_id(locator['value']))
        elif locator['by']=="android":
            element = WebDriverWait(self.driver, 30, 0.3).until(
                lambda x: x.find_element_by_android_uiautomator(locator['value']))
        elif locator['by']=="text":
            element = WebDriverWait(self.driver, 60, 0.3).until(
                lambda x: x.find_element_by_xpath('//*[@text="%s"]'%locator['value']))
            #其他的如id等直接用located
        else:
            element = WebDriverWait(self.driver, 20, 0.3).until(EC.presence_of_element_located(locator))
        return element

    def click(self,locator):
        self.find(locator).click()

    def clear(self,locator):
        self.find(locator).clear()
    def send(self,locator,_text):
        self.find(locator).send_keys(_text)

        # 判断元素是否存在
    def is_element_exist(self, locator):
        try:
            self.find(locator)
            return True
        except:
            return False