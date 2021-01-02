from appium.webdriver.common.touch_action import TouchAction
class Base():
    def __init__(self,driver):
        self.driver = driver
        self.a = self.driver.get_window_size()  # 获取屏幕分辨率


    def swipeUp(self,t=10):
        # 滑动
        print(self.a)  # {'width': 1080, 'height': 1920}
        width = self.a['width']
        height = self.a['height']
        start_x = width / 2
        start_y = height / 5 * 4

        end_x = width / 2
        end_y = height / 5 * 1
        # 往上滑动
        for i in range(t):
            self.driver.swipe(start_x, start_y, end_x, end_y)

    def swipeDown(self):
        # 滑动
        print(self.a)  # {'width': 1080, 'height': 1920}
        width = self.a['width']
        height = self.a['height']
        start_x = width / 2
        start_y = height / 5 * 1

        end_x = width / 2
        end_y = height / 5 * 4
        # 往下滑动
        self.driver.swipe(start_x, start_y, end_x, end_y)

#e1是元素，x,y是坐标,count触摸次数
    def tab_new(self,e1=None,x=None,y=None,count=1):
        action = TouchAction(self.driver)
        if e1 is not None:
            action.tap(element=e1,count=count).perform() #能定位到元素就传元素
        else:
            action.tap(x=x,y=y,count=count).perform()#定位不到元素就传坐标


