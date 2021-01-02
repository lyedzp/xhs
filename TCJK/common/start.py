from appium import webdriver
from run_all import main
import sys




des_leidian = {
        "platformName":"Android",#手机是android还是ios
        "deviceName":"emulator-5554",#手机名称，通过adb devices获得
        "platformVersion":"7.1.2",#android版本号
        "appPackage":"com.tchhy.tcjk",#app包名
        "appActivity":"com.tchhy.tcjk.ui.splash.SplashActivity",#apk第一个启动页
        "udid":"emulator-5554",
        "noReset":True#不重置手机app
    }

des_xiaomi9 = {
        "platformName":"Android",#手机是android还是ios
        "deviceName":"ca548277",#手机名称，通过adb devices获得
        "platformVersion":"10",#android版本号
        "appPackage":"com.tchhy.tcjk",#app包名
        "appActivity":"com.tchhy.tcjk.ui.splash.SplashActivity",#apk第一个启动页
        "udid":"ca548277",#识别手机唯一标志
        "noReset":True#不重置手机app
    }
def start_app(n=None):
    if n==None:
        #这句话表示设备名称从命令行获取
        deviceName = main(sys.argv[1:])
    else:
        deviceName=n

    if deviceName=="leidian":
        des = des_leidian
    elif deviceName=="xiaomi9":
        des = des_xiaomi9
    else:
        des = des_leidian
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des)
    return driver

