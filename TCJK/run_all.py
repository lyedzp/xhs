#coding=utf-8
import time
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
import sys,getopt,os

def main(argv):
    name = 'xiaomi9'
    #h为帮助,n代表设备名称,n:表示n后面有参数
    try:
        opts,args = getopt.getopt(argv,"hn:",["deviceName="])
    except getopt.GetoptError:
        print('帮助信息： -n<deviceName>')
        sys.exit(2)
    for opt,arg in opts:
        if opt == '-h':
            print('帮助信息： -n<deviceName>')
            sys.exit()
        elif opt in ('-n','--deviceName'):
            name = arg
    print('手机名称为：',name)
    return name

# 指定测试用例为当前文件夹下的interface目录
test_dir = os.getcwd()
testsuit = defaultTestLoader.discover(test_dir,pattern='test*')
if __name__=='__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name='./report/'+now+'result.html'
    fp = open(report_name,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='appui自动化测试',
                            description='运行环境')
    runner.run(testsuit)
    fp.close()